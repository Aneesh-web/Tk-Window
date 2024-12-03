import cv2

# Load the image
image_path = 'download (1).jpeg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    print("Image loaded successfully!")
else:
    print("Error: Image could not be loaded.")

# Display the image (optional)
cv2.imshow('Loaded Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
