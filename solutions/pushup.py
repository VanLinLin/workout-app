import cv2
from pose_detector import PoseDetector


cap = cv2.VideoCapture(1)

detector = PoseDetector()


dir = 0  # 0->伸直，1->彎曲
count = 0

while True:


    try:
        success, img = cap.read()
        if success:
            h, w, c = img.shape

            img = detector.find_pose(img, draw=True)

            positions = detector.find_positions(img)

            if positions:

                angle = detector.find_angle(img, 11, 13, 15)

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
            cap.release()
            cv2.destroyAllWindows()
            break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()


