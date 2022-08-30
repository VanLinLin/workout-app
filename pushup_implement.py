import cv2
from numpy import ndarray
from PySide6.QtGui import QImage, QPixmap
from PySide6 import QtWidgets
from UI_implement.Ui_pushup import Ui_PushUP
from camera import Camera


class PushupMainWindow(QtWidgets.QMainWindow):
    """用於建立伏地挺身視窗以及開啟鏡頭執行緒

    """

    # 建構子
    def __init__(self, parent=None):
        # 繼承父類別並初始化
        super().__init__(parent)
        # 建立伏地挺身視窗物件
        self.pushup_window: Ui_PushUP = Ui_PushUP()
        # 建立伏地挺身視窗UI功能
        self.pushup_window.setupUi(self)

        # 呼叫設置鏡頭函數
        self.setup_camera()

    # 設置鏡頭函數
    def setup_camera(self) -> None:
        # 建立鏡頭物件
        self.camera = Camera()
        # 將辨識完畢回傳回來的訊號連結到顯示影像函數
        self.camera.numpy_frame.connect(self.show_video)
        # 呼叫開啟鏡頭函數
        self.camera.open()
        # 呼叫開始讀取影像函數
        self.camera.start_reading()

    # 顯示影像函數
    def show_video(self, cv_frame: ndarray) -> None:
        # 若影像不為None則呼叫轉換格式函數
        if cv_frame is not None:
            # 將openCV格式轉換為Qt能顯示的格式
            qt_img: QPixmap = self.convert_cv2qt(cv_frame)
            # 將影像顯示到label上
            self.pushup_window.show_frame_label.setPixmap(qt_img)

    # openCV格式轉換到Qt格式函數
    def convert_cv2qt(self, cv_frame: ndarray) -> QPixmap:
        # 若影像不為None則將影像進行轉換
        if cv_frame is not None:
            # 將openCV色彩通道轉換為Qt格式
            rgb_img = cv2.cvtColor(cv_frame, cv2.COLOR_BGR2RGB)
            # 取得影像大小及通道數
            h, w, channels = rgb_img.shape
            # 計算每一行的位元組
            bytes_per_line = channels * w
            # 轉換影像(QImage格式)
            convert_to_Qt_format: QImage = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
            # 轉換成QPixmap格式並回傳
            return QPixmap.fromImage(convert_to_Qt_format)

    # 開啟鏡頭函數
    def open_camera(self) -> None:
        # 將鏡頭連接旗標設為True
        self.camera.connected = True
        # 將鏡頭執行旗標設為True
        self.camera.running = True
        # 啟動鏡頭執行緒
        self.camera.start()

    # 關閉視窗事件函數
    def closeEvent(self, event) -> None:
        # 呼叫停止鏡頭函數
        self.camera.stop_camera()
        # 呼叫停止執行緒函數
        self.camera.quit()
        # 阻塞執行緒直到執行緒確實停止
        self.camera.wait()
        super().closeEvent(event)

    # 釋放鏡頭資源函數
    def release_camera(self) -> None:
        # 呼叫釋放鏡頭資源函數
        self.camera.release_camera()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PushupMainWindow()
    window.show()
    window.open_camera()
    sys.exit(app.exec())
