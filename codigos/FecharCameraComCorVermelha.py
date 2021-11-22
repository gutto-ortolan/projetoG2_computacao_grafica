import cv2
import numpy as np
import time

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    vermelhoLower = np.array([161, 155, 84], np.uint8)
    vermelhoUpper = np.array([179, 255, 255], np.uint8)
    mascara = cv2.inRange(hsv_frame, vermelhoLower, vermelhoUpper)
    result = cv2.bitwise_and(frame, frame, mask=mascara)
    frame_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(frame_gray, 3, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:

        areaContorno = cv2.contourArea(contorno)

        if areaContorno > 1000:
            time.sleep(5)
            cv2.destroyAllWindows()
            camera.release()

        cv2.imshow("Camera", frame)

    if ret:
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
