from PyQt5 import QtCore, QtGui, QtWidgets
from actualScreen import Ui_screen, model
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from gtts import gTTS
from chat import kernel
from random import choice
from matlab import cal
import webbrowser
import os
from selenium import webdriver
from weather import Weather

w = Weather()

di = {'FRENCH':'fr', 'GERMAN':'de', 'HINDI':'hi', 'ITALIAN':'it', 'SPANISH':'es', 'GREEK':'el'}

class master(QWidget, Ui_screen):
    def __init__(self):
        super(master, self).__init__()
        self.setupUi(self)
        self.user1 = None
        self.user2 = None
        self.bot1 = None
        self.bot2 = None
        self.tran = False
        self.cmdList.currentIndexChanged.connect(self.cmd)
        self.lan = None
        self.send.clicked.connect(self.compute)
        self.lay.addWidget(QLabel(''))
        self.show()
    def cmd(self):
        a = self.cmdList.currentText()
        print(a)
        if self.cmdList.currentIndex()!=0:
            self.userText.clear()
            self.userText.setPlainText(a)

    def compute(self):

        a = self.userText.toPlainText().strip()
        self.userText.clear()
        if self.user1 and self.user2:
            self.user1.hide()
            self.user2.hide()
            self.bot1.hide()
            self.bot2.hide()
            self.user1 = None
            self.user2 = None
            self.bot1 = None
            self.bot2 = None
            self.user1 = user()
            self.user1.inputText.setReadOnly(False)
            if a.upper().startswith('CHECK WEBMAIL'):
                p = a.split()
                self.user1.inputText.setPlainText(' '.join(p[:3])+' ********')
            else:
                self.user1.inputText.setPlainText(a)
            self.user1.inputText.setReadOnly(True)
            self.lay.addWidget(self.user1)

        elif self.user1:
            self.user2 = user()
            self.user2.inputText.setReadOnly(False)
            if a.upper().startswith('CHECK WEBMAIL'):
                p = a.split()
                self.user2.inputText.setPlainText(' '.join(p[:3])+' ********')
            else:
                self.user2.inputText.setPlainText(a)
            self.user2.inputText.setReadOnly(True)
            self.lay.addWidget(self.user2)
            self.user2.show()
        else:
            self.user1 = user()
            self.user1.inputText.setReadOnly(False)
            if a.upper().startswith('CHECK WEBMAIL'):
                p = a.split()
                self.user1.inputText.setPlainText(' '.join(p[:3])+' ********')
            else:
                self.user1.inputText.setPlainText(a)
            self.user1.inputText.setReadOnly(True)
            self.lay.addWidget(self.user1)
            self.user1.show()

        if self.tran:
            st = model.translate(a, src='en', dest=self.lan)
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText(st.text)
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText(st.text)
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            if not self.sound.isChecked():
                speak = thread(st.text, lang=self.lan)
                speak.run()
            self.tran = False

        elif a.upper().startswith('SAY'):
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText(a[4:])
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText(a[4:])
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)

            if not self.sound.isChecked():
                speak = thread(a[4:])
                speak.run()

        elif a.upper().startswith('SEARCH'):
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText('Searching...')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText('Searching...')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            webbrowser.open('https://www.google.com.tr/search?q={}'.format(a[7:]))
            '''if not self.sound.isChecked():
                speak = thread('Searching...')
                speak.run()'''

        elif a.upper().startswith('OPEN'):
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText('Searching...')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText('Searching...')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            webbrowser.open('https://{}'.format(a[5:]))

        elif a.upper().startswith('CHECK WEBMAIL'):
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText('Fetching...')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText('Fetching...')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            a = a.split()
            web = webdriver.Chrome()
            web.get('https://webmail.daiict.ac.in')
            web.find_element_by_id('username').send_keys(a[2])
            web.find_element_by_id('password').send_keys(a[3])
            web.find_element_by_xpath("//input[@type='submit']").click()

            '''if not self.sound.isChecked():
                speak = thread('Fetching...')
                speak.run()'''

        elif 'WEATHER' in a.upper():
            b = w.lookup_by_location(location='ahmedabad').atmosphere()
            c = w.lookup_by_location(location='ahmedabad').condition()
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText(c.text() + ',' + 'temperature is ' + c.temp() + ' F,' + 'humidity is ' + b['humidity'] + '%')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText(c.text() + ',' + 'temperature is ' + c.temp() + ' F,' + 'humidity is ' + b['humidity'] + '%')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)

            if not self.sound.isChecked():
                speak = thread(
                    c.text() + ',' + 'temperature is ' + c.temp() + ' F,' + 'humidity is ' + b['humidity'] + '%')
                speak.run()

        elif a.upper().startswith('IMAGE') or a.upper().startswith('PICTURE') or a.upper().startswith('PHOTO'):
            webbrowser.open(
                "https://www.google.com/search?tbm=isch&source=hp&biw=1280&bih=642&ei=nGNiWq-ZBozJvgSjtKS4DA&q={}".format(
                    '+'.join(a.split()[2:])))
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('Searching...')
            if not self.sound.isChecked():
                speak = thread('Searching...')
                speak.run()
            self.chatbotText.setReadOnly(True)

        elif a.upper().startswith('TRANSLATE'):
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText('Type the sentence...')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText('Type the sentence...')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            if not self.sound.isChecked():
                speak = thread('Type the sentence...')
                speak.run()
            self.tran = True
            self.lan = di[a.upper().split()[2]]

        elif a.upper().startswith('CALC'):

            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText('There You GO...')
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText('There You GO...')
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
            calc = cal()
            if not self.sound.isChecked():
                speak = thread('There You GO...')
                speak.run()

        else:
            ans = kernel.respond(a.upper())
            print(ans)
            if self.bot1:
                self.bot2 = bot()
                self.bot2.inputText.setReadOnly(False)
                self.bot2.inputText.setPlainText(ans)
                self.bot2.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot2)
            else:
                self.bot1 = bot()
                self.bot1.inputText.setReadOnly(False)
                self.bot1.inputText.setPlainText(ans)
                self.bot1.inputText.setReadOnly(True)
                self.lay.addWidget(self.bot1)
                self.bot1.inputText.show()
            if not self.sound.isChecked():
                speak = thread(ans)
                QCoreApplication.processEvents()
                speak.run()
                QCoreApplication.processEvents()
        self.cmdList.setCurrentIndex(0)


