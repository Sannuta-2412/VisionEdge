from ultralytics import YOLO
import time

# Load the model
model = YOLO("yolov8n.pt")

# Start timer
start_time = time.time()

# Run detection on the sample image
results = model.predict(
    source="bus.jpg",
    device="mps",
    save=True
)

# End timer
end_time = time.time()

# Calculate FPS
inference_time = end_time - start_time
fps = 1 / inference_time

print("✅ Detection completed!")
print(f"⏱ Inference Time: {inference_time:.3f} seconds")
print(f"🚀 Approximate FPS: {fps:.2f}")