# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newFrame.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 205)
        self.fr = QtWidgets.QFrame(Form)
        self.fr.setGeometry(QtCore.QRect(0, 20, 521, 111))
        self.fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr.setObjectName("fr")
        self.inputText = QtWidgets.QPlainTextEdit(self.fr)
        self.inputText.setGeometry(QtCore.QRect(10, 20, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputText.sizePolicy().hasHeightForWidth())
        self.inputText.setSizePolicy(sizePolicy)
        self.inputText.setStyleSheet("background-color:rgba(220,220,220,0.4);border-radius:2px;font-size:16pt;")
        self.inputText.setReadOnly(True)
        self.inputText.setObjectName("inputText")
        self.label = QtWidgets.QLabel(self.fr)
        self.label.setGeometry(QtCore.QRect(390, 40, 41, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("dash.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.userr = QtWidgets.QLabel(self.fr)
        self.userr.setGeometry(QtCore.QRect(440, 20, 60, 51))
        self.userr.setText("")
        self.userr.setPixmap(QtGui.QPixmap("profile.png"))
        self.userr.setScaledContents(True)
        self.userr.setObjectName("userr")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

