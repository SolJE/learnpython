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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.status_lineEdit = QtWidgets.QLineEdit(Form)
        self.status_lineEdit.setObjectName("status_lineEdit")
        self.verticalLayout.addWidget(self.status_lineEdit)
        self.result_lineEdit = QtWidgets.QLineEdit(Form)
        self.result_lineEdit.setObjectName("result_lineEdit")
        self.verticalLayout.addWidget(self.result_lineEdit)
        self.mac_textEdit = QtWidgets.QTextEdit(Form)
        self.mac_textEdit.setObjectName("mac_textEdit")
        self.verticalLayout.addWidget(self.mac_textEdit)
        self.runtime_lineEdit = QtWidgets.QLineEdit(Form)
        self.runtime_lineEdit.setObjectName("runtime_lineEdit")
        self.verticalLayout.addWidget(self.runtime_lineEdit)
        self.replace_Button = QtWidgets.QPushButton(Form)
        self.replace_Button.setObjectName("replace_Button")
        self.verticalLayout.addWidget(self.replace_Button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.replace_Button.setText(_translate("Form", "Replace"))

