import cv2
from pose_detector import PoseDetector


cap = cv2.VideoCapture(1)

detector = PoseDetector()


dir = 0  # 0->伸直，1->彎曲
count = 0

while True:

    success, img = cap.read()

    if success:
        h, w, c = img.shape

        img = detector.find_pose(img, draw=True)

        positions = detector.find_positions(img)

        if positions:

            angle = detector.find_angle(img, 11, 13, 15)

            # bar = np.interp(angle, (50, 130), (w // 2 - 100, w // 2 + 100))
            # cv2.rectangle(img, (w // 2 - 100, h - 150), (int(bar), h - 100), (0, 255, 0), cv2.FILLED)

            if angle <= 110:
                if dir == 0:
                    count = count + 0.5
                    dir = 1

            if angle >= 150:
                if dir == 1:
                    count = count + 0.5
                    dir = 0
            cv2.putText(img, str(int(count)), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 20, cv2.LINE_AA)


        cv2.imshow('Image', img)
        
    else:
        break

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()
