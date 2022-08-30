import cv2
import math
import mediapipe as mp
from numpy import ndarray


class PoseDetector():
    """姿勢檢測物件
    """

    # 建構子
    def __init__(self,
                 static_image_mode=False,       # 辨識照片才需開啟
                 smooth_landmarks=True,         # 設置為True可以減少抖動
                 min_detection_confidence=0.5,  # 最小偵測信心程度，小於此值將直接忽略
                 min_tracking_confidence=0.5    # 最小追蹤信心程度，小於此值將直接忽略
                 ) -> None:
        self.static_image_mode = static_image_mode
        self.smooth_landmarks = smooth_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        # 建立姿勢辨識物件
        self.pose = mp.solutions.pose.Pose(
            static_image_mode=self.static_image_mode,
            model_complexity=2,  # 物件複雜度，範圍:1~2，越大辨識時間越久，但越準確
            smooth_landmarks=self.smooth_landmarks,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )

    # 尋找姿勢函數
    def find_pose(self, img: ndarray, draw=True) -> ndarray:
        """將影像進行辨識並繪圖後回傳

        Args:
            img (ndarray): 要辨識的影像
            draw (bool, optional): 是否繪圖，預設為是

        Returns:
            ndarray: 辨識過後的影像
        """

        # 將openCV影像色彩通道轉為mediapipe使用的格式
        # openCV -> BGR 通道， mediapipe -> RGB 通道
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 將影像進行辨識
        self.results = self.pose.process(imgRGB)

        # 如果有辨識到，就進行繪圖
        if self.results.pose_landmarks:
            # 如果有要繪圖，就呼叫繪圖函數
            if draw:
                mp.solutions.drawing_utils.draw_landmarks(img, self.results.pose_landmarks,
                                                          mp.solutions.pose.POSE_CONNECTIONS)

        # 回傳辨識過後的影像
        return img

    # 取得姿勢資料表
    def find_positions(self, img) -> list:
        """取得姿勢資料

        Args:
            img (ndarray): 輸入的影像

        Returns:
            list: 姿勢位置陣列 [id, x, y]
        """

        # 儲存資料陣列
        self.lmslist = []
        # 若是有判斷到點，則新增進陣列
        if self.results.pose_landmarks:
            # 取得id及位置
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # 取得影像大小及通道數量
                h, w, c = img.shape
                # 點的x及y軸
                cx, cy = int(lm.x * w), int(lm.y * h)
                # 新增進陣列
                self.lmslist.append([id, cx, cy])

        # 回傳陣列
        return self.lmslist

    # 計算角度函數
    def find_angle(self, img, p1, p2, p3, draw=True) -> int:
        """用於計算角度

        Args:
            img (ndarray): 當前影像
            p1 (list): 手腕點
            p2 (list): 手軸點
            p3 (list): 肩膀點
            draw (bool, optional): 是否繪圖，預設為是

        Returns:
            int: 手臂與肩膀的角度
        """

        # 取得手腕點的x及y軸
        x1, y1 = self.lmslist[p1][1], self.lmslist[p1][2]
        # 取得手軸點的x及y軸
        x2, y2 = self.lmslist[p2][1], self.lmslist[p2][2]
        # 取得肩膀點的x及y軸
        x3, y3 = self.lmslist[p3][1], self.lmslist[p3][2]

        # 計算角度
        angle = int(math.degrees(math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2)))

        # 將角度保持在0~180之間
        # 若是角度小於0
        if angle < 0:
            # +360
            angle: int = angle + 360
        # 若是角度大於0
        if angle > 180:
            # 360減去目前角度
            angle: int = 360 - angle

        # 判斷是否要畫圖
        if draw:
            # 畫上圓形並塗滿
            cv2.circle(img, (x1, y1), 20, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 30, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 20, (0, 255, 255), cv2.FILLED)
            # 畫上直線
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255, 3))
            cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255, 3))
            # 顯示文字於影像上
            cv2.putText(img, str(angle), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

        # 回傳影像
        return angle


if __name__ == "__main__":
    test = PoseDetector()
