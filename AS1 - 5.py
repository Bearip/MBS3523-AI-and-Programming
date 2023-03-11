import cv2

def nil(x):
    pass

cv2.namedWindow("Frame")
cv2.createTrackbar("X_POS", "Frame", 0, 640,nil)
cv2.createTrackbar("Y_POS", "Frame", 0, 480,nil)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    x_pos = cv2.getTrackbarPos("X_POS", "Frame")
    y_pos = cv2.getTrackbarPos("Y_POS", "Frame")
    cv2.line(frame, (x_pos, 0), (x_pos, 480), (255, 0, 0), 2)
    cv2.line(frame, (0, y_pos), (640, y_pos), (0, 255, 0), 2)

    cv2.putText(frame, 'MBS3523 Assignment 1 - Q3  Name: IP CHUN HUNG',
                (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()