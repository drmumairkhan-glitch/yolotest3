# Basic Webcam Emotion Detector

This project uses your laptop webcam and the DeepFace pretrained model to estimate facial expressions in real time — right inside a video window on your screen.

> **Important note:** This app estimates the visible facial expression captured by the camera. It does not know your real inner emotion with 100% accuracy. Results depend on lighting, camera angle, and face visibility.

---

## Requirements

- Python 3.8 or higher
- A working laptop webcam

---

## Setup (Windows PowerShell)

Run these commands one by one inside your project folder:

```powershell
# 1. Go into the project folder
cd basic-emotion-detector

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate the virtual environment
.venv\Scripts\activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt
```

---

## Run

```powershell
python main.py
```

A webcam window will open. Your detected facial expression will be shown on screen, updated every 15 frames.

---

## Controls

| Key | Action     |
|-----|------------|
| Q   | Quit / Exit |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Webcam does not open | Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in `main.py` |
| Import error for DeepFace | Make sure `.venv` is activated before running `pip install` |
| File named `deepface.py` exists | Rename it — it conflicts with the DeepFace package import |
| First run is very slow | DeepFace downloads model weights on the first run; wait for it to finish |
| App feels slow or laggy | Increase the frame interval: change `15` to `25` in `main.py` |
| VS Code uses wrong Python | Press `Ctrl+Shift+P` → "Python: Select Interpreter" → choose `.venv` |
| TensorFlow / Keras error | Run `pip install tf-keras` inside the activated `.venv` |
