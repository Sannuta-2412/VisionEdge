# VisionEdge - AI Object Detection Module

## Overview

This module is part of the VisionEdge project. It performs real-time object detection using YOLOv8 and OpenCV through a live webcam.

## Features

- Real-time object detection
- Live webcam detection
- Custom colored bounding boxes
- Object labels with confidence score
- FPS (Frames Per Second) counter
- Total object counter
- Individual object counting
- Confidence threshold filtering
- Custom information panel
- Optimized for Apple Silicon (MPS)

## Technologies Used

- Python
- YOLOv8
- OpenCV
- PyTorch
- Ultralytics
- NumPy

## Folder Structure

```
VisionEdge/
│
├── scripts/
│   └── webcam_detect.py
│
├── yolov8n.pt
├── README.md
```

## How to Run

Install dependencies:

```bash
pip install ultralytics opencv-python torch
```

Run:

```bash
python3 scripts/webcam_detect.py
```

## Current Output

- Live webcam feed
- Real-time object detection
- Custom bounding boxes
- Confidence scores
- FPS counter
- Total detected objects
- Object count by category

## Future Enhancements

- Screenshot capture
- Video recording
- Detection history
- Session statistics
- Detection alerts

## Author

**Sannuta**

B.Tech – Computer Science Engineering (AI & ML)

Dayananda Sagar Universitys