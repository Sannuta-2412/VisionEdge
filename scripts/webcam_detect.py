import cv2
import time
from datetime import datetime
from collections import Counter
from ultralytics import YOLO

# -----------------------------------
# Load YOLO Model
# -----------------------------------
model = YOLO("../yolov8s.pt")

CONFIDENCE_THRESHOLD = 0.50

# Objects we want to display
ALLOWED_CLASSES = {
    "person",
    "car",
    "bus",
    "truck",
    "bicycle",
    "motorcycle",
    "laptop",
    "bottle",
    "cell phone"
}

# -----------------------------------
# Open Webcam
# -----------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

prev_frame_time = 0

print("===================================")
print(" VisionEdge AI Started")
print(" Press Q to Quit")
print("===================================")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO
    results = model(
        frame,
        device="mps",
        conf=CONFIDENCE_THRESHOLD,
        verbose=False
    )

    result = results[0]

    annotated_frame = frame.copy()

    object_counter = Counter()

    # -----------------------------
    # Draw Custom Boxes
    # -----------------------------
    for box in result.boxes:

        confidence = float(box.conf[0])

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        if class_name not in ALLOWED_CLASSES:
            continue

        object_counter[class_name] += 1

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Different colours
        if class_name == "person":
            color = (0,255,0)

        elif class_name == "car":
            color = (0,255,255)

        elif class_name == "bus":
            color = (255,0,255)

        elif class_name == "truck":
            color = (255,255,0)

        elif class_name == "bottle":
            color = (255,0,0)

        elif class_name == "laptop":
            color = (0,165,255)

        elif class_name == "cell phone":
            color = (128,0,255)

        elif class_name == "bicycle":
            color = (255,255,255)

        else:
            color = (180,180,180)

        cv2.rectangle(
            annotated_frame,
            (x1,y1),
            (x2,y2),
            color,
            2
        )

        label = f"{class_name} {confidence:.2f}"

        cv2.putText(
            annotated_frame,
            label,
            (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

       # -----------------------------
    # FPS & Inference Time
    # -----------------------------
    current_time = time.time()

    if prev_frame_time == 0:
        fps = 0
        inference_time = 0
    else:
        inference_time = (current_time - prev_frame_time) * 1000
        fps = 1 / (current_time - prev_frame_time)

    prev_frame_time = current_time

    total_objects = sum(object_counter.values())

    # -----------------------------
    # Information Panel
    # -----------------------------
    cv2.rectangle(
        annotated_frame,
        (5, 5),
        (320, 230),
        (30, 30, 30),
        -1
    )

    y = 30

    cv2.putText(
        annotated_frame,
        "VISIONEDGE",
        (15, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    y += 35

    cv2.putText(
        annotated_frame,
        f"FPS : {int(fps)}",
        (15, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 0),
        2
    )

    y += 30

    cv2.putText(
        annotated_frame,
        f"Objects : {total_objects}",
        (15, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 0),
        2
    )

    y += 30

    cv2.putText(
        annotated_frame,
        f"Inference : {inference_time:.1f} ms",
        (15, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (0, 255, 255),
        2
    )

    y += 35

    for name, count in object_counter.items():

        cv2.putText(
            annotated_frame,
            f"{name}: {count}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        y += 25

    # -----------------------------
    # Timestamp
    # -----------------------------
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cv2.putText(
        annotated_frame,
        timestamp,
        (10, annotated_frame.shape[0] - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 255),
        2
    )

    # -----------------------------
    # Display
    # -----------------------------
    cv2.imshow(
        "VisionEdge - AI Powered Real-Time Object Detection",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
print("\nStopping VisionEdge...")

cap.release()

cv2.destroyAllWindows()

print("Resources Released Successfully.")