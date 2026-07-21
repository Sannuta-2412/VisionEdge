from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run object detection on an example image
results = model("https://ultralytics.com/images/bus.jpg", save=True)

print("Detection completed successfully!")