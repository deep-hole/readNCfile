# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 529)
        font = QFont()
        font.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.click_print = QPushButton(self.centralwidget)
        self.click_print.setObjectName(u"click_print")
        self.click_print.setGeometry(QRect(600, 40, 81, 31))
        self.click_print.setFont(font)
        self.filename_line = QLineEdit(self.centralwidget)
        self.filename_line.setObjectName(u"filename_line")
        self.filename_line.setEnabled(False)
        self.filename_line.setGeometry(QRect(170, 40, 401, 31))
        font1 = QFont()
        font1.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font1.setPointSize(11)
        self.filename_line.setFont(font1)
        self.filename_line.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.filename_line.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filename_line.setReadOnly(True)
        self.plot = QWidget(self.centralwidget)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(140, 90, 621, 381))
        self.fileProperties = QTextBrowser(self.plot)
        self.fileProperties.setObjectName(u"fileProperties")
        self.fileProperties.setEnabled(True)
        self.fileProperties.setGeometry(QRect(10, 0, 621, 381))
        font2 = QFont()
        font2.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font2.setPointSize(12)
        self.fileProperties.setFont(font2)
        self.vars_box = QComboBox(self.centralwidget)
        self.vars_box.setObjectName(u"vars_box")
        self.vars_box.setGeometry(QRect(10, 120, 131, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 90, 41, 21))
        font3 = QFont()
        font3.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.draw = QPushButton(self.centralwidget)
        self.draw.setObjectName(u"draw")
        self.draw.setGeometry(QRect(20, 170, 111, 31))
        self.draw.setFont(font)
        self.Prev_plot = QPushButton(self.centralwidget)
        self.Prev_plot.setObjectName(u"Prev_plot")
        self.Prev_plot.setGeometry(QRect(10, 390, 61, 31))
        font4 = QFont()
        font4.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.Prev_plot.setFont(font4)
        self.Next_plot = QPushButton(self.centralwidget)
        self.Next_plot.setObjectName(u"Next_plot")
        self.Next_plot.setGeometry(QRect(80, 390, 61, 31))
        self.Next_plot.setFont(font)
        self.close_plot = QPushButton(self.centralwidget)
        self.close_plot.setObjectName(u"close_plot")
        self.close_plot.setGeometry(QRect(10, 430, 61, 31))
        self.close_plot.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u725b\u903cnc\u6587\u4ef6\u8bfb\u53d6", None))
        self.click_print.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.filename_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8bfb\u53d6\u6587\u4ef6", None))
        self.vars_box.setCurrentText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None))
        self.draw.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316", None))
        self.Prev_plot.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.Next_plot.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.close_plot.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u56fe\u50cf", None))
    # retranslateUi

