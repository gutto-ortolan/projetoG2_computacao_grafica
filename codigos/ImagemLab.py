import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)

    labImage = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    if ret:
        cv2.imshow("Imagem Lab", labImage)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
