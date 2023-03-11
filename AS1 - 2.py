import cv2

cam = cv2.VideoCapture(0)

while (True):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Face with colour', frame)

    ret, BnW = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Face in black and white', BnW)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()