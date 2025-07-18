from flask import Flask, render_template, request
from deepface import DeepFace
import os
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    result = DeepFace.analyze(img_path=file_path, actions=['emotion'], enforce_detection=False)
    emotion = result[0]['dominant_emotion']

    return render_template('result.html', emotion=emotion, image_path=file.filename)


if __name__ == '__main__':
    app.run(debug = True)