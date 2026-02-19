# ✋ Hand Gesture Recognition System

A real-time **Hand Gesture Recognition** system built using **Python, Computer Vision, and Machine Learning**.
This project detects and classifies hand gestures through a webcam and predicts gestures such as 👍 thumbs up and 👎 thumbs down.

---

## 📌 Project Overview

This system captures hand landmarks using computer vision techniques and trains a machine learning model to recognize different gestures.

It can be used for:

* Human-computer interaction
* Assistive communication
* Touchless control systems
* Sign language basics

---

## 🚀 Features

✅ Real-time hand tracking using webcam
✅ Custom gesture data collection
✅ Machine learning model training
✅ Live gesture prediction
✅ Easy to extend with new gestures

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **MediaPipe**
* **NumPy**
* **Scikit-learn**

---

## 📁 Project Structure

```
Hand-Gesture-Recognition/
│
├── dataset/            # CSV gesture data
├── collect_data.py     # Collect gesture samples
├── train_model.py      # Train ML model
├── predict.py          # Predict gestures in real time
├── hand_test.py        # Test hand detection
├── model.pkl           # Trained model (generated after training)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/sowjanyanu-34/Hand-Gesture-Recognition.git
cd Hand-Gesture-Recognition
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate virtual environment

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 4️⃣ Install dependencies

```
pip install opencv-python mediapipe numpy scikit-learn
```

---

## 📊 How to Use

### ▶️ Step 1: Collect gesture data

```
python collect_data.py
```

Capture samples for each gesture.

---

### ▶️ Step 2: Train the model

```
python train_model.py
```

This creates:

```
model.pkl
```

---

### ▶️ Step 3: Run gesture prediction

```
python predict.py
```

The webcam will open and display predicted gestures.

---

## ➕ Adding New Gestures

1. Collect data for the new gesture
2. Update labels if required
3. Retrain the model
4. Run prediction again

---

## 🎯 Applications

* Sign language assistance
* Gesture-based controls
* Smart home automation
* Interactive gaming
* Accessibility tools

---

## 📸 Demo (Add Screenshot Here)

You can add screenshots or GIFs showing gesture detection.

Example:

```
![Demo](images/demo.png)
```

---

## 👩‍💻 Author

**Sowjanya N U**
Computer Science Engineering Student

---

## ⭐ Future Improvements

* Support more gestures
* Improve accuracy with deep learning
* Deploy as a web app
* Mobile integration

---

## 📜 License

This project is open-source and available for educational use.

---

⭐ If you like this project, give it a star!
