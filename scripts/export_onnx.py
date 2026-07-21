from ultralytics import YOLO

# Load the pretrained model
model = YOLO("yolov8n.pt")

# Export to ONNX
model.export(format="onnx")

print("Model exported to ONNX successfully!")
