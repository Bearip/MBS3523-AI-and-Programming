import cv2

face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        roi_c = frame[y:y + h, x:x + w].copy()
        gray[y:y + h, x:x + w]=roi_c

    cv2.imshow('New Frame', gray)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()