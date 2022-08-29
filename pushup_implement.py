import cv2
import os
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from UI_implement.Ui_pushup import Ui_PushUP
from camera import Camera

class PushupMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pushup_window = Ui_PushUP()
        self.pushup_window.setupUi(self)

        self.setup_camera()
        

    def setup_camera(self):
        self.camera = Camera()
        # print(F"camera init, {self.camera.connected}, {self.camera.running}")
        self.camera.numpy_frame.connect(self.show_video)
        self.camera.open()
        self.camera.start_reading()


    def show_video(self, cv_frame):
        # print(F"line 25:{cv_frame}")
        if cv_frame is not None:
            qt_img = self.convert_cv2qt(cv_frame)
            self.pushup_window.show_frame_label.setPixmap(qt_img)

    def convert_cv2qt(self, cv_frame):
        # print(F"line 30 : {cv_frame}")
        if cv_frame is not None:
            rgb_img = cv2.cvtColor(cv_frame, cv2.COLOR_BGR2RGB)
            h, w, channels = rgb_img.shape
            bytes_per_line = channels * w
            convert_to_Qt_format = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
            return QPixmap.fromImage(convert_to_Qt_format) 
            # p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
            # return QPixmap.fromImage(p)        

    def open_camera(self):
        # print(F"{self.camera.connected}, {self.camera.running}")
        self.camera.connected = True
        self.camera.running = True
        self.camera.start()

    # 關閉主視窗的彈出式視窗提示
    def closeEvent(self, event):
        self.camera.stop_camera()
        self.camera.quit()
        self.camera.wait()
        super().closeEvent(event)
        # print("thread close")

    def release_camera(self):
        self.camera.release_camera()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PushupMainWindow()
    window.show()
    window.open_camera()
    sys.exit(app.exec())