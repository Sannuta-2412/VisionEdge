# VisionEdge

AI/ML Computer Vision Project

## Development Branch

Sathish-setup-testing




# Week 1 – Project Setup

## Setup Completed

- Created VisionEdge project structure.
- Created Python virtual environment.
- Installed required Python packages.
- Configured Git and GitHub.
- All project work is maintained on the `Sathish-setup-testing` branch.
- Verified the project setup using `src/main.py`.

## Setup Output

VisionEdge project setup successful




# Week 2 – YOLOv8 ONNX Model Export and Testing
## Completed Tasks

- Installed YOLOv8 using Ultralytics.
- Downloaded YOLOv8n pretrained model.
- Exported YOLOv8n PyTorch model to ONNX format.
- Tested ONNX model using ONNX Runtime.
- Verified object detection using test images.

## Model Information


Model: YOLOv8n
Format: ONNX
Runtime: ONNX Runtime 1.28.0
Execution Provider: CPUExecutionProvider

## Detection Result

Test Image: car.jpg
Detection: 1 car detected
Status: Successful





# Week 3 – ONNX Inference Pipeline

## Completed Tasks

✓ Created inference testing scripts
✓ Loaded YOLOv8 ONNX model
✓ Tested object detection pipeline
✓ Verified preprocessing
✓ Verified inference
✓ Verified postprocessing
✓ Generated detection results


## Inference Pipeline

Input Image

      ↓

YOLOv8 ONNX Model

      ↓

ONNX Runtime CPU Inference

      ↓

Detection Output




# Week 4 – ONNX Benchmark and Stability Testing
## YOLOv8 ONNX Benchmark Test

Model:
YOLOv8n ONNX

Runtime:
ONNX Runtime 1.28.0

Execution Provider:
CPUExecutionProvider

Input Resolution:
640x640

Test Image:
car.jpg

## Performance Results

Average Inference Time : 59.65 ms

FPS : 16.76

Detection : 1 car

## Memory Leak / Stability Test

Test Runs:
50 inference cycles

Initial RAM Usage:
238.87 MB

Final RAM Usage:
423.14 MB

RAM Increase:
184.27 MB

## Observation

The YOLOv8 ONNX model successfully performed object detection using ONNX Runtime CPU inference.
Memory usage increased during model initialization and remained stable during repeated inference runs.
No continuous memory growth was observed.

# Project Status

Week 1  - Project Setup                 ✅ Completed

Week 2  - YOLOv8 ONNX Testing          ✅ Completed

Week 3  - ONNX Inference Pipeline      ✅ Completed

Week 4  - Benchmark & Stability Test   ✅ Completed
