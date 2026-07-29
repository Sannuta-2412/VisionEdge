from ultralytics import YOLO

# Load the model
model = YOLO("yolov8n.pt")

# Run detection on the sample image
results = model.predict(
    source="bus.jpg",
    device="mps",
    save=True
)

print("✅ Detection completed!")