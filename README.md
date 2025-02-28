# Echo Hands

**Echo Hands** is an American Sign Language (ASL) interpreter that uses computer vision and machine learning to recognize hand gestures and convert them into text. This project leverages **MediaPipe**, **OpenCV**, and a trained machine learning model for real-time gesture recognition.

## 🚀 Features
- Real-time hand gesture detection using **MediaPipe**.
- Recognizes various ASL signs and translates them into text.
- Uses a **pre-trained machine learning model** for accurate predictions.
- Displays detected gestures with bounding boxes and labels on the video feed.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-Learn (pre-trained model using `pickle`)
- **Computer Vision:** OpenCV, MediaPipe
- **Frameworks:** Flask (if deploying as a web API)
- **Deployment (Optional):** Docker, AWS/GCP

## 📌 Installation
### 1️⃣ Prerequisites
Make sure you have **Python 3.8+** installed. Then install the required dependencies:
```bash
pip install opencv-python mediapipe numpy pickle-mixin
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/echo-hands.git
cd echo-hands
```

### 3️⃣ Run the ASL Interpreter
```bash
python3 inference_classifier.py
```
This will open your webcam and start detecting ASL gestures.

## 🎯 Usage
- Run the script and **show ASL gestures** to the camera.
- The model detects and **displays the corresponding letter/word**.
- Press **'q'** to exit the program.

## 🛠️ Model Training (Optional)
If you want to train your own model:
1. Collect ASL hand gesture images.
2. Extract landmarks using **MediaPipe**.
3. Train an **ML model** (e.g., SVM, Decision Tree) using **Scikit-Learn**.
4. Save the model using `pickle`.

## 🔥 Future Improvements
- Improve accuracy with **Deep Learning (TensorFlow/PyTorch)**.
- Add **real-time speech synthesis** for detected signs.
- Extend to more complex ASL sentences.

## 🤝 Contributing
Want to contribute? Feel free to **fork the repo and submit a pull request**!

---
Made with ❤️ by the Echo Hands Team 🚀

