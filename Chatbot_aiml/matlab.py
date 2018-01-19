import calcUi
import fractions
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sys import argv
from math import pi,e,sin,cos,tan,factorial as fact,degrees as de,sqrt,log, exp
class cal(QWidget,calcUi.Ui_Form):
    def __init__(self):
        super(cal,self).__init__()
        self.setupUi(self)
        self.tr=[]
        self.ind=0
        self.nu=1
        self.temp=fr(0,self.ws)
        self.temp.sgn.connect(self.changeIndex)
        self.tr.append(self.temp)
        #self.tr.setStyleSheet('background-color:green')
        self.tr[self.ind].setGeometry(50,50,self.tr[self.ind].width()+10,40)
        self.tr[self.ind].line()
        self.one.clicked.connect(lambda :self.m(1))
        self.two.clicked.connect(lambda : self.m(2))
        self.three.clicked.connect(lambda : self.m(3))
        self.four.clicked.connect(lambda : self.m(4))
        self.five.clicked.connect(lambda : self.m(5))
        self.six.clicked.connect(lambda : self.m(6))
        self.seven.clicked.connect(lambda : self.m(7))
        self.eight.clicked.connect(lambda : self.m(8))
        self.nine.clicked.connect(lambda : self.m(9))
        self.zero.clicked.connect(lambda : self.m(0))
        self.back.clicked.connect(lambda : self.m('back'))
        self.mod.clicked.connect(lambda : self.m('mod'))
        self.cancel.clicked.connect(lambda : self.m('cancel'))
        self.sin.clicked.connect(lambda : self.m('sin'))
        self.cos.clicked.connect(lambda: self.m('cos'))
        self.tan.clicked.connect(lambda: self.m('tan'))
        self.add.clicked.connect(lambda : self.m('+'))
        self.minus.clicked.connect(lambda: self.m('-'))
        self.div.clicked.connect(lambda: self.m('/'))
        self.mul.clicked.connect(lambda: self.m('*'))
        self.fact.clicked.connect(lambda: self.m('fact'))
        self.pi.clicked.connect(lambda: self.m('pi'))
        self.e.clicked.connect(lambda: self.m('e'))
        self.rBrace.clicked.connect(lambda : self.m('('))
        self.lBrace.clicked.connect(lambda: self.m(')'))
        self.dec.clicked.connect(lambda: self.m('.'))
        self.enter.clicked.connect(lambda: self.m('enter'))
        self.deg.clicked.connect(lambda: self.m('deg'))
        self.ra.clicked.connect(lambda: self.m('ra'))
        self.sq.clicked.connect(lambda: self.m('sq'))
        self.loge.clicked.connect(lambda: self.m('ln'))
        self.pushButton_21.clicked.connect(lambda: self.m('exp'))
        self.pushButton_29.clicked.connect(lambda: self.m('i'))
        self.opBrace=[0]
        #self.entry.textChanged.connect(lambda:self.eva(self.entry.text()))
        self.entry.textEdited.connect(lambda:self.change(self.entry.text()))
        self.show()
    def prr(self):
        print("HI")
    def changeIndex(self,i):
        self.ind=i
        self.entry.setText(self.tr[self.ind].l.text().split(' =')[0])
    def m(self,st):
        l=self.entry.text()
        i=self.entry.cursorPosition()
        flag=0
        if st in [0,1,2,3,4,5,6,7,8,9]:
            if l and l[i-1] == ')':
                self.entry.setText(l[:i]+'*'+str(st)+l[i:])
                self.entry.setCursorPosition(i + 2)
                self.eva(self.entry.text())
            else:
                self.entry.setText(l[:i] + str(st) + l[i:])
                self.entry.setCursorPosition(i + 1)
                self.eva(self.entry.text())
            flag=1

        elif st in ['+','-','*','/']:
            self.entry.setText(l[:i]+st+l[i:])
            self.entry.setCursorPosition(i + 1)
        elif st=='back':
            if l:
                if l[-1]=='(':
                    self.opBrace[self.ind]-=1
                elif l[-1]==')':
                    self.opBrace[self.ind]+=1
                self.entry.setText(l[:i-1]+l[i:])
                if not self.entry.text():
                    flag=0
                else:
                    flag=2
                self.entry.setCursorPosition(i-1)
            else:
                flag=0
        elif st=='mod':
            self.opBrace[self.ind] += 1
            if l and l[i-1] not in ['+','-','*','/']:
                self.entry.setText(l[:i] + '*abs(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:

                self.entry.setText(l[:i]+'abs('+l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st=='cancel':
            self.entry.clear()
            self.tr[self.ind].l.clear()
            self.opBrace[self.ind]=0
            self.tr[self.ind].resize(40, self.tr[self.ind].height())
            self.tr[self.ind].l1.setGeometry(5, 1, 15, 5)
            self.tr[self.ind].l2.setGeometry(1, 5, 5, 15)
            self.tr[self.ind].l3.setGeometry(5, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l4.setGeometry(1, self.tr[self.ind].height() - 17, 5, 15)
            self.tr[self.ind].l5.setGeometry(self.tr[self.ind].width() - 17, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l7.setGeometry(self.tr[self.ind].width() - 17, 1, 15, 5)
            self.tr[self.ind].l8.setGeometry(self.tr[self.ind].width() - 3, 5, 5, 15)
            self.tr[self.ind].l.resize(40, self.tr[self.ind].l.height())
            flag=3
        elif st=='.':
            self.entry.setText(l[:i] + '.' + l[i:])
            self.entry.setCursorPosition(i + 1)

        elif st=='sin':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*sin(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:
                self.entry.setText(l[:i] + 'sin(' + l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st=='cos':
            self.opBrace[self.ind]+= 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*cos(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:
                self.entry.setText(l[:i] + 'cos(' + l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st == 'tan':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*tan(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:
                self.entry.setText(l[:i] + 'tan(' + l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st=='fact':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*fact(' + l[i:])
                self.entry.setCursorPosition(i + 6)
            else:
                self.entry.setText(l[:i] + 'fact(' + l[i:])
                self.entry.setCursorPosition(i + 5)
        elif st=='exp':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*exp(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:
                self.entry.setText(l[:i] + 'exp(' + l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st=='pi':
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*pi' + l[i:])
                self.entry.setCursorPosition(i + 3)
            else:
                self.entry.setText(l[:i] + 'pi' + l[i:])
                self.entry.setCursorPosition(i + 2)
            self.eva(self.entry.text())
            flag = 1
        elif st=='i':
            if l and l[i-1] not in ['1','2','3','4','5','6','7','8','9','0']:
                self.entry.setText(l[:i]+'1j'+l[i:])
                self.entry.setCursorPosition(i+2)
            else:
                self.entry.setText(l[:i] + 'j' + l[i:])
                self.entry.setCursorPosition(i + 1)

            self.eva(self.entry.text())
            flag=1
        elif st=='e':
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*e' + l[i:])
                self.entry.setCursorPosition(i + 2)
            else:
                self.entry.setText(l[:i] + 'e' + l[i:])
                self.entry.setCursorPosition(i + 1)
            self.eva(self.entry.text())
            flag = 1
        elif st=='(':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*(' + l[i:])
                self.entry.setCursorPosition(i + 2)
            else:
                self.entry.setText(l[:i] + '(' + l[i:])
                self.entry.setCursorPosition(i + 1)
        elif st==')':
            self.opBrace[self.ind]-=1
            self.entry.setText(self.entry.text()[:i] + ')' + self.entry.text()[i:])
            self.entry.setCursorPosition(i + 1)
            self.eva(self.entry.text())
            flag = 1
        elif st=='deg':
            self.opBrace[self.ind] += 1
            self.entry.setText(l[:i] + 'de(' + l[i:])
            self.entry.setCursorPosition(i + 3)
        elif st=='ra':
            self.entry.setText(l[:i] + '^' + l[i:])
            self.entry.setCursorPosition(i + 1)

        elif st=='sq':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*sqrt(' + l[i:])
                self.entry.setCursorPosition(i + 6)
            else:
                self.entry.setText(l[:i] + 'sqrt(' + l[i:])
                self.entry.setCursorPosition(i + 5)
        elif st=='ln':
            self.opBrace[self.ind] += 1
            if l and l[i - 1] not in ['+', '-', '*', '/','(']:
                self.entry.setText(l[:i] + '*log(' + l[i:])
                self.entry.setCursorPosition(i + 5)
            else:
                self.entry.setText(l[:i] + 'log(' + l[i:])
                self.entry.setCursorPosition(i + 4)
        elif st=='enter':
            self.entry.clear()
            self.temp = fr(self.nu, self.ws)
            self.ind=self.nu
            self.nu += 1
            self.temp.sgn.connect(self.changeIndex)
            self.tr.append(self.temp)
            self.opBrace.append(0)
            self.tr[self.ind].setGeometry(100, 50, self.tr[self.ind].width() + 10, 40)
            self.tr[self.ind].line()
        if flag==0:
            self.pr(self.entry.text())
        elif flag==2:
            self.eva(self.entry.text())
    def change(self,st):
        if not st:
            self.pr(st)
            self.opBrace[self.ind]=0
        else:
            l=st.count('(')-st.count(')')
            self.opBrace[self.ind]=l
            self.eva(st)
    def pr(self,st):
        if not st:
            self.tr[self.ind].resize(40, self.tr[self.ind].height())
            self.tr[self.ind].l.resize(40, self.tr[self.ind].l.height())
        else:
            self.tr[self.ind].resize(len(st) * 12, self.tr[self.ind].height())
            self.tr[self.ind].l.resize(len(st) * 11, self.tr[self.ind].l.height())
        self.tr[self.ind].l1.setGeometry(5, 1, 15, 5)
        self.tr[self.ind].l2.setGeometry(1, 5, 5, 15)
        self.tr[self.ind].l3.setGeometry(5, self.tr[self.ind].height() - 3, 15, 5)
        self.tr[self.ind].l4.setGeometry(1, self.tr[self.ind].height() - 17, 5, 15)
        self.tr[self.ind].l5.setGeometry(self.tr[self.ind].width() - 17, self.tr[self.ind].height() - 3, 15, 5)
        self.tr[self.ind].l6.setGeometry(self.tr[self.ind].width() - 3, self.tr[self.ind].height() - 17, 5, 15)
        self.tr[self.ind].l7.setGeometry(self.tr[self.ind].width() - 17, 1, 15, 5)
        self.tr[self.ind].l8.setGeometry(self.tr[self.ind].width() - 3, 5, 5, 15)
        self.tr[self.ind].l.setText(st)
    def eva(self,st):
        c=''
        if self.opBrace[self.ind]>0:
            asdflkj=st.lstrip('0')+')'*self.opBrace[self.ind]
            c=asdflkj.replace('^','**')
        else:
            asdflkj = st.lstrip('0')
            c=asdflkj.replace('^', '**')
        try:
            l=asdflkj+' = '+str(eval(c))
            self.tr[self.ind].resize(len(l)*8,self.tr[self.ind].height())
            self.tr[self.ind].l1.setGeometry(5, 1, 15, 5)
            self.tr[self.ind].l2.setGeometry(1, 5, 5, 15)
            self.tr[self.ind].l3.setGeometry(5, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l4.setGeometry(1, self.tr[self.ind].height() - 17, 5, 15)
            self.tr[self.ind].l5.setGeometry(self.tr[self.ind].width() - 17, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l6.setGeometry(self.tr[self.ind].width() - 3, self.tr[self.ind].height() - 17, 5, 15)
            self.tr[self.ind].l7.setGeometry(self.tr[self.ind].width() - 17, 1, 15, 5)
            self.tr[self.ind].l8.setGeometry(self.tr[self.ind].width() - 3, 5, 5, 15)
            self.tr[self.ind].l.resize(len(l)*7.5,self.tr[self.ind].l.height())
            self.tr[self.ind].l.setText(l)
        except Exception as e:
            self.tr[self.ind].resize(len(st) * 12, self.tr[self.ind].height())
            self.tr[self.ind].l1.setGeometry(5, 1, 15, 5)
            self.tr[self.ind].l2.setGeometry(1, 5, 5, 15)
            self.tr[self.ind].l3.setGeometry(5, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l4.setGeometry(1, self.tr[self.ind].height() - 17, 5, 15)
            self.tr[self.ind].l5.setGeometry(self.tr[self.ind].width() - 17, self.tr[self.ind].height() - 3, 15, 5)
            self.tr[self.ind].l6.setGeometry(self.tr[self.ind].width() - 3, self.tr[self.ind].height() - 17, 5, 15)
            self.tr[self.ind].l7.setGeometry(self.tr[self.ind].width() - 17, 1, 15, 5)
            self.tr[self.ind].l8.setGeometry(self.tr[self.ind].width() - 3, 5, 5, 15)
            self.tr[self.ind].l.resize(len(st) * 11, self.tr[self.ind].l.height())
            self.tr[self.ind].l.setText(st)
            print(e)
class fr(QFrame):
    sgn=pyqtSignal(int)
    def __init__(self,ind,parent=None):
        super(fr,self).__init__(parent)
        self.index=ind
        self.l = QLabel(self)
        self.l.resize(5*7.5, 30)
        self.l.move(5,5)
        self.l.setStyleSheet('font-size:10pt;background-color:rgba(255,255,255,0);border-radius: 2px;border-color:rgba(255,255,255,0)')
        self.l1=""
        self.l2=""
        self.l3 = ""
        self.l4 = ""
        self.l5 = ""
        self.l6 = ""
        self.l7 = ""
        self.l8 = ""

    def line(self):
        self.l1 = QFrame(self)
        self.l1.setFrameShape(QFrame.HLine)
        self.l1.setGeometry(5, 1, 15, 5)
        self.l1.setStyleSheet('color:blue')
        self.l2 = QFrame(self)
        self.l2.setFrameShape(QFrame.VLine)
        self.l2.setGeometry(1, 5, 5, 15)
        self.l2.setStyleSheet('color:blue')
        self.l3 = QFrame(self)
        self.l3.setFrameShape(QFrame.HLine)
        self.l3.setGeometry(5, self.height() - 3, 15, 5)
        self.l3.setStyleSheet('color:blue')

        self.l4 = QFrame(self)
        self.l4.setFrameShape(QFrame.VLine)
        self.l4.setGeometry(1, self.height()-17, 5, 15)
        self.l4.setStyleSheet('color:blue')

        self.l5 = QFrame(self)
        self.l5.setFrameShape(QFrame.HLine)
        self.l5.setGeometry(self.width()-17, self.height()-3, 15, 5)
        self.l5.setStyleSheet('color:blue')
        self.l6 = QFrame(self)
        self.l6.setFrameShape(QFrame.VLine)
        self.l6.setGeometry(self.width()-3, self.height()-17, 5, 15)
        self.l6.setStyleSheet('color:blue')
        self.l7 = QFrame(self)
        self.l7.setFrameShape(QFrame.HLine)
        self.l7.setGeometry(self.width()-17, 1, 15, 5)
        self.l7.setStyleSheet('color:blue')
        self.l8 = QFrame(self)
        self.l8.setFrameShape(QFrame.VLine)
        self.l8.setGeometry(self.width()-3, 5, 5, 15)
        self.l8.setStyleSheet('color:blue')
        self.show()
        #self.l.setReadOnly(True)
    def mousePressEvent(self, event):
        self.mpos=event.pos()
        self.sgn.emit(self.index)
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            diff=event.pos()-self.mpos
            newpos=self.pos()+diff
            if newpos.x()>0 and newpos.x()+self.width()<391:
                if newpos.y()>30 and newpos.y()+self.height()//2<201:
                    self.move(newpos)
                elif newpos.y()<=30:
                    self.move(QPoint(newpos.x(),31))
                else:
                    self.move(QPoint(newpos.x(), 201-self.height()//2))
            elif newpos.x()<=0:
                if newpos.y()>30 and newpos.y()+self.height()//2<180:
                    self.move(QPoint(1,newpos.y()))
                elif newpos.y()<=30:
                    self.move(QPoint(1,31))
                else:
                    self.move(QPoint(1, 201-self.height()//2))
            else:
                if newpos.y()>30 and newpos.y()+self.height()//2<180:
                    self.move(QPoint(391-self.width(),newpos.y()))
                elif newpos.y()<=30:
                    self.move(QPoint(391-self.width(),31))
                else:
                    self.move(QPoint(391-self.width(), 201-self.height()//2))

if __name__ == '__main__':
    app=QApplication(argv)
    master=cal()
    app.exec_()