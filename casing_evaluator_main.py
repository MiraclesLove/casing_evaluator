# -*- codingg:utf8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
from casing_evaluator import Ui_MainWindow
import sys
import io
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, MultiCursor, RadioButtons, Button
import matplotlib.font_manager as fm
import las
from casing_evaluator_matplotlib import Matplot_class


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.id = 1
        self.lines = []
        self.editable = True
        self.des_sort = True
        self.table2()
        self.table3()
        self.table4()

        self.pushButton_5.clicked.connect(self.add_line_for_tableWidget_4)
        self.pushButton_6.clicked.connect(self.delete_line_for_tableWidget_4)

        self.pushButton_12.clicked.connect(self.openLasFiles)
        self.pushButton_13.clicked.connect(self.readLasFiles)

    def openLasFiles(self):
        fnames = QFileDialog.getOpenFileNames(self, '打开LAS文件', './')  # 注意这里返回值是元组
        if fnames[0]:
            for fname in fnames[0]:
                self.textEdit_4.append(fname)

    def readLasFiles(self):
        fileDir = self.textEdit_4.toPlainText()
        fileDir = fileDir.replace('file:///', '')

        # 解决中文乱码问题
        # myfont = fm.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)
        # matplotlib.rcParams["axes.unicode_minus"] = False
        # 读取las数据
        # log = las.LASReader(u'ning209H19-4_resample_jz.LAS', null_subs=np.nan)
        log = las.LASReader(fileDir, null_subs=np.nan)
        self.mat_view = Matplot_class(fileDir)#关键一步，创建Matplot_class类对象


    def table2(self):
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(6)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem('起始深度(m)'))
        self.tableWidget_2.setItem(0, 2, QTableWidgetItem('结束深度(m)'))
        self.tableWidget_2.setItem(0, 3, QTableWidgetItem('最大损伤点深度(m)'))
        self.tableWidget_2.setItem(0, 4, QTableWidgetItem('测量臂号数'))
        self.tableWidget_2.setItem(0, 5, QTableWidgetItem('最小内径(mm)'))
        self.tableWidget_2.setItem(0, 6, QTableWidgetItem('平均内径(mm)'))
        self.tableWidget_2.setItem(0, 7, QTableWidgetItem('最大内径(mm)'))

        self.tableWidget_2.setItem(row + 1, col, QTableWidgetItem('1'))
        self.tableWidget_2.setItem(row + 2, col, QTableWidgetItem('2'))

        self.tableWidget_2.setColumnWidth(0, 20)
        self.tableWidget_2.setColumnWidth(1, 80)
        self.tableWidget_2.setColumnWidth(2, 80)
        self.tableWidget_2.setColumnWidth(3, 110)
        self.tableWidget_2.setColumnWidth(4, 90)
        self.tableWidget_2.setColumnWidth(5, 90)

        self.tableWidget_2.setRowHeight(0, 50)
        self.tableWidget_2.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget_2.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def table3(self):
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.setRowCount(6)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        self.tableWidget_3.setItem(0, 1, QTableWidgetItem('起始深度(m)'))
        self.tableWidget_3.setItem(0, 2, QTableWidgetItem('结束深度(m)'))
        self.tableWidget_3.setItem(0, 3, QTableWidgetItem('最大结垢点深度(m)'))
        self.tableWidget_3.setItem(0, 4, QTableWidgetItem('测量臂号数'))
        self.tableWidget_3.setItem(0, 5, QTableWidgetItem('最小内径(mm)'))
        self.tableWidget_3.setItem(0, 6, QTableWidgetItem('平均内径(mm)'))
        self.tableWidget_3.setItem(0, 7, QTableWidgetItem('最大内径(mm)'))

        self.tableWidget_3.setItem(row + 1, col, QTableWidgetItem('1'))
        self.tableWidget_3.setItem(row + 2, col, QTableWidgetItem('2'))

        self.tableWidget_3.setColumnWidth(0, 20)
        self.tableWidget_3.setColumnWidth(1, 80)
        self.tableWidget_3.setColumnWidth(2, 80)
        self.tableWidget_3.setColumnWidth(3, 110)
        self.tableWidget_3.setColumnWidth(4, 90)
        self.tableWidget_3.setColumnWidth(5, 90)

        self.tableWidget_3.setRowHeight(0, 50)
        self.tableWidget_3.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget_3.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def table4(self):
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_4.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_4.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始深度(m)', '结束深度(m)', '最大变形点深度(m)', '最小内径(mm)', '平均内径(mm)', '最大内径(mm)']
        self.tableWidget_4.setHorizontalHeaderLabels(self.headers)

        self.tableWidget_4.setItem(row + 1, col, QTableWidgetItem('1'))
        self.tableWidget_4.setItem(row + 2, col, QTableWidgetItem('2'))

        self.tableWidget_4.setColumnWidth(0, 80)
        self.tableWidget_4.setColumnWidth(1, 80)
        self.tableWidget_4.setColumnWidth(2, 110)
        self.tableWidget_4.setColumnWidth(3, 90)
        self.tableWidget_4.setColumnWidth(4, 90)
        self.tableWidget_4.setColumnWidth(5, 90)

        # self.tableWidget_4.setRowHeight(0, 50)
        # self.tableWidget_4.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget_4.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def add_line_for_tableWidget_4(self):
        # self.table.cellChanged.disconnect()
        row = self.tableWidget_4.rowCount()
        self.tableWidget_4.setRowCount(row + 1)
        # 添加表格数据
        self.tableWidget_4.setItem(row, 0, QTableWidgetItem('3000'))
        self.tableWidget_4.setItem(row, 1, QTableWidgetItem('4000'))
        self.tableWidget_4.setItem(row, 2, QTableWidgetItem('3500'))
        self.tableWidget_4.setItem(row, 3, QTableWidgetItem('90'))
        self.tableWidget_4.setItem(row, 4, QTableWidgetItem('100'))
        self.tableWidget_4.setItem(row, 5, QTableWidgetItem('110'))

    def delete_line_for_tableWidget_4(self):
        # self.table.cellChanged.disconnect()
        row = self.tableWidget_4.rowCount()
        self.tableWidget_4.setRowCount(row - 1)

    def table5(self):
        self.tableWidget_5.setColumnCount(6)
        self.tableWidget_5.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_5.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_5.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始深度(m)', '结束深度(m)', '最大变形点深度(m)', '最小内径(mm)', '平均内径(mm)', '最大内径(mm)']
        self.tableWidget_5.setHorizontalHeaderLabels(self.headers)

        self.tableWidget_5.setItem(row + 1, col, QTableWidgetItem('1'))
        self.tableWidget_5.setItem(row + 2, col, QTableWidgetItem('2'))

        self.tableWidget_5.setColumnWidth(0, 80)
        self.tableWidget_5.setColumnWidth(1, 80)
        self.tableWidget_5.setColumnWidth(2, 110)
        self.tableWidget_5.setColumnWidth(3, 90)
        self.tableWidget_5.setColumnWidth(4, 90)
        self.tableWidget_5.setColumnWidth(5, 90)

        # self.tableWidget_4.setRowHeight(0, 50)
        # self.tableWidget_4.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget_4.horizontalHeader().setVisible(False)  # 隐藏水平表头

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())