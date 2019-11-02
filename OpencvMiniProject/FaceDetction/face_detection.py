import cv2
import time

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

custom_img = cv2.imread('twitch.png', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    cv2.line(frame, (0,150), (1600, 150), (185, 128, 41), 10)

    cv2.putText(frame, 'BlaBlaBla', (100, 130), font, 1,
                (255, 255, 255), 2)



    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 2)
        cv2.circle(frame, (x+56, y+82), 30, (185, 185, 185), 2)
        cv2.circle(frame, (x+136, y+82), 30, (185, 185, 185), 2)
        cv2.line(frame, (x+88, y+86), (x+98, y+82), (185, 185, 185), 3)
        cv2.line(frame, (x + 98, y + 82), (x + 108, y + 86), (185, 185, 185), 3)
        cv2.imwrite('twitch.png',frame)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

video_capture.release()
cv2.destroyAllWindows()