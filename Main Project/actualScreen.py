from PyQt5 import QtCore, QtGui, QtWidgets
from trans import Translator

class Ui_screen(object):
    def setupUi(self, screen):
        screen.setObjectName("screen")
        screen.resize(900, 580)
        self.userText = QtWidgets.QPlainTextEdit(screen)
        self.userText.setGeometry(QtCore.QRect(125, 445, 561, 79))
        self.userText.setStyleSheet("background-color:rgba(220,220,220,0.4);border-radius:2px;font-size:16pt;")
        self.userText.setObjectName("userText")
        self.label = QtWidgets.QLabel(screen)
        self.label.setGeometry(QtCore.QRect(95, 430, 701, 131))
        self.label.setStyleSheet("background-color:rgba(220,220,220,0.4)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.send = QtWidgets.QPushButton(screen)
        self.send.setGeometry(QtCore.QRect(690, 470, 101, 32))
        self.send.setStyleSheet("background-color:rgb(30,144,255);color:white;border:1px;border-radius:2pt;font-size:14pt;")
        self.send.setObjectName("send")
        self.command = QtWidgets.QPushButton(screen)
        self.command.setGeometry(QtCore.QRect(130, 528, 41, 32))
        self.command.setStyleSheet("background-color:rgb(30,144,255);color:white;border:1px;border-radius:2pt;font-size:14pt;")
        self.command.setObjectName("command")
        self.back = QtWidgets.QLabel(screen)
        self.back.setGeometry(QtCore.QRect(0, 0, 901, 581))
        self.back.setText("")
        self.back.setPixmap(QtGui.QPixmap("wall.jpg"))
        self.back.setScaledContents(True)
        self.back.setObjectName("back")
        self.textArea = QtWidgets.QWidget(screen)
        self.textArea.setGeometry(QtCore.QRect(100, 30, 700, 380))
        self.textArea.setObjectName("textArea")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.textArea)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lay = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lay.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.setObjectName("lay")
        self.sound = QtWidgets.QCheckBox(screen)
        self.sound.setGeometry(QtCore.QRect(370, 528, 91, 31))
        self.sound.setStyleSheet("color:white")
        self.sound.setObjectName("sound")
        self.cmdList = QtWidgets.QComboBox(screen)
        self.cmdList.setGeometry(QtCore.QRect(190, 530, 161, 26))
        self.cmdList.setObjectName("cmdList")
        self.cmdList.addItem('None')
        self.cmdList.addItem('Translate to <Language>')
        self.cmdList.addItem('Search <Search Term>')
        self.cmdList.addItem('Open <Domain Name-eg. daiict.ac.in>')
        self.cmdList.addItem('Check webmail <username> <password>')
        self.cmdList.addItem('Calc')
        self.cmdList.addItem('Images of <Search Term>')
        self.cmdList.addItem('What\'s the weather?')
        self.back.raise_()
        self.label.raise_()
        self.userText.raise_()
        self.send.raise_()
        self.command.raise_()
        self.textArea.raise_()
        self.sound.raise_()
        self.cmdList.raise_()

        self.retranslateUi(screen)
        QtCore.QMetaObject.connectSlotsByName(screen)

    def retranslateUi(self, screen):
        _translate = QtCore.QCoreApplication.translate
        screen.setWindowTitle(_translate("screen", "Form"))
        self.userText.setPlaceholderText(_translate("screen", "Type your message..."))
        self.send.setText(_translate("screen", "SEND"))
        self.command.setText(_translate("screen", "C"))
        self.sound.setText(_translate("screen", "Sound Off"))

model = Translator()