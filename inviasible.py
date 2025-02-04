import cv2
import numpy as np

# Load the video
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

# Capture the background (first frame assumed as static background)
ret, background = cap.read()
if ret:
    background = cv2.GaussianBlur(background, (21, 21), 0)

# Define output path
output_path = "invisible_effect.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS) / 2)  # Reduce FPS for efficiency
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2)
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Process each frame with downscaling
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing
    frame = cv2.resize(frame, (frame_width, frame_height))
    background_resized = cv2.resize(background, (frame_width, frame_height))

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for the blanket (assuming red)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create mask
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Apply morphological operations
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))

    # Create inverse mask
    inverse_mask = cv2.bitwise_not(mask)

    # Replace blanket area with background
    background_part = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    frame_part = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    output_frame = cv2.addWeighted(background_part, 1, frame_part, 1, 0)

    # Write to output video
    out.write(output_frame)

# Release resources
cap.release()
out.release()

print(f"Processed video saved as {output_path}")
