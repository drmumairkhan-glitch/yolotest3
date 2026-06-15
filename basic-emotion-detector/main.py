import cv2
import time
from deepface import DeepFace

# Open the laptoppp webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam. Try changing VideoCapture(0) to VideoCapture(1).")
    exit()

# Variables to track state
frame_count = 0          # counts every frame we read
emotion = "unknown"      # stores the last detected emotion
prev_time = time.time()  # used to calculate FPS

print("Webcam started. Press Q to quit.")

# Main loop - keep reading frames until we press Q
while True:
    ret, frame = cap.read()

    # If frame could not be read, stop the loop
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    frame_count += 1

    # Only run DeepFace every 15 frames to keep the app fast
    if frame_count % 15 == 0:
        try:
            # Analyze the current frame for emotion
            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False,  # don't crash if no face is found
                detector_backend="opencv",
                silent=True              # suppress console output from DeepFace
            )
            # result is a list; get the dominant emotion from the first face
            emotion = result[0]["dominant_emotion"]
        except Exception:
            # If DeepFace fails for any reason, show "unknown"
            emotion = "unknown"

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time + 1e-9)  # 1e-9 prevents division by zero
    prev_time = current_time

    # Draw emotion text on the frame
    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 50),                    # position: 20px from left, 50px from top
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,                         # font size
        (255, 255, 255),             # white color
        2                            # thickness
    )

    # Draw FPS counter
    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (200, 200, 200),
        2
    )

    # Draw quit instruction
    cv2.putText(
        frame,
        "Press Q to quit",
        (20, frame.shape[0] - 20),   # near the bottom of the window
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (180, 180, 180),
        2
    )

    # Show the frame in a window
    cv2.imshow("Webcam Emotion Detector", frame)

    # Wait 1ms for a key press; break the loop if Q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
print("App closed.")
