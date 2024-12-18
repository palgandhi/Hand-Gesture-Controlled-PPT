import cv2 as cv
import time
import handTrackingModule as htm
import pyautogui as pg
import subprocess

# Path to your PowerPoint file
ppt_path = "/Users/palgandhi/Desktop/Coffee-Cultivation-in-India.pptx"

# Open PowerPoint and start the slideshow
try:
    subprocess.call(["open", ppt_path])
    time.sleep(5)  # Give PowerPoint time to open
    pg.hotkey("command", "shift", "s")  # Start the slideshow
except Exception as e:
    print(f"Error opening PowerPoint: {e}")

#Initialize webcam and hand detector
cap = cv.VideoCapture(0)
detection = htm.HandDetector(detectionCon=0.7)

# Store positions (time and X-coordinates)
position_history = []
history_duration = 1  # Duration in seconds for gesture recognition

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hands and find landmarks
    detection.findHands(img)
    landmarks_list = detection.findPosition(img)

    if len(landmarks_list) != 0:
        # Get coordinates of the index finger
        x1, y1 = landmarks_list[8][1], landmarks_list[8][2]
        x2, y2 = landmarks_list[12][1], landmarks_list[12][2]

        # Draw circles on index and middle fingers
        cv.circle(img, (x2, y2), 25, (255, 0, 0), cv.FILLED)
        cv.circle(img, (x1, y1), 15, (255, 0, 0), cv.FILLED)

        # Store the position with timestamp
        current_time = time.time()
        position_history.append((current_time, x1))

        # Remove entries older than history_duration
        position_history = [pos for pos in position_history if current_time - pos[0] <= history_duration]

        # Detect swipe gestures
        if len(position_history) >= 2:
            x_old = position_history[0][1]  # Oldest X-coordinate
            x_new = position_history[-1][1]  # Newest X-coordinate

            if x_new - x_old > 100:  # Right swipe threshold
                pg.press('right')  # Move to next slide
                cv.putText(img, "Next Slide", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
                position_history = []  # Clear history after action

            elif x_old - x_new > 100:  # Left swipe threshold
                pg.press('left')  # Move to previous slide
                cv.putText(img, "Previous Slide", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
                position_history = []  # Clear history after action

    # Show the video feed
    #cv.imshow("Hand Gesture Control", img)
    #if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        #break

#cap.release()
#cv.destroyAllWindows()
