from flask import Flask
from flask import render_template, redirect
from flask import request

import numpy as np
import base64
from PIL import Image
from random import seed
from random import randint
import matplotlib.pyplot as pyplot
import scipy.misc
from final import guessIMG


app = Flask(__name__)

seed(1)


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, -1)).astype(np.uint8)


def convert_and_save(b64_string):
    with open("./static/temp.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

    im = Image.open("./static/temp.png")
    im_np = load_image_into_numpy_array(im)
    image_without_alpha = im_np[:, :, :3]
    im = Image.fromarray(image_without_alpha)
    print(image_without_alpha.shape)
    im.save("./static/temp.png")


def aiGuessNow():
    if 'AIguess' not in globals():
        return 'none'
    else:
        return AIguess


def aiNot():
    if 'AIguess' not in globals():
        return False
    else:
        return True


@app.route('/')
def play_page():
    return render_template('index.html')


@app.route('/draw')
def draw():
    global words
    words = ['lion', 'mushroom', 'apple', 'starfish', 'hamburger']
    global num
    num = randint(0, 4)
    return render_template('draw.html', word=words[num])


@app.route('/guess')
def guess():
    full_filename = "./static/temp.png"
    if aiGuessNow() == words[num]:
        return render_template('lose.html')
    else:
        return render_template("guess.html", user_image=full_filename, ai=aiGuessNow())


@app.route('/send', methods=["POST"])
def get_image():
    image_b64 = request.values['imageBase64']
    convert_and_save(image_b64)
    global AIguess
    AIguess = guessIMG("./static/temp.png")
    print(AIguess)
    return ''


@app.route('/get', methods=["POST"])
def send_image():
    text = request.form['text']
    processed_text = text.lower()

    if processed_text == words[num]:
        return render_template('victory.html')
    else:
        return redirect('./guess')


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
