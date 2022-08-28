from PySide6 import QtWidgets
from UI_implement.Ui_pushup import Ui_PushUP

class PushupMainWindow(QtWidgets.QMainWindow):
    def __init__(self, window_title):
        # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_PushUP()
        self.ui.setupUi(self)
        self.setWindowTitle(window_title)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PushupMainWindow("健身神器")
    window.show()
    sys.exit(app.exec())