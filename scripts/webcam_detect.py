import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("../yolov8n.pt")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame, device="mps")

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Show the result
    cv2.imshow("VisionEdge - YOLO Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
