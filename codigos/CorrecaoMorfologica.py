import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    binarizationObject = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ImagemGaussianBlur = cv2.GaussianBlur(binarizationObject, (7, 7), 0)
    _, ImagemThrehold = cv2.threshold(
        ImagemGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV
    )
    ImagemAdaptive = cv2.adaptiveThreshold(
        ImagemGaussianBlur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        10,
    )

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(ImagemAdaptive, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(ImagemAdaptive, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)

    if ret:
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
