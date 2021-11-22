import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    amareloLower = np.array([23, 59, 119])
    amareloUpper = np.array([54, 255, 255])
    mascara = cv2.inRange(hsv_frame, amareloLower, amareloUpper)
    res = cv2.bitwise_not(frame, frame, mask=mascara)
    rest = cv2.bitwise_and(frame, frame, mask=mascara)
    res[mascara > 0] = (0, 0, 255)

    if ret:
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
