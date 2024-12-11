# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chg.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(342, 294)
        self.comboBox1 = QComboBox(Form)
        self.comboBox1.setObjectName(u"comboBox1")
        self.comboBox1.setGeometry(QRect(170, 150, 141, 41))
        self.comboBox2 = QComboBox(Form)
        self.comboBox2.setObjectName(u"comboBox2")
        self.comboBox2.setGeometry(QRect(170, 210, 141, 41))
        self.pushButton_chg = QPushButton(Form)
        self.pushButton_chg.setObjectName(u"pushButton_chg")
        self.pushButton_chg.setGeometry(QRect(190, 40, 121, 41))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font.setPointSize(14)
        self.pushButton_chg.setFont(font)
        self.lineEdit1 = QLineEdit(Form)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(30, 150, 131, 41))
        self.lineEdit2 = QLineEdit(Form)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(30, 210, 131, 41))
        self.textBrowser_qian = QTextBrowser(Form)
        self.textBrowser_qian.setObjectName(u"textBrowser_qian")
        self.textBrowser_qian.setGeometry(QRect(30, 40, 151, 41))
        self.textBrowser_hou = QTextBrowser(Form)
        self.textBrowser_hou.setObjectName(u"textBrowser_hou")
        self.textBrowser_hou.setGeometry(QRect(30, 90, 181, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 141, 20))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Sans Serif"])
        self.label.setFont(font1)
        self.comboBox_select = QComboBox(Form)
        self.comboBox_select.setObjectName(u"comboBox_select")
        self.comboBox_select.setGeometry(QRect(220, 90, 91, 41))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 270, 121, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f6c\u6362\u5668", None))
        self.pushButton_chg.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.textBrowser_qian.setMarkdown(QCoreApplication.translate("Form", u"0=\n"
"\n"
"", None))
        self.textBrowser_qian.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#8f8f8f;\">0=</span></p></body></html>", None))
        self.textBrowser_hou.setMarkdown(QCoreApplication.translate("Form", u"0=\n"
"\n"
"", None))
        self.textBrowser_hou.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#626262;\">0=</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#2f5e8d;\">ANit \u8f6c\u6362\u5668</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" color:#005078;\">ANit 0.1.0.1</span></p></body></html>", None))
    # retranslateUi

