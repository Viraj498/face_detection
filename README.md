# 🎭 Emotion Detection Web App using DeepFace & Flask

This is a simple and effective web-based emotion detection system that uses **DeepFace**, an open-source face recognition and facial attribute analysis framework. Users can upload a photo, and the app will analyze and display the **dominant emotion** detected in the face.

---
# Author - Viraj Devkar
## 🔍 About the Project

This project demonstrates how to integrate Deep Learning into a Flask web app. It uses **DeepFace** to detect and classify human emotions based on facial expressions in images. Ideal for beginners interested in AI, face analysis, or web app development.

---

## 🚀 Features

- Upload a face image and analyze emotion
- Emotion detection powered by DeepFace
- Simple Flask-based UI
- Displays:
  - Dominant emotion
  - Uploaded image preview

---

## 📁 Project Structure :

face_detection/
├── app.py # Main Flask application
├── templates/
│ ├── index.html # Image upload interface
│ └── result.html # Emotion result view
├── static/
│ └── uploads/ # Uploaded image storage
├── uploads/ # Temporary image storage (created at runtime)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## ⚙️ Setup Instructions

## Clone the Repository
git clone https://github.com/yourusername/face_detection.git
cd face_detection

## Install Dependencies
pip install -r requirements.txt
Create Upload Folder (if not auto-created)

## Create Upload Folder (if not auto-created)
mkdir uploads

## Run the Flask App
python app.py

## Visit in Browser
http://127.0.0.1:5000
