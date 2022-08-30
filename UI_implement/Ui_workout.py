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
    QStatusBar, QVBoxLayout, QWidget)
import appsources_rc

class Ui_Workout(object):
    def setupUi(self, Workout):
        if not Workout.objectName():
            Workout.setObjectName(u"Workout")
        Workout.resize(800, 600)
        self.centralwidget = QWidget(Workout)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 763, 501))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(268, 80))
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.john_cena_label = QLabel(self.layoutWidget)
        self.john_cena_label.setObjectName(u"john_cena_label")
        self.john_cena_label.setMinimumSize(QSize(278, 221))
        self.john_cena_label.setPixmap(QPixmap(u"../sources/gif/john_cena.gif"))
        self.john_cena_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.john_cena_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.push_up_button = QPushButton(self.layoutWidget)
        self.push_up_button.setObjectName(u"push_up_button")
        self.push_up_button.setMinimumSize(QSize(91, 51))

        self.horizontalLayout_2.addWidget(self.push_up_button)

        self.horizontalSpacer_2 = QSpacerItem(568, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        Workout.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Workout)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        Workout.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Workout)
        self.statusbar.setObjectName(u"statusbar")
        Workout.setStatusBar(self.statusbar)

        self.retranslateUi(Workout)
        self.push_up_button.clicked.connect(Workout.open_pushup_window)

        QMetaObject.connectSlotsByName(Workout)
    # setupUi

    def retranslateUi(self, Workout):
        Workout.setWindowTitle(QCoreApplication.translate("Workout", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Workout", u"<html><head/><body><p><span style=\" color:#ff00ff;\">\u5065\u8eab\u795e\u5668</span></p></body></html>", None))
        self.john_cena_label.setText("")
#if QT_CONFIG(whatsthis)
        self.push_up_button.setWhatsThis(QCoreApplication.translate("Workout", u"<html><head/><body><p>\u958b\u59cb\u4f0f\u5730\u633a\u8eab!!!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.push_up_button.setText(QCoreApplication.translate("Workout", u"Pushup", None))
    # retranslateUi

