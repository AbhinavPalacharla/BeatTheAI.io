import xml.etree.cElementTree as et
import os


pathh = 'Path to dataset'

files = []
for r, d, f in os.walk(pathh):
    for file in f:
        files.append(file)

for i in range(len(files)):
    if "n02129165" in files[i]:
        annotation = et.Element("annotation")

        folder = et.SubElement(annotation, "folder").text = "test"

        filename = et.SubElement(annotation, "filename").text = files[i]

        path = et.SubElement(annotation, "path").text = os.path.join("./", files[i])

        source = et.SubElement(annotation, "source")
        db = et.SubElement(source, "database").text = "Unknown"

        size = et.SubElement(annotation, "size")
        width = et.SubElement(size, "width").text = "256"
        height = et.SubElement(size, "height").text = "256"
        depth = et.SubElement(size, "depth").text = "1"

        segmented = et.SubElement(annotation, "segmented").text = "0"

        obj = et.SubElement(annotation, "object")
        name = et.SubElement(obj, "name").text = "lion"
        pose = et.SubElement(obj, "pose").text = "Unspecified"
        truncated = et.SubElement(obj, "truncated").text = "0"
        difficult = et.SubElement(obj, "difficult").text = "0"
        bndbox = et.SubElement(obj, "bndbox")
        xmin = et.SubElement(bndbox, "xmin").text = "1"
        ymin = et.SubElement(bndbox, "ymin").text = "1"
        xmax = et.SubElement(bndbox, "xmax").text = "255"
        ymax = et.SubElement(bndbox, "ymax").text = "255"
        tree = et.ElementTree(annotation)
        tree.write("Path to dataset/n{}.xml".format(files[i].strip('.png')))
    elif "n07739125" in files[i]:
        annotation = et.Element("annotation")

        folder = et.SubElement(annotation, "folder").text = "test"

        filename = et.SubElement(annotation, "filename").text = files[i]

        path = et.SubElement(annotation, "path").text = os.path.join("./", files[i])

        source = et.SubElement(annotation, "source")
        db = et.SubElement(source, "database").text = "Unknown"

        size = et.SubElement(annotation, "size")
        width = et.SubElement(size, "width").text = "256"
        height = et.SubElement(size, "height").text = "256"
        depth = et.SubElement(size, "depth").text = "1"

        segmented = et.SubElement(annotation, "segmented").text = "0"

        obj = et.SubElement(annotation, "object")
        name = et.SubElement(obj, "name").text = "apple"
        pose = et.SubElement(obj, "pose").text = "Unspecified"
        truncated = et.SubElement(obj, "truncated").text = "0"
        difficult = et.SubElement(obj, "difficult").text = "0"
        bndbox = et.SubElement(obj, "bndbox")
        xmin = et.SubElement(bndbox, "xmin").text = "1"
        ymin = et.SubElement(bndbox, "ymin").text = "1"
        xmax = et.SubElement(bndbox, "xmax").text = "255"
        ymax = et.SubElement(bndbox, "ymax").text = "255"
        tree = et.ElementTree(annotation)
        tree.write("Path to dataset/n{}.xml".format(files[i].strip('.png')))
    elif "n07697313" in files[i]:
        print(files[i])
        annotation = et.Element("annotation")

        folder = et.SubElement(annotation, "folder").text = "test"

        filename = et.SubElement(annotation, "filename").text = files[i]

        path = et.SubElement(annotation, "path").text = os.path.join("./", files[i])

        source = et.SubElement(annotation, "source")
        db = et.SubElement(source, "database").text = "Unknown"

        size = et.SubElement(annotation, "size")
        width = et.SubElement(size, "width").text = "256"
        height = et.SubElement(size, "height").text = "256"
        depth = et.SubElement(size, "depth").text = "1"

        segmented = et.SubElement(annotation, "segmented").text = "0"

        obj = et.SubElement(annotation, "object")
        name = et.SubElement(obj, "name").text = "hamburger"
        pose = et.SubElement(obj, "pose").text = "Unspecified"
        truncated = et.SubElement(obj, "truncated").text = "0"
        difficult = et.SubElement(obj, "difficult").text = "0"
        bndbox = et.SubElement(obj, "bndbox")
        xmin = et.SubElement(bndbox, "xmin").text = "1"
        ymin = et.SubElement(bndbox, "ymin").text = "1"
        xmax = et.SubElement(bndbox, "xmax").text = "255"
        ymax = et.SubElement(bndbox, "ymax").text = "255"
        tree = et.ElementTree(annotation)
        tree.write("Path to dataset/n{}.xml".format(files[i].strip('.png')))
    elif "n12997919" in files[i]:
        annotation = et.Element("annotation")

        folder = et.SubElement(annotation, "folder").text = "test"

        filename = et.SubElement(annotation, "filename").text = files[i]

        path = et.SubElement(annotation, "path").text = os.path.join("./", files[i])

        source = et.SubElement(annotation, "source")
        db = et.SubElement(source, "database").text = "Unknown"

        size = et.SubElement(annotation, "size")
        width = et.SubElement(size, "width").text = "256"
        height = et.SubElement(size, "height").text = "256"
        depth = et.SubElement(size, "depth").text = "1"

        segmented = et.SubElement(annotation, "segmented").text = "0"

        obj = et.SubElement(annotation, "object")
        name = et.SubElement(obj, "name").text = "mushroom"
        pose = et.SubElement(obj, "pose").text = "Unspecified"
        truncated = et.SubElement(obj, "truncated").text = "0"
        difficult = et.SubElement(obj, "difficult").text = "0"
        bndbox = et.SubElement(obj, "bndbox")
        xmin = et.SubElement(bndbox, "xmin").text = "1"
        ymin = et.SubElement(bndbox, "ymin").text = "1"
        xmax = et.SubElement(bndbox, "xmax").text = "255"
        ymax = et.SubElement(bndbox, "ymax").text = "255"
        tree = et.ElementTree(annotation)
        tree.write("Path to dataset/n{}.xml".format(files[i].strip('.png')))
    elif "n02317335" in files[i]:
        annotation = et.Element("annotation")

        folder = et.SubElement(annotation, "folder").text = "test"

        filename = et.SubElement(annotation, "filename").text = files[i]

        path = et.SubElement(annotation, "path").text = os.path.join("./", files[i])

        source = et.SubElement(annotation, "source")
        db = et.SubElement(source, "database").text = "Unknown"

        size = et.SubElement(annotation, "size")
        width = et.SubElement(size, "width").text = "256"
        height = et.SubElement(size, "height").text = "256"
        depth = et.SubElement(size, "depth").text = "1"

        segmented = et.SubElement(annotation, "segmented").text = "0"

        obj = et.SubElement(annotation, "object")
        name = et.SubElement(obj, "name").text = "starfish"
        pose = et.SubElement(obj, "pose").text = "Unspecified"
        truncated = et.SubElement(obj, "truncated").text = "0"
        difficult = et.SubElement(obj, "difficult").text = "0"
        bndbox = et.SubElement(obj, "bndbox")
        xmin = et.SubElement(bndbox, "xmin").text = "1"
        ymin = et.SubElement(bndbox, "ymin").text = "1"
        xmax = et.SubElement(bndbox, "xmax").text = "255"
        ymax = et.SubElement(bndbox, "ymax").text = "255"
        tree = et.ElementTree(annotation)
        tree.write("Path to dataset/n{}.xml".format(files[i].strip('.png')))
    else:
        continue
