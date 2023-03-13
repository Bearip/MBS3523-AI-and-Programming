import cv2

PNT1, PNT2 = (0, 0)
crop = False
text = 'MBS3523 Assignment 1 - Q6  Name: IP CHUN HUNG'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 2

def mouse_event(event, x, y, flags, param):
    global PNT1, PNT2, crop

    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x, y)
        crop = False

    elif event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x, y)
        crop = True

    elif event == cv2.EVENT_RBUTTONDOWN:
        PNT1, PNT2 = (0, 0)
        crop = False
        cv2.destroyWindow('ROI Frame')

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cv2.namedWindow('Q6')
cv2.setMouseCallback('Q6', mouse_event)

while True:
    success, frame = cam.read()
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int((frame.shape[1] - text_size[0]) / 2)
    text_y = int(text_size[1] + 10)
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness)
    newFrame = frame.copy()
    if cam is None:
        break
    if crop:
        x1, y1 = PNT1
        x2, y2 = PNT2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow('Q6', frame)
        roi_1 = frame[y1:y2, x1:x2]
        if roi_1.shape[0] > 0 and roi_1.shape[1] > 0:
            cv2.imshow('ROI Frame', roi_1)
        else:
            crop = False

    cv2.imshow('Q6', newFrame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cam.release()
cv2.destroyAllWindows()
