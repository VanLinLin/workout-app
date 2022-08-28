import numpy as np
import cv2
import time
from PySide6.QtCore import QThread, Signal

class Camera(QThread):
    numpy_frame = Signal(np.ndarray)

    def __init__(self, parent=None):
        """ 初始化
            - 執行 QtCore.QThread 的初始化
            - 建立 cv2 的 VideoCapture 物件
            - 設定屬性來確認狀態
            - self.connect：連接狀態
            - self.running：讀取狀態
        """
        # 將父類初始化
        super().__init__(parent)
        # 建立 cv2 的攝影機物件
        self.cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        self.connected = False
        self.running = False

    def run(self):
        """ 執行多執行緒
            - 讀取影像
            - 發送影像
            - 簡易異常處理
        """
        # 當正常連接攝影機才能進入迴圈
        while self.connected and self.running:
            ret, img = self.cam.read()    # 讀取影像
            if ret:
                self.numpy_frame.emit(img)    # 發送影像
            else:    # 例外處理
                print("Warning!!!")
                self.release_camera()

    def open(self):
        """ 連接攝影機 """
        self.connected = True    # 啟動讀取狀態

    def start_reading(self):
        """ 開始攝影機影像讀取功能 """
        self.running = True

    def release_camera(self):
        """ 關閉攝影機功能 """
        self.connected = False    # 關閉讀取狀態
        time.sleep(1)
        self.cam.release()      # 釋放攝影機