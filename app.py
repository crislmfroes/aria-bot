from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
import argparse
from utils.classifier import ImageClassifier
import tensorflow as tf

tf.enable_eager_execution()

classifier = ImageClassifier()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads/'

parser = argparse.ArgumentParser()
parser.add_argument('development', type=bool, nargs='?', const=False)

extensions = ['jpg', 'png', 'jpeg']

def valida_file(file_name):
    return '.' in file_name and file_name.split('.')[1].lower() in extensions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    file_form = request.files['image-input']
    if file_form and valida_file(file_form.filename):
        classifications = classifier.classify(file_form)
        return render_template('class_results.html', scores=classifications)
    return ''

def main():
    args = parser.parse_args()
    development = args.development
    if development:
        app.env = 'development'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=development, port=port)

if __name__ == '__main__':
    main()