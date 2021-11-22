import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)

    imagem = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if ret:
        cv2.imshow("Imagem HSV", imagem)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
