import cv2
import numpy as np

f_width, f_height = 640, 480
box_size = 80
cam = cv2.VideoCapture(0)

box_x = np.random.randint(0, f_width - box_size)
box_y = np.random.randint(0, f_height - box_size)
ang = np.random.randint(15, 75)
speed = 4

while True:
    ret, frame = cam.read()
    cv2.putText(frame, 'MBS3523 Assignment 1 - Q3  Name: IP CHUN HUNG', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.rectangle(frame, (box_x, box_y), (box_x+box_size, box_y+box_size), (0, 0, 255), 2)

    delta_x = speed * np.cos(np.deg2rad(ang))
    delta_y = speed * np.sin(np.deg2rad(ang))
    box_x, box_y = box_x + int(delta_x), box_y + int(delta_y)

    if box_x < 0:
        box_x = 0
        ang = 180-ang
    elif box_x + box_size > f_width:
        box_x = f_width - box_size
        ang = 180-ang

    if box_y < 0:
        box_y = 0
        ang = -ang
    elif box_y + box_size > f_height:
        box_y = f_height - box_size
        ang = -ang

    cv2.imshow('Frame', frame)

    if cv2.waitKey(2) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
