import cv2
import codecs
from datetime import datetime

camera = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("xmls/haarcascade_frontalface_alt.xml")

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect = cascade.detectMultiScale(frameGray, 1.1, 5)
    for (x, y, w, h) in detect:

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        logs = codecs.open("logs/logsReconhecimentoFace.txt", "a+", "UTF-8")
        logs.write("Face detectada " + date + "\n")

    if ret:
        cv2.imshow("Reconhecimento Face", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()
camera.release()
