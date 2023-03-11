import cv2

face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
text = 'MBS3523 Assignment 1 - Q3  Name: IP CHUN HUNG'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 2

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int((frame.shape[1] - text_size[0]) / 2)
    text_y = int(text_size[1] + 10)
    cv2.putText(gray, text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        roi_c = frame[y:y + h, x:x + w].copy()
        gray[y:y + h, x:x + w]=roi_c

    cv2.imshow('New Frame', gray)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()