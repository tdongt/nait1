# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11299\Desktop\其他\qt\简易进制转换\chg.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 294)
        self.comboBox1 = QtWidgets.QComboBox(Form)
        self.comboBox1.setGeometry(QtCore.QRect(170, 150, 141, 41))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(170, 210, 141, 41))
        self.comboBox2.setObjectName("comboBox2")
        self.pushButton_chg = QtWidgets.QPushButton(Form)
        self.pushButton_chg.setGeometry(QtCore.QRect(190, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(14)
        self.pushButton_chg.setFont(font)
        self.pushButton_chg.setObjectName("pushButton_chg")
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(30, 150, 131, 41))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(30, 210, 131, 41))
        self.lineEdit2.setObjectName("lineEdit2")
        self.textBrowser_qian = QtWidgets.QTextBrowser(Form)
        self.textBrowser_qian.setGeometry(QtCore.QRect(30, 40, 151, 41))
        self.textBrowser_qian.setObjectName("textBrowser_qian")
        self.textBrowser_hou = QtWidgets.QTextBrowser(Form)
        self.textBrowser_hou.setGeometry(QtCore.QRect(30, 90, 181, 41))
        self.textBrowser_hou.setObjectName("textBrowser_hou")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_select = QtWidgets.QComboBox(Form)
        self.comboBox_select.setGeometry(QtCore.QRect(220, 90, 91, 41))
        self.comboBox_select.setObjectName("comboBox_select")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 270, 121, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "转换器"))
        self.pushButton_chg.setText(_translate("Form", "转换"))
        self.textBrowser_qian.setMarkdown(_translate("Form", "0=\n"
"\n"
""))
        self.textBrowser_qian.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#8f8f8f;\">0=</span></p></body></html>"))
        self.textBrowser_hou.setMarkdown(_translate("Form", "0=\n"
"\n"
""))
        self.textBrowser_hou.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#626262;\">0=</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#2f5e8d;\">ANit 转换器</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#005078;\">ANit 0.1.0.1</span></p></body></html>"))
