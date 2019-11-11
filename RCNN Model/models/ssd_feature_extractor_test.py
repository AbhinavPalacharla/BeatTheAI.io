# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Base test class SSDFeatureExtractors."""

from abc import abstractmethod

import itertools
import numpy as np
import tensorflow as tf

from google.protobuf import text_format
from object_detection.builders import hyperparams_builder
from object_detection.protos import hyperparams_pb2
from object_detection.utils import test_case


class SsdFeatureExtractorTestBase(test_case.TestCase):

  def _build_conv_hyperparams(self, add_batch_norm=True):
    conv_hyperparams = hyperparams_pb2.Hyperparams()
    conv_hyperparams_text_proto = """
      activation: RELU_6
      regularizer {
        l2_regularizer {
        }
      }
      initializer {
        truncated_normal_initializer {
        }
      }
    """
    if add_batch_norm:
      batch_norm_proto = """
        batch_norm {
          scale: false
        }
      """
      conv_hyperparams_text_proto += batch_norm_proto
    text_format.Merge(conv_hyperparams_text_proto, conv_hyperparams)
    return hyperparams_builder.KerasLayerHyperparams(conv_hyperparams)

  def conv_hyperparams_fn(self):
    with tf.contrib.slim.arg_scope([]) as sc:
      return sc

  @abstractmethod
  def _create_feature_extractor(self,
                                depth_multiplier,
                                pad_to_multiple,
                                use_explicit_padding=False,
                                num_layers=6,
                                use_keras=False,
                                use_depthwise=False):
    """Constructs a new feature extractor.

    Args:
      depth_multiplier: float depth multiplier for feature extractor
      pad_to_multiple: the nearest multiple to zero pad the input height and
        width dimensions to.
      use_explicit_padding: use 'VALID' padding for convolutions, but prepad
        inputs so that the output dimensions are the same as if 'SAME' padding
        were used.
      num_layers: number of SSD layers.
      use_keras: if True builds a keras-based feature extractor, if False builds
        a slim-based one.
      use_depthwise: Whether to use depthwise convolutions.
    Returns:
      an ssd_meta_arch.SSDFeatureExtractor or an
      ssd_meta_arch.SSDKerasFeatureExtractor object.
    """
    pass

  def _extract_features(self,
                        image_tensor,
                        depth_multiplier,
                        pad_to_multiple,
                        use_explicit_padding=False,
                        use_depthwise=False,
                        num_layers=6,
                        use_keras=False):
    kwargs = {}
    if use_explicit_padding:
      kwargs.update({'use_explicit_padding': use_explicit_padding})
    if use_depthwise:
      kwargs.update({'use_depthwise': use_depthwise})
    if num_layers != 6:
      kwargs.update({'num_layers': num_layers})
    if use_keras:
      kwargs.update({'use_keras': use_keras})
    feature_extractor = self._create_feature_extractor(
        depth_multiplier,
        pad_to_multiple,
        **kwargs)
    if use_keras:
      feature_maps = feature_extractor(image_tensor)
    else:
      feature_maps = feature_extractor.extract_features(image_tensor)
    return feature_maps

  def check_extract_features_returns_correct_shape(self,
                                                   batch_size,
                                                   image_height,
                                                   image_width,
                                                   depth_multiplier,
                                                   pad_to_multiple,
                                                   expected_feature_map_shapes,
                                                   use_explicit_padding=False,
                                                   num_layers=6,
                                                   use_keras=False,
                                                   use_depthwise=False):

    def graph_fn(image_tensor):
      return self._extract_features(
          image_tensor,
          depth_multiplier,
          pad_to_multiple,
          use_explicit_padding=use_explicit_padding,
          num_layers=num_layers,
          use_keras=use_keras,
          use_depthwise=use_depthwise)

    image_tensor = np.random.rand(batch_size, image_height, image_width,
                                  3).astype(np.float32)
    feature_maps = self.execute(graph_fn, [image_tensor])
    for feature_map, expected_shape in itertools.izip(
        feature_maps, expected_feature_map_shapes):
      self.assertAllEqual(feature_map.shape, expected_shape)

  def check_extract_features_returns_correct_shapes_with_dynamic_inputs(
      self,
      batch_size,
      image_height,
      image_width,
      depth_multiplier,
      pad_to_multiple,
      expected_feature_map_shapes,
      use_explicit_padding=False,
      num_layers=6,
      use_keras=False,
      use_depthwise=False):

    def graph_fn(image_height, image_width):
      image_tensor = tf.random.uniform([batch_size, image_height, image_width,
                                        3], dtype=tf.float32)
      return self._extract_features(
          image_tensor,
          depth_multiplier,
          pad_to_multiple,
          use_explicit_padding=use_explicit_padding,
          num_layers=num_layers,
          use_keras=use_keras,
          use_depthwise=use_depthwise)

    feature_maps = self.execute_cpu(graph_fn, [
        np.array(image_height, dtype=np.int32),
        np.array(image_width, dtype=np.int32)
    ])
    for feature_map, expected_shape in itertools.izip(
        feature_maps, expected_feature_map_shapes):
      self.assertAllEqual(feature_map.shape, expected_shape)

  def check_extract_features_raises_error_with_invalid_image_size(
      self,
      image_height,
      image_width,
      depth_multiplier,
      pad_to_multiple,
      use_keras=False,
      use_depthwise=False):
    preprocessed_inputs = tf.compat.v1.placeholder(tf.float32, (4, None, None, 3))
    feature_maps = self._extract_features(
        preprocessed_inputs,
        depth_multiplier,
        pad_to_multiple,
        use_keras=use_keras,
        use_depthwise=use_depthwise)
    test_preprocessed_image = np.random.rand(4, image_height, image_width, 3)
    with self.test_session() as sess:
      sess.run(tf.compat.v1.global_variables_initializer())
      with self.assertRaises(tf.errors.InvalidArgumentError):
        sess.run(feature_maps,
                 feed_dict={preprocessed_inputs: test_preprocessed_image})

  def check_feature_extractor_variables_under_scope(self,
                                                    depth_multiplier,
                                                    pad_to_multiple,
                                                    scope_name,
                                                    use_keras=False,
                                                    use_depthwise=False):
    variables = self.get_feature_extractor_variables(
        depth_multiplier,
        pad_to_multiple,
        use_keras=use_keras,
        use_depthwise=use_depthwise)
    for variable in variables:
      self.assertTrue(variable.name.startswith(scope_name))

  def get_feature_extractor_variables(self,
                                      depth_multiplier,
                                      pad_to_multiple,
                                      use_keras=False,
                                      use_depthwise=False):
    g = tf.Graph()
    with g.as_default():
      preprocessed_inputs = tf.compat.v1.placeholder(tf.float32, (4, None, None, 3))
      self._extract_features(
          preprocessed_inputs,
          depth_multiplier,
          pad_to_multiple,
          use_keras=use_keras,
          use_depthwise=use_depthwise)
      return g.get_collection(tf.compat.v1.GraphKeys.GLOBAL_VARIABLES)
