from PySide6 import QtWidgets
from PySide6.QtGui import QMovie
from UI_implement.Ui_workout import Ui_Workout

class WorkoutMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.workout_window = Ui_Workout()
        self.workout_window.setupUi(self)
        self.setWindowTitle("健身神器")

        # setup gif 
        self.setup_gif()
        
    def setup_gif(self) -> None:
        self.john_cena_gif: QMovie = QMovie('sources\gif\john_cena.gif')
        self.workout_window.john_cena.setMovie(self.john_cena_gif)
        self.john_cena_gif.start()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())