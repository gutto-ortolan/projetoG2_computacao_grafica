import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    binarizacao = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imagemGaussianBlur = cv2.GaussianBlur(binarizacao, (7, 7), 0)
    _, imagemThrehold = cv2.threshold(
        imagemGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV
    )

    imagemAdaptive = cv2.adaptiveThreshold(
        imagemGaussianBlur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        10,
    )

    imagem = np.vstack([np.hstack([imagemThrehold, imagemAdaptive])])
    cv2.imshow("Camera Binarizada", imagem)

    if ret:
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
