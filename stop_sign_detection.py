import cv2
import time
from datetime import datetime

# Load Haar Cascade classifier for stop sign detection
cascade_path = "haarcascade_stop_sign.xml"
stop_cascade = cv2.CascadeClassifier(cascade_path)

# Initialize video capture (webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Variables to manage stop signal timing and state
last_detection_time = 0          # Timestamp of last detected stop sign
stop_signal_duration = 3         # Duration (in seconds) to send 'stop' signal after detection
sending_stop = False             # Whether currently sending the stop signal

print("[INFO] Press 'q' to quit the program.")

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect stop signs in the grayscale frame
    stops = stop_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Get current time for timing and logging
    current_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # If any stop signs detected:
    if len(stops) > 0:
        # Draw red rectangles around detected stop signs
        for (x, y, w, h) in stops:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # If not already sending stop signal, start now and record the time
        if not sending_stop:
            last_detection_time = current_time
            sending_stop = True
            print(f"{timestamp} - Sending 1 to Arduino")

    # Check if the stop signal duration has elapsed; if so, stop sending '1'
    if sending_stop and (current_time - last_detection_time) >= stop_signal_duration:
        sending_stop = False
        print(f"{timestamp} - Sending 0 to Arduino")

    # If not sending stop signal and no stop sign detected, keep sending '0'
    if not sending_stop and len(stops) == 0:
        print(f"{timestamp} - Sending 0 to Arduino")

    # Display the video frame with detections
    cv2.imshow("Stop Sign Detection", frame)

    # Listen for keypress; if 'q' is pressed, exit the loop and end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] 'q' pressed. Exiting program.")
        break

# Release the webcam and close windows properly
cap.release()
cv2.destroyAllWindows()
