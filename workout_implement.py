from turtle import isvisible
from PySide6 import QtWidgets
from PySide6.QtGui import QMovie
from UI_implement.Ui_workout import Ui_Workout
from pushup_implement import PushupMainWindow

class WorkoutMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.workout_window = Ui_Workout()
        self.workout_window.setupUi(self)
        self.setWindowTitle("健身神器")

        # setup gif 
        self.setup_gif()

        # pushup window setting
        self.setup_pushup_window()
        self.workout_window.push_up_button.clicked.connect(self.open_pushup_window)


    def setup_gif(self) -> None:
        self.john_cena_gif: QMovie = QMovie(r'sources\gif\no_cat.gif')
        self.workout_window.john_cena.setMovie(self.john_cena_gif)
        self.john_cena_gif.start()

    def setup_pushup_window(self):
        self.pushup_window = PushupMainWindow(self)

    def open_pushup_window(self):
        self.pushup_window.setWindowTitle("伏地挺身")
        self.pushup_window.open_camera()
        self.pushup_window.show()

    def closeEvent(self, event):
        self.pushup_window.closeEvent(event)
        super().closeEvent(event)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WorkoutMainWindow()
    window.show()
    sys.exit(app.exec())