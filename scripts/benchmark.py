import time
import cv2
import psutil
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.onnx", task="detect")

# Load image
image = cv2.imread("car.jpg")

# Get RAM before testing
process = psutil.Process()
ram_before = process.memory_info().rss / (1024 * 1024)

print("RAM Before Test:", round(ram_before, 2), "MB")


# Run inference 50 times
for i in range(50):
    results = model(image)

    if (i + 1) % 10 == 0:
        ram_now = process.memory_info().rss / (1024 * 1024)
        print(
            "Run:", i + 1,
            "RAM:",
            round(ram_now, 2),
            "MB"
        )


# RAM after test
ram_after = process.memory_info().rss / (1024 * 1024)

print("RAM After Test:", round(ram_after, 2), "MB")
print("RAM Increase:", round(ram_after - ram_before, 2), "MB")