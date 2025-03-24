import cv2

image= cv2.imread('mario.png')


if image is None:
    print("Error: Could not read image file")
    exit()

    scale_percent = 50
    width=int(image.shape[1])
    height=int(image.shape[1] * scale_percent /100)
    resized = cv2.resize(image, (width, height))

    

    rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)


    gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', image)
    cv2.imshow('Resized', resized)
    cv2.imshow('Rotated', rotated)
    cv2.imshow('Grayscale', gray)

    cv2.waitKey(0)
cv2.destroyAllWindows()
