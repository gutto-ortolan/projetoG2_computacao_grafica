import cv2

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)

    imagemRedimensionada = cv2.resize(frame, (360, 200), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Imagem Redimensionada:", imagemRedimensionada)

    if ret:
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
