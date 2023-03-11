import cv2

PNT1, PNT2 = (0,0)
crop = False


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
cam.set(3,640)
cam.set(4,480)
cv2.namedWindow('Q6')
cv2.setMouseCallback('Q6', mouse_event)

while True:
    success, frame = cam.read()
    newFrame = frame.copy()
    if cam is None:
        break
    if crop:
        cv2.rectangle(newFrame, PNT1, PNT2, (0, 255, 0), 2)

        roi_1 = frame[PNT1[1]:PNT2[1], PNT1[0]:PNT2[0]]
        cv2.imshow('ROI Frame', roi_1)

    cv2.imshow('Q6', newFrame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
