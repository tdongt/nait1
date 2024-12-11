# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QPushButton, QRadioButton, QSizePolicy, QTextBrowser,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(540, 370)
        self.yuanlan = QComboBox(Form)
        self.yuanlan.setObjectName(u"yuanlan")
        self.yuanlan.setGeometry(QRect(390, 80, 131, 51))
        self.hou_lan = QComboBox(Form)
        self.hou_lan.setObjectName(u"hou_lan")
        self.hou_lan.setGeometry(QRect(390, 270, 131, 51))
        self.hou = QTextBrowser(Form)
        self.hou.setObjectName(u"hou")
        self.hou.setGeometry(QRect(10, 200, 341, 131))
        self.trans = QPushButton(Form)
        self.trans.setObjectName(u"trans")
        self.trans.setGeometry(QRect(400, 180, 121, 61))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(12)
        self.trans.setFont(font)
        self.yuan = QTextEdit(Form)
        self.yuan.setObjectName(u"yuan")
        self.yuan.setGeometry(QRect(10, 40, 341, 131))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 340, 141, 20))
        self.auto_2 = QRadioButton(Form)
        self.auto_2.setObjectName(u"auto_2")
        self.auto_2.setGeometry(QRect(360, 150, 101, 20))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(8)
        self.auto_2.setFont(font1)
        self.lanout = QLineEdit(Form)
        self.lanout.setObjectName(u"lanout")
        self.lanout.setGeometry(QRect(460, 150, 71, 20))
        self.lanout.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u5668", None))
        self.trans.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u4e3a", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">ANit TRANSLATOR one1</p><p align=\"center\">0.01.1</p><p align=\"center\"><br/></p></body></html>", None))
        self.auto_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u68c0\u6d4b\u8bed\u8a00\uff1a", None))
    # retranslateUi

