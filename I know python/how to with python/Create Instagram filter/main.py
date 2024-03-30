import random,cv2,time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")

video = cv2.VideoCapture(0)

num = 0

def smile_meter(frame, x1, y1):
    global num
    if num > 100:
        x = str(random.randint(0,100))
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255,0,255)
        text = cv2.putText(frame, "your smile is", (int(x1)+15, int(y1)-70), font, 1, color, 4, cv2.LINE_AA)
        text = cv2.putText(frame, x+" %", (int(x1)+50, int(y1)-20), font, 1, color, 4, cv2.LINE_AA)
        time.sleep(15)
        num = 0
        return num
    else:
        x = str(random.randint(0,100))
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255,0,255)
        text = cv2.putText(frame, "smile meter", (int(x1)+15, int(y1)-70), font, 1, color, 4, cv2.LINE_AA)
        text = cv2.putText(frame, x+" %", (int(x1)+50, int(y1)-20), font, 1, color, 4, cv2.LINE_AA)
        num = num + 5
        return num

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in face:
        img = cv2.rectangle(frame, (x,y), (x+(w+20), y+(h-300)), (0,0,255), -1)
        smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)
        for x1,y1,w1,h1 in smile:
            img = cv2.rectangle(frame, (x1,y1), (x1+(w1), y1+(h1)), (255,0,0), 3)
            smile_meter(frame, x, y)

    cv2.imshow("smile meter", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()