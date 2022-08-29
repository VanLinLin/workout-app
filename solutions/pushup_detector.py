import cv2
try:
    from solutions.pose_detector import PoseDetector
except ModuleNotFoundError:
    from pose_detector import PoseDetector

class PushupDetector():
    def __init__(self):
        self.detector = PoseDetector()
        self.dir = 0
        self.count = 0
    
    def detecting(self, frame):
        # print(f"line 14: {frame}")
        if frame is not None:
            h, w, c = frame.shape
            detected_frame = self.detector.find_pose(frame, draw=True)
            positions = self.detector.find_positions(detected_frame)
            # print(F"line 19: {positions}")
            if len(positions) != 0:

                angle = self.detector.find_angle(frame, 11, 13, 15)

                if angle <= 110:
                    if self.dir == 0:
                        self.count += 0.5
                        self.dir = 1

                if angle >= 150:
                    if self.dir == 1:
                        self.count += 0.5
                        self.dir = 0
                cv2.putText(detected_frame, str(int(self.count)), (w // 2+100, h // 2-100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 20, cv2.LINE_AA)
                # print(F"line 34: {detected_frame}")
                return detected_frame
            else:
                return frame
        else:
            return frame

    def recounting(self):
        self.dir = 0
        self.count = 0

if __name__ == '__main__':
    cam = cv2.VideoCapture(1)
    test = PushupDetector()

    while 1:
        success, frame = cam.read()
        # if success == True:
            # print(F'Line 45: {"is true"}')
        # if frame is None:
            # print(F'line 47: {"is none"}')

        detected_frame = test.detecting(frame)
        # print(F"line 50: {detected_frame}")
        if detected_frame is not None:
            cv2.imshow('test', detected_frame)

        if cv2.waitKey(1) == ord('q'):
            break
        
    cam.release()
    cv2.destroyAllWindows()