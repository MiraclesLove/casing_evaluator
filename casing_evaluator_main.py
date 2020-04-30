# -*- codingg:utf8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
from casing_evaluator import Ui_MainWindow
import sys
import io
import numpy as np
import pandas as pd
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
        self.pushButton_9.clicked.connect(self.generate_results_from_tableWidget_4)

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
        self.mat_view = Matplot_class(fileDir)  # 关键一步，创建Matplot_class类对象

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
        # 读取文件中的数值
        data = pd.read_excel('temp.xlsx', index=False)
        self.start_Depth = data.loc[0, 'value']
        self.end_Depth = data.loc[1, 'value']
        self.critical_Depth = data.loc[2, 'value']
        self.min_Diameter = data.loc[3, 'value']
        self.ave_Diameter = data.loc[4, 'value']
        self.max_Diameter = data.loc[5, 'value']
        # self.table.cellChanged.disconnect()
        self.row_tableWidget_4 = self.tableWidget_4.rowCount()
        self.tableWidget_4.setRowCount(self.row_tableWidget_4 + 1)
        # 添加表格数据
        self.tableWidget_4.setItem(self.row_tableWidget_4, 0, QTableWidgetItem(str(self.start_Depth)))
        self.tableWidget_4.setItem(self.row_tableWidget_4, 1, QTableWidgetItem(str(self.end_Depth)))
        self.tableWidget_4.setItem(self.row_tableWidget_4, 2, QTableWidgetItem(str(self.critical_Depth)))
        self.tableWidget_4.setItem(self.row_tableWidget_4, 3, QTableWidgetItem(str(self.min_Diameter)))
        self.tableWidget_4.setItem(self.row_tableWidget_4, 4, QTableWidgetItem(str(self.ave_Diameter)))
        self.tableWidget_4.setItem(self.row_tableWidget_4, 5, QTableWidgetItem(str(self.max_Diameter)))

    def delete_line_for_tableWidget_4(self):
        # self.table.cellChanged.disconnect()
        self.row = self.tableWidget_4.rowCount()
        self.tableWidget_4.setRowCount(self.row - 1)

    def generate_results_from_tableWidget_4(self):
        self.row_tableWidget_4 = self.tableWidget_4.rowCount()

        text_all = ''
        data = pd.DataFrame({'变形井段(m)': '',
                             '变形长度(m)': '',
                             '最大变形点深度(m)': '',
                             '最小内径(mm)': '',
                             '平均内径(mm)': '',
                             '最大内径(mm)': '',
                             '变形量(mm)': '',
                             '变形程度(%)': '',
                             '变形级别': ''},
                            index=[1])
        for row in range(0, self.row_tableWidget_4):
            inner_Diameter = self.lineEdit_2.text()
            inner_Diameter = float(inner_Diameter)
            thickness = self.lineEdit_3.text()
            thickness = float(thickness)

            well_interval = ''.join([self.tableWidget_4.item(row, 0).text(), '-', self.tableWidget_4.item(row, 1).text()])
            transformation_length = round(
                float(self.tableWidget_4.item(row, 1).text()) - float(self.tableWidget_4.item(row, 0).text()), 2)
            transformation_value = max(float(inner_Diameter - float(self.tableWidget_4.item(row, 3).text())),
                                       float(float(self.tableWidget_4.item(row, 5).text()) - inner_Diameter))
            transformation_value = round(transformation_value, 2)
            transformation_degree = round(transformation_value / inner_Diameter * 100, 2)

            # 变形级别判定
            if transformation_length > 10:
                if transformation_degree <= 5:
                    transformation_describe = '一级变形'
                elif 5 < transformation_degree <= 10:
                    transformation_describe = '二级变形'
                elif 10 < transformation_degree <= 20:
                    transformation_describe = '三级变形'
                elif 20 < transformation_degree <= 40:
                    transformation_describe = '四级变形'
                elif 40 < transformation_degree:
                    transformation_describe = '五级变形'
            elif transformation_length <= 10:
                if transformation_degree <= 10:
                    transformation_describe = '一级变形'
                elif 10 < transformation_degree <= 20:
                    transformation_describe = '二级变形'
                elif 20 < transformation_degree <= 40:
                    transformation_describe = '三级变形'
                elif 40 < transformation_degree <= 60:
                    transformation_describe = '四级变形'
                elif 60 < transformation_degree:
                    transformation_describe = '五级变形'

            data_single_layer = pd.DataFrame({'变形井段(m)': well_interval,
                                              '变形长度(m)': str(transformation_length),
                                              '最大变形点深度(m)': self.tableWidget_4.item(row, 2).text(),
                                              '最小内径(mm)': self.tableWidget_4.item(row, 3).text(),
                                              '平均内径(mm)': self.tableWidget_4.item(row, 4).text(),
                                              '最大内径(mm)': self.tableWidget_4.item(row, 5).text(),
                                              '变形量(mm)': str(transformation_value),
                                              '变形程度(%)': str(transformation_degree),
                                              '变形级别': str(transformation_describe)},
                                             index=[1])
            data = pd.concat([data, data_single_layer], ignore_index=True)
            text = ''.join(['    井段', well_interval, 'm，存在套管变形特征，变形长度为', str(transformation_length),\
                            'm，最大变形点深度为', self.tableWidget_4.item(row, 2).text(), 'm，测量最小内径为', \
                            self.tableWidget_4.item(row, 3).text(), 'mm，测量平均内径为', self.tableWidget_4.item(row, 4).text(), \
                            'mm，测量最大内径为', self.tableWidget_4.item(row, 5).text(), 'mm，最大变形量为', str(transformation_value), \
                            'mm，变形程度为', str(transformation_degree), '%，根据解释标准评价为', str(transformation_describe), '。\n'])
            text_all = ''.join([text_all, text])
        data.drop([0], inplace=True)
        print(data)
        writer = pd.ExcelWriter('变形评价表.xlsx')
        data.to_excel(writer, 'Sheet1')
        writer.save()

        #生成描述建议
        self.textEdit_3.setText(text_all)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
