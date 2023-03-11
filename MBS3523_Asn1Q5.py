import cv2


def nil(x):
    pass


text = 'MBS3523 Assignment 1 - Q5  Name: IP CHUN HUNG'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 2

cv2.namedWindow("Frame")
cv2.createTrackbar("X_POS", "Frame", 0, 640, nil)
cv2.createTrackbar("Y_POS", "Frame", 0, 480, nil)

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:
    ret, frame = cam.read()
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int((frame.shape[1] - text_size[0]) / 2)
    text_y = int(text_size[1] + 10)
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness)
    x_pos = cv2.getTrackbarPos("X_POS", "Frame")
    y_pos = cv2.getTrackbarPos("Y_POS", "Frame")
    cv2.line(frame, (x_pos, 0), (x_pos, 480), (255, 0, 0), 2)
    cv2.line(frame, (0, y_pos), (640, y_pos), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
