from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8s.pt")

# Export to ONNX
model.export(format="onnx")

print("YOLO model exported to ONNX successfully!")