import numpy as np
import cv2
import time
from typing import Literal
from PySide6.QtCore import QThread, Signal
from solutions.pushup_detector import PushupDetector
from numpy import ndarray


class Camera(QThread):
    """
    定義鏡頭執行緒的功能,並且進行辨識,然後將辨識完成的影像存入numpy_frame並發射(emit)回去
    這裡回傳的影像會被伏地挺身視窗的connect函數接收到,並傳到connect連結的函數進行後續處理

    辨識完畢 -> emit 發射 -> connect 接收 -> 傳入 connect 括號內連結的函數
    """

    # 要被發射的變數
    numpy_frame: Signal = Signal(np.ndarray)

    # 建構子
    def __init__(self, parent=None):
        """ 初始化
            - 執行 QtCore.QThread 的初始化
            - 建立 cv2 的 VideoCapture 物件
            - 設定屬性來確認狀態
            - self.connect:連接狀態
            - self.running:讀取狀態
        """
        # 繼承父類別並初始化
        super().__init__(parent)

        # 建立 cv2 的攝影機物件
        # DSHOW -> Direct Show -> 可取得更高的解析度
        self.cam = cv2.VideoCapture(1, cv2.CAP_DSHOW) if cv2.VideoCapture(1).isOpened() else cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # 鏡頭連接旗標，預設為False
        self.connected = False
        # 鏡頭執行旗標，預設為False
        self.running = False

        # 建立伏地挺身辨識物件
        self.detector: PushupDetector = PushupDetector()

    def run(self) -> None:
        """ 執行多執行緒
            - 讀取影像
            - 發送影像
            - 簡易異常處理
        """

        # 呼叫計數器歸零函數
        self.detector.recounting()

        # 當攝影機連接上並開始執行時，則開始讀取影像
        while self.connected and self.running:
            # 讀取影像
            ret, frame = self.cam.read()

            # 若影像非None，則進行辨識並發射回辨識後的影像
            if frame is not None:
                # 進行辨識
                detected_frame: ndarray = self.detector.detecting(frame)
                # 發射影像
                self.numpy_frame.emit(detected_frame)

    # 連接鏡頭函數
    def open(self) -> None:
        # 鏡頭成功連接
        self.connected: Literal[True] = True

    # 開始執行函數
    def start_reading(self) -> None:
        # 鏡頭開始執行
        self.running: Literal[True] = True

    # 關閉鏡頭函數
    def stop_camera(self) -> None:
        # 斷開鏡頭
        self.connected = False

    # 釋放鏡頭資源函數
    def release_camera(self) -> None:
        # 斷開鏡頭
        self.connected = False
        # 釋放鏡頭資源
        self.cam.release()
