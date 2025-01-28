import os
import cv2
from datetime import datetime

# Directory containing the images
image_dir = "images"

# Generate a unique output video file name based on the current timestamp
output_video = f"collage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mov"

# Video settings
frame_width = 640
frame_height = 480
fps = 30

def create_video_collage(image_dir, output_video, frame_width, frame_height, fps):
    # Get list of image files in the directory
    image_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No images found in the directory.")
        return

    # Initialize video writer with codec compatible with QuickTime
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

    for file in image_files:
        # Read the image
        img = cv2.imread(file)

        if img is not None:
            # Resize the image to fit the frame
            img_resized = cv2.resize(img, (frame_width, frame_height))

            # Write the same frame multiple times to extend its duration
            for _ in range(fps * 2):  # Display each image for 2 seconds
                out.write(img_resized)
        else:
            print(f"Error loading image: {file}")

    # Release the video writer
    out.release()
    print(f"Video collage saved as {output_video}")

# Create the video collage
create_video_collage(image_dir, output_video, frame_width, frame_height, fps)
