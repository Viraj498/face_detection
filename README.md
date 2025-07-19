# 🎭 Emotion Detection Web App using DeepFace & Flask

This is a simple and effective web-based emotion detection system that uses **DeepFace**, an open-source face recognition and facial attribute analysis framework. Users can upload a photo, and the app will analyze and display the **dominant emotion** detected in the face.

---
# Author - Viraj Developer
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

emotion-detection-app/
├── app.py # Main Flask application
├── templates/
│ ├── index.html # Image upload interface
│ └── result.html # Emotion result view
├── static/
│ └── uploads/ # Uploaded image storage
├── uploads/ # Temporary image storage (created at runtime)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


### Install via pip

```bash
pip install -r requirements.txt

