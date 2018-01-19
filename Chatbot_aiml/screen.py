from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gtts import gTTS
from googletrans import Translator

class Ui_chatBot(object):
    def setupUi(self, chatBot):
        chatBot.setObjectName("chatBot")
        chatBot.resize(500, 400)
        self.userText = QTextEdit(chatBot)
        self.userText.setGeometry(QtCore.QRect(0, 30, 240, 211))
        self.userText.setStyleSheet("font-size:16pt;")
        self.userText.setObjectName("userText")
        self.chatbotText = QtWidgets.QTextEdit(chatBot)
        self.chatbotText.setGeometry(QtCore.QRect(260, 30, 240, 291))
        self.chatbotText.setStyleSheet("background-color:#87ceeb;color:black;font-size: 16pt")
        self.chatbotText.setReadOnly(True)
        self.chatbotText.setObjectName("chatbotText")
        self.send = QtWidgets.QPushButton(chatBot)
        self.send.setGeometry(QtCore.QRect(220, 140, 61, 71))
        self.send.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.send.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("se.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon)
        self.send.setIconSize(QtCore.QSize(50, 50))
        self.send.setObjectName("send")
        self.back = QtWidgets.QLabel(chatBot)
        self.back.setGeometry(QtCore.QRect(0, 0, 501, 401))
        self.back.setText("")
        self.back.setPixmap(QtGui.QPixmap("cr.jpg"))
        self.back.setScaledContents(True)
        self.back.setObjectName("back")
        self.prevText = QtWidgets.QTextEdit(chatBot)
        self.prevText.setGeometry(QtCore.QRect(0, 240, 240, 81))
        self.prevText.setReadOnly(True)
        self.prevText.setObjectName("prevText")
        self.label = QtWidgets.QLabel(chatBot)
        self.label.setGeometry(QtCore.QRect(72, 223, 91, 16))
        self.label.setObjectName("label")
        self.e2send = QtWidgets.QCheckBox(chatBot)
        self.e2send.setGeometry(QtCore.QRect(50, 330, 131, 20))
        self.e2send.setStyleSheet("color:white;")
        self.e2send.setObjectName("e2send")
        self.sound = QtWidgets.QCheckBox(chatBot)
        self.sound.setGeometry(QtCore.QRect(330, 330, 121, 20))
        self.sound.setStyleSheet("color:white;")
        self.sound.setObjectName("sound")
        self.back.raise_()
        self.userText.raise_()
        self.chatbotText.raise_()
        self.send.raise_()
        self.prevText.raise_()
        self.label.raise_()
        self.e2send.raise_()
        self.sound.raise_()

        self.retranslateUi(chatBot)
        QtCore.QMetaObject.connectSlotsByName(chatBot)

    def retranslateUi(self, chatBot):
        _translate = QtCore.QCoreApplication.translate
        chatBot.setWindowTitle(_translate("chatBot", "Form"))
        self.userText.setPlaceholderText(_translate("chatBot", "Type Here..."))
        self.label.setText(_translate("chatBot", "Previous Text"))
        self.e2send.setText(_translate("chatBot", "Tap Enter to send"))
        self.sound.setText(_translate("chatBot", "Turn off sound"))
model = Translator()
class textBox(QTextEdit):
    sgn = pyqtSignal(int)
    def __init__(self, parent=None):
        super(textBox, self).__init__(parent)
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Enter:
            self.sgn.emit(10)
        else:
            self.sgn.emit(1)
