import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
         super().__init__()
         self.setupUi(self)

         self.timer = QTimer(self)
         self.timer.start(1000)
         self.timer.timeout.connect(self.timeout)
     # # 이벤트 처리 코드
    def btn_clicked(self):
         price = pykorbit.get_current_price("BTC")
         self.lineEdit.setText(str(price))

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

# QApplication 객체 생성 및 이벤트 루프 생성 코드
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




