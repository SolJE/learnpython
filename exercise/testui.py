# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.status_lineEdit = QtWidgets.QLineEdit(Form)
        self.status_lineEdit.setGeometry(QtCore.QRect(9, 190, 381, 20))
        self.status_lineEdit.setObjectName("status_lineEdit")
        self.replace_Button = QtWidgets.QPushButton(Form)
        self.replace_Button.setGeometry(QtCore.QRect(9, 268, 75, 23))
        self.replace_Button.setObjectName("replace_Button")
        self.runtime_lineEdit = QtWidgets.QLineEdit(Form)
        self.runtime_lineEdit.setGeometry(QtCore.QRect(9, 242, 381, 20))
        self.runtime_lineEdit.setObjectName("runtime_lineEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(9, 216, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.mac_lineEdit = QtWidgets.QLineEdit(Form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(10, 20, 381, 20))
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.result_textEdit = QtWidgets.QTextEdit(Form)
        self.result_textEdit.setGeometry(QtCore.QRect(10, 50, 381, 131))
        self.result_textEdit.setObjectName("result_textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.replace_Button.setText(_translate("Form", "Replace"))

