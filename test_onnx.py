from ultralytics import YOLO

# YOLO model
model = YOLO("yolov8n.onnx")

# Give input image for detection
image = "images.jpg"

# Detect objects in the image
results = model(image)

# detected objects
results[0].show()

# detected image
results[0].save(filename="output.jpg")

print("Object detection completed successfully")