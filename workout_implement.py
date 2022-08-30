from PySide6 import QtWidgets
from PySide6.QtGui import QMovie
from UI_implement.Ui_workout import Ui_Workout
from pushup_implement import PushupMainWindow


class WorkoutMainWindow(QtWidgets.QMainWindow):
    """用於建構主視窗，定義了開啟伏地挺身視窗的功能

    """

    # 建構子
    def __init__(self, parent=None) -> None:
        # 繼承父類別並初始化
        super().__init__(parent)
        # 建立主視窗物件
        self.workout_window: Ui_Workout = Ui_Workout()
        # 建立主視窗UI功能
        self.workout_window.setupUi(self)
        # 更改視窗名稱
        self.setWindowTitle("健身神器")

        # 呼叫gif函數
        self.setup_gif()

        # 呼叫建立伏地挺身視窗函數
        self.setup_pushup_window()
        # 將伏地挺身按鈕事件連結到開啟伏地挺身視窗函數
        self.workout_window.push_up_button.clicked.connect(self.open_pushup_window)

    # 建立gif函數
    def setup_gif(self) -> None:
        # 引入gif路徑
        self.john_cena_gif: QMovie = QMovie(r'sources\gif\john_cena.gif')
        # 設定gif動作
        self.workout_window.john_cena_label.setMovie(self.john_cena_gif)
        # 啟動gif執行緒
        self.john_cena_gif.start()

    # 設置伏地挺身視窗函數
    def setup_pushup_window(self) -> None:
        # 建立伏地挺身視窗物件
        self.pushup_window = PushupMainWindow(self)

    # 開啟伏地挺身視窗函數
    def open_pushup_window(self) -> None:
        # 更改伏地挺身視窗名稱
        self.pushup_window.setWindowTitle("伏地挺身")
        # 顯示伏地挺身視窗
        self.pushup_window.show()
        # 呼叫開啟鏡頭函數
        self.pushup_window.open_camera()

    # 關閉視窗事件函數
    def closeEvent(self, event) -> None:
        self.pushup_window.closeEvent(event)
        super().closeEvent(event)


if __name__ == '__main__':
    import sys
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: WorkoutMainWindow = WorkoutMainWindow()
    window.show()
    sys.exit(app.exec())
