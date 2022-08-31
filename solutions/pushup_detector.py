import cv2
from numpy import ndarray
from typing import Literal
try:
    from solutions.pose_detector import PoseDetector
except ModuleNotFoundError:
    from pose_detector import PoseDetector


class PushupDetector():
    """伏地挺身物件
        - 將影像進行辨識
        - 判斷手軸角度
        - 計數
    """

    # 建構子
    def __init__(self) -> None:
        # 建立姿勢辨識物件
        self.detector: PoseDetector = PoseDetector()
        # 方向變數(1->往下，0->往上)
        self.dir: Literal[0] = 0
        # 計數變數
        self.count: Literal[0] = 0

    # 辨識函數
    def detecting(self, frame: ndarray) -> ndarray:
        # 若是影像不為None，則呼叫辨識並計算角度
        if frame is not None:
            # 取得影像大小及通道
            h, w, c = frame.shape
            # 對影像進行姿勢辨識
            detected_frame: ndarray = self.detector.find_pose(frame, draw=True)
            # 對影像進行編號點辨識
            positions: list = self.detector.find_positions(detected_frame)

            # 如果編號點總數不為0，則尋找手軸的點並進行辨識
            if len(positions) != 0:

                # 計算手軸角度
                angle = self.detector.find_angle(frame, 11, 13, 15)

                # 如果角度小於110，則判斷方向是否為向下
                if angle <= 110:
                    # 如果方向向下，則將計數器+0.5，方向變數改為1(向上)
                    if self.dir == 0:
                        # 計數器+0.5
                        self.count += 0.5
                        # 方向變數改為1
                        self.dir = 1

                # 如果角度大於150，則判斷方向是否為向上
                if angle >= 150:
                    # 如果方向向上，則將計數器+0.5，方向變數改為0(向下)
                    if self.dir == 1:
                        # 計數器+0.5
                        self.count += 0.5
                        # 方向變數改為0
                        self.dir = 0

                # 將文字顯示在影像上
                # 參數意義(照順序):辨識過的影像，要顯示的文字，文字位置(左上角)，字體，大小，顏色，粗細，線條風格
                cv2.putText(detected_frame, str(int(self.count)), (w // 2+100, h // 2-100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 20)

                # 回傳辨識過的影像
                return detected_frame
            else:
                # 回傳未辨識的影像
                return frame
        else:
            # 回傳未辨識的影像
            return frame

    # 計數器歸零函數
    def recounting(self) -> None:
        self.dir = 0
        self.count = 0


if __name__ == '__main__':
    cam = cv2.VideoCapture(1)
    test = PushupDetector()

    while 1:
        success, frame = cam.read()

        detected_frame = test.detecting(frame)
        # print(F"line 50: {detected_frame}")
        if detected_frame is not None:
            cv2.imshow('test', detected_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
