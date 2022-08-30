import cv2

a = cv2.VideoCapture(1)

# success, img = cap.read()

cam = cv2.VideoCapture(1) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0)

while True:
    success, img = cam.read()

    cv2.imshow('test', img)

    if cv2.waitKey(1) == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()