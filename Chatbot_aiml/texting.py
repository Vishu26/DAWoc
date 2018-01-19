from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from screen import Ui_chatBot, model
from gtts import gTTS
from chat import kernel
from random import choice
from matlab import cal
import webbrowser
import os
from weather import Weather

w = Weather()

di = {'FRENCH':'fr', 'GERMAN':'de', 'HINDI':'hi', 'ITALIAN':'it', 'SPANISH':'es', 'GREEK':'el'}

class master(QWidget, Ui_chatBot):
    def __init__(self):
        super(master, self).__init__()
        self.setupUi(self)
        self.tran = False
        self.lan = None
        self.send.clicked.connect(self.compute)
        self.show()

    def compute(self):
        a = self.userText.toPlainText().strip()
        self.userText.clear()
        self.prevText.setReadOnly(False)
        self.prevText.clear()
        self.prevText.setText(a)
        self.prevText.setReadOnly(True)

        if self.tran:
            st = model.translate(a, src='en', dest=self.lan)
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText(st.text)
            if not self.sound.isChecked():
                speak = thread(st.text, lang=self.lan)
                speak.run()
            self.chatbotText.setReadOnly(True)
            self.tran = False

        elif not a:
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText(''.join(choice(['Was that a typo?',
                                  "I am afraid, I can't understand",
                                  'Am I overfitted on data?, coz I can\'t get that one!',
                                  'Correct your grammar probably?'])))
            self.chatbotText.setReadOnly(True)
        elif a.upper().startswith('SPELL'):
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText(a[6:])
            if not self.sound.isChecked():
                speak = thread(a[6:])
                speak.run()
            self.chatbotText.setReadOnly(True)

        elif a.upper().startswith('SEARCH'):
            webbrowser.open('https://www.google.com.tr/search?q={}'.format(a[7:]))
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('Searching...')
            if not self.sound.isChecked():
                speak = thread('Searching...')
                speak.run()
            self.chatbotText.setReadOnly(True)
        elif a.upper().startswith('OPEN'):
            webbrowser.open('https://www.{}.com'.format(a[5:].lstrip('https://www.').rstrip('.com').rstrip('.in').rstrip('.co.in').rstrip('.org')))
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('Searching...')
            if not self.sound.isChecked():
                speak = thread('Searching...')
                speak.run()
            self.chatbotText.setReadOnly(True)

        elif 'WEATHER' in a.upper():
            b = w.lookup_by_location(location='ahmedabad').atmosphere()
            c = w.lookup_by_location(location='ahmedabad').condition()

            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText(c.text()+','+'temperature is '+c.temp()+' F,'+'humidity is '+b['humidity']+'%')
            if not self.sound.isChecked():
                speak = thread(c.text()+','+'temperature is '+c.temp()+' F,'+'humidity is '+b['humidity']+'%')
                speak.run()
            self.chatbotText.setReadOnly(True)

        elif a.upper().startswith('IMAGE') or a.upper().startswith('PICTURE') or a.upper().startswith('PHOTO'):
            webbrowser.open("https://www.google.com/search?tbm=isch&source=hp&biw=1280&bih=642&ei=nGNiWq-ZBozJvgSjtKS4DA&q={}".format('+'.join(a.split()[2:])))
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('Searching...')
            if not self.sound.isChecked():
                speak = thread('Searching...')
                speak.run()
            self.chatbotText.setReadOnly(True)

        elif a.upper().startswith('TRANSLATE'):
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('Type the sentence...')
            if not self.sound.isChecked():
                speak = thread('Type the sentence...')
                speak.run()
            self.chatbotText.setReadOnly(True)
            self.tran = True
            self.lan = di[a.upper().split()[2]]

        elif a.upper().startswith('CALC'):
            calc = cal()
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText('There You GO...')
            if not self.sound.isChecked():
                speak = thread('There You GO...')
                speak.run()
            self.chatbotText.setReadOnly(True)

        else:
            ans = kernel.respond(a.upper())
            self.chatbotText.setReadOnly(False)
            self.chatbotText.clear()
            self.chatbotText.setText(ans)
            if not self.sound.isChecked():
                speak = thread(ans)
                QCoreApplication.processEvents()
                speak.run()
                QCoreApplication.processEvents()
            self.chatbotText.setReadOnly(True)

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