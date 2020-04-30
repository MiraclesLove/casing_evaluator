# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Worker(QThread):
    x = pyqtSignal(int)
    y = pyqtSignal(int)

    def run(self):
        for i in range(10):
            print('第 %d 次' % i)
            self.x.emit(i)
            k = False
            if k is True:
                print("成功！！！")
                # self.y.emit(i)
            self.sleep(1)
        pass


class MainWidget(QWidget):
    def __init__(self, parent=None):
        global k
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("是否进行？")
        self.setMinimumSize(400, 300)
        self.thread = Worker()
        self.line = QLabel()
        self.btn1 = QPushButton('YES')
        self.btn2 = QPushButton('NO')
        layout = QGridLayout(self)
        layout.addWidget(self.line, 0, 0, 1, 2)
        layout.addWidget(self.btn1, 1, 0)
        layout.addWidget(self.btn2, 1, 1)
        self.th = Worker(self)
        self.btn1.clicked.connect(self.slotStart)
        self.btn2.clicked.connect(self.slotJump)

    def slotStart(self):
        self.th.x.connect(self.ShowX)
        # th.y.connect(self.ShowY)
        self.th.start()

    def slotJump(self):
        global k
        # self.th.wait()
        self.k = True

    def ShowX(self, i):
        self.line.setText("第%d" % i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = MainWidget()
    test.show()
    sys.exit(app.exec_())