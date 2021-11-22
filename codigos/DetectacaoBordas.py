import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    imagem = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    imageGaussianBlur = cv2.GaussianBlur(imagem, (7, 7), 0)
    _, imageThrehold = cv2.threshold(imageGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV)
    imageAdaptive = cv2.adaptiveThreshold(
        imageGaussianBlur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        10,
    )

    imageSobelEixoX = cv2.Sobel(imageGaussianBlur, cv2.CV_64F, 1, 0)
    imageSobelEixoY = cv2.Sobel(imageGaussianBlur, cv2.CV_64F, 0, 1)
    imageSobelEixoX = np.uint8(np.absolute(imageSobelEixoX))
    imageSobelEixoY = np.uint8(np.absolute(imageSobelEixoY))
    imageSobel = cv2.bitwise_or(imageSobelEixoX, imageSobelEixoY)

    imageUnitedSobel = np.vstack(
        [
            np.hstack([imagem, imageSobelEixoX]),
            np.hstack([imageSobelEixoY, imageSobel]),
        ]
    )

    if ret:
        cv2.imshow("Sobel", imageUnitedSobel)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
