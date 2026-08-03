import cv2
from ultralytics import YOLO

print("1. Loading model...")
model = YOLO("yolov8n.onnx", task="detect")
print("2. Model loaded")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

print("3. Webcam opened")

while True:
    success, frame = cap.read()

    if not success:
        print("Error: Cannot read frame")
        break

    print("4. Frame captured")

    # Run YOLO detection
    results = model(frame, verbose=False)

    print("5. Detection completed")
    print(results[0].boxes)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Show the result
    cv2.imshow("VisionEdge Webcam", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()