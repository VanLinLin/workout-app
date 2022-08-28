# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)
import appsources_rc

class Ui_Workout(object):
    def setupUi(self, Workout):
        if not Workout.objectName():
            Workout.setObjectName(u"Workout")
        Workout.resize(800, 600)
        self.centralwidget = QWidget(Workout)
        self.centralwidget.setObjectName(u"centralwidget")
        self.push_up_button = QPushButton(self.centralwidget)
        self.push_up_button.setObjectName(u"push_up_button")
        self.push_up_button.setGeometry(QRect(60, 410, 91, 51))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 20, 641, 202))
        self.app_name = QHBoxLayout(self.layoutWidget)
        self.app_name.setObjectName(u"app_name")
        self.app_name.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)

        self.app_name.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.app_name.addItem(self.horizontalSpacer)

        self.john_cena = QLabel(self.layoutWidget)
        self.john_cena.setObjectName(u"john_cena")
        self.john_cena.setPixmap(QPixmap(u":/gif/gif/john_cena.gif"))
        self.john_cena.setAlignment(Qt.AlignCenter)

        self.app_name.addWidget(self.john_cena)

        Workout.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Workout)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        Workout.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Workout)
        self.statusbar.setObjectName(u"statusbar")
        Workout.setStatusBar(self.statusbar)

        self.retranslateUi(Workout)
        self.push_up_button.clicked.connect(Workout.show)

        QMetaObject.connectSlotsByName(Workout)
    # setupUi

    def retranslateUi(self, Workout):
        Workout.setWindowTitle(QCoreApplication.translate("Workout", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.push_up_button.setWhatsThis(QCoreApplication.translate("Workout", u"<html><head/><body><p>\u958b\u59cb\u4f0f\u5730\u633a\u8eab!!!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.push_up_button.setText(QCoreApplication.translate("Workout", u"Pushup", None))
        self.label.setText(QCoreApplication.translate("Workout", u"<html><head/><body><p><span style=\" color:#ff00ff;\">\u5065\u8eab\u795e\u5668</span></p></body></html>", None))
        self.john_cena.setText("")
    # retranslateUi

