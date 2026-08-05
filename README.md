# VisionEdge - AI Object Detection Module

## Overview

This module is part of the VisionEdge project. It performs real-time object detection using **YOLOv8s**, **PyTorch**, and **OpenCV** through a live webcam. The model is also exported to **ONNX** for deployment and optimization.

---

## Features

- Real-time object detection
- Live webcam detection
- YOLOv8s object detection
- Custom colored bounding boxes
- Object labels with confidence score
- FPS (Frames Per Second) counter
- Total object counter
- Individual object counting
- Confidence threshold filtering
- Custom information panel
- Optimized for Apple Silicon (MPS)

---

## Technologies Used

- Python
- YOLOv8s
- PyTorch
- OpenCV
- ONNX
- Ultralytics
- NumPy

---

## Folder Structure

```text
VisionEdge/
│
├── scripts/
│   ├── webcam_detect.py
│   ├── export_onnx.py
│   └── test_yolo.py
│
├── yolov8s.pt
├── yolov8s.onnx
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How to Run

### Install Dependencies

```bash
pip install ultralytics opencv-python torch onnx
```

### Run Real-Time Detection

```bash
python3 scripts/webcam_detect.py
```

### Export Model to ONNX

```bash
python3 scripts/export_onnx.py
```

---

## Current Output

- Live webcam feed
- Real-time object detection
- Custom colored bounding boxes
- Confidence score display
- FPS monitoring
- Total detected objects
- Individual object count
- YOLOv8s model
- ONNX exported model

---

## Future Enhancements

- TensorRT engine optimization
- CuPy zero-copy pipeline
- Screenshot capture
- Video recording
- Detection history
- Session statistics
- Detection alerts

---

## Author

**Sannuta**

B.Tech – Computer Science Engineering (AI & ML)

Dayananda Sagar University