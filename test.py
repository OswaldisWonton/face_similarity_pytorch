import cv2
import time

def display_camera_then_video(camera_index, video_path, switch_time=5):
    # Initialize the window
    cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE)
    
    # Start capturing camera feed
    cap = cv2.VideoCapture(camera_index)
    start_time = time.time()

    # Display camera feed until the switch time is reached
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Display", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if (time.time() - start_time) > switch_time:
            break
    
    # Switch to video file without closing the window or releasing the capture
    cap.release()  # Release the camera

    # Start video playback
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Display", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

# Usage
camera_index = 0  # Usually 0 for the default camera
video_path = 'input/19609-303404131_small.mp4'
display_camera_then_video(camera_index, video_path)