# VisionEdge - AI Object Detection Module

## Overview
VisionEdge is an AI-powered real-time object detection project developed using Python, OpenCV, and YOLOv8. The application detects objects from a live webcam feed and displays bounding boxes with class labels in real time.

## Features
- Real-time object detection
- Live webcam integration
- YOLOv8 pretrained model
- ONNX model export
- Bounding box visualization

## Technologies Used
- Python
- OpenCV
- Ultralytics YOLOv8
- ONNX

## Project Structure
```
VisionEdge/
├── scripts/
│   ├── webcam_detect.py
│   ├── test_yolo.py
│   └── export_onnx.py
├── yolov8n.pt
├── yolov8n.onnx
├── README.md
```

## How to Run

Install dependencies:

```bash
pip install ultralytics opencv-python torch torchvision numpy
```

Run the application:

```bash
python3 scripts/webcam_detect.py
```

## Future Improvements

- Improve object detection accuracy using a larger model or custom training.
- Add video file support.
- Optimize inference speed.
- Integrate the AI module into the complete VisionEdge application.s