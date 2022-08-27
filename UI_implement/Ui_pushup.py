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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_PushUP(object):
    def setupUi(self, PushUP):
        if not PushUP.objectName():
            PushUP.setObjectName(u"PushUP")
        PushUP.resize(800, 600)
        self.centralwidget = QWidget(PushUP)
        self.centralwidget.setObjectName(u"centralwidget")
        PushUP.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PushUP)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        PushUP.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PushUP)
        self.statusbar.setObjectName(u"statusbar")
        PushUP.setStatusBar(self.statusbar)

        self.retranslateUi(PushUP)

        QMetaObject.connectSlotsByName(PushUP)
    # setupUi

    def retranslateUi(self, PushUP):
        PushUP.setWindowTitle(QCoreApplication.translate("PushUP", u"MainWindow", None))
    # retranslateUi

