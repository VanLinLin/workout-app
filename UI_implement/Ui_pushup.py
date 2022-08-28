# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pushup.ui'
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
    QMenuBar, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_PushUP(object):
    def setupUi(self, PushUP):
        if not PushUP.objectName():
            PushUP.setObjectName(u"PushUP")
        PushUP.resize(798, 600)
        PushUP.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(PushUP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.show_frame_label = QLabel(self.centralwidget)
        self.show_frame_label.setObjectName(u"show_frame_label")
        self.show_frame_label.setMinimumSize(QSize(640, 480))
        self.show_frame_label.setMaximumSize(QSize(640, 480))

        self.horizontalLayout.addWidget(self.show_frame_label)

        self.horizontalSpacer_2 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        PushUP.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PushUP)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 21))
        PushUP.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PushUP)
        self.statusbar.setObjectName(u"statusbar")
        PushUP.setStatusBar(self.statusbar)

        self.retranslateUi(PushUP)

        QMetaObject.connectSlotsByName(PushUP)
    # setupUi

    def retranslateUi(self, PushUP):
        PushUP.setWindowTitle(QCoreApplication.translate("PushUP", u"MainWindow", None))
        self.show_frame_label.setText("")
    # retranslateUi