class user(QWidget):
    def __init__(self):
        super(user, self).__init__()
        self.userr = QLabel(self)
        self.userr.setGeometry(480, 20, 50, 50)
        self.userr.setText("")
        self.userr.setPixmap(QPixmap("user.png"))
        self.userr.setScaledContents(True)
        self.userr.show()
        self.inputText = QPlainTextEdit(self)
        self.inputText.setGeometry(30, 17, 401, 61)
        self.inputText.setStyleSheet("background-color:rgba(220,220,220,0.4);border-radius:2px;font-size:16pt;")
        self.inputText.setReadOnly(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(434, 40, 41, 21)
        self.label.setText("")
        self.label.setPixmap(QPixmap("dash.png"))
        self.label.setScaledContents(True)


class bot(QWidget):
    def __init__(self):
        super(bot, self).__init__()
        self.userr = QLabel(self)
        self.userr.setGeometry(10, 20, 60, 51)
        self.userr.setText("")
        self.userr.setPixmap(QPixmap("bot.png"))
        self.userr.setScaledContents(True)
        self.userr.show()
        self.inputText = QPlainTextEdit(self)
        self.inputText.setGeometry(120, 17, 401, 61)
        self.inputText.setStyleSheet("background-color:rgba(30,144,255,0.4);border-radius:2px;font-size:16pt;color:white")
        self.inputText.setReadOnly(True)
        self.inputText.show()
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(74, 40, 41, 21)
        self.label.setText("")
        self.label.setPixmap(QPixmap("dash.png"))
        self.label.setScaledContents(True)
        self.label.show()

class thread(QThread):
    def __init__(self, st, lang='en'):
        super(thread, self).__init__()
        self.st = st
        self.lang = lang
    def run(self):
        QCoreApplication.processEvents()
        sp = gTTS(text=self.st, lang=self.lang, slow=False)
        sp.save('text.mp3')
        os.system('mplayer text.mp3')

if __name__ == '__main__':
    app = QApplication(argv)
    main = master()
    app.exec_()