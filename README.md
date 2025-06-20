# Stop Sign Detection and UART Integration

## 🧠 Project Description
A real-time system using OpenCV and Python to detect stop signs via webcam. When a stop sign is detected, the system sends a `1` over UART to the microcontroller for 3 seconds, then resumes sending `0`.

## 📁 Contents
- `stop_sign_detection.py` - Main script
- `haarcascade_stop_sign.xml` - Classifier
- `README.md` - This file

## 🔧 Requirements
- Python 3
- OpenCV
- pyserial

## 💻 Installation
```bash
pip install opencv-python pyserial
```

## 🧪 Testing Instructions
1. Connect your Arduino via USB and identify its COM port (e.g., COM3).
2. Replace `'COM3'` in `stop_sign_detection.py` with your actual port.
3. Run the script:
```bash
python stop_sign_detection.py
```
4. Show a printed stop sign image to the webcam and observe output on Arduino (LED or Serial Monitor).

## 📤 Submission
1. Zip this folder.
2. Submit using this link: https://forms.gle/mizRDEfJrehDVRXu5
