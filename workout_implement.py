from PySide6 import QtWidgets
from PySide6.QtGui import QMovie
from UI_implement.Ui_workout import Ui_Workout
from pushup_implement import PushupMainWindow

class WorkoutMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.workout_window = Ui_Workout()
        self.workout_window.setupUi(self)
        self.setWindowTitle("健身神器")

        # setup gif 
        self.setup_gif()

        # pushup window setting
        self.open_pushup_window(window_title="伏地挺身")

        
    def setup_gif(self) -> None:
        self.john_cena_gif: QMovie = QMovie('sources\gif\john_cena.gif')
        self.workout_window.john_cena.setMovie(self.john_cena_gif)
        self.john_cena_gif.start()

    def open_pushup_window(self, window_title="伏地挺身"):
        self.pushup_window = PushupMainWindow(window_title)
        self.workout_window.push_up_button.clicked.connect(self.pushup_window.show)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WorkoutMainWindow()
    window.show()
    sys.exit(app.exec())