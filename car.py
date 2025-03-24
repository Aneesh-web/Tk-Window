import cv2

# Load the Haar cascade for car detection
car_cascade = cv2.CascadeClassifier('cars.xml')  # Use correct path if needed

# Load video
cap = cv2.VideoCapture('car.mp4')  # <- Change this path

# Check if video loaded
if not cap.isOpened():
    print(" Error: Could not open video file.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print(" End of video or cannot read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Car Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
