# -*- coding:utf8 -*-
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
import xlrd, xlwt
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
        self.table_casing()
        # self.dateTimeEdit()
        # self.dateTimeEdit_2()

        # 打开解析LAS文件
        self.pushButton_12.clicked.connect(self.openLasFiles)
        self.pushButton_13.clicked.connect(self.readLasFiles)

        # 损伤评价按钮组
        self.pushButton.clicked.connect(self.add_line_for_tableWidget_2)
        self.pushButton_2.clicked.connect(self.delete_line_for_tableWidget_2)
        self.pushButton_7.clicked.connect(self.generate_results_from_tableWidget_2)

        # 结垢评价按钮组
        self.pushButton_4.clicked.connect(self.add_line_for_tableWidget_3)
        self.pushButton_3.clicked.connect(self.delete_line_for_tableWidget_3)
        self.pushButton_8.clicked.connect(self.generate_results_from_tableWidget_3)

        # 变形评价按钮组
        self.pushButton_5.clicked.connect(self.add_line_for_tableWidget_4)
        self.pushButton_6.clicked.connect(self.delete_line_for_tableWidget_4)
        self.pushButton_9.clicked.connect(self.generate_results_from_tableWidget_4)

        # 填写确认生成本地Excel文件
        self.pushButton_14.clicked.connect(self.add_line_for_tableWidget_5)
        self.pushButton_15.clicked.connect(self.delete_line_for_tableWidget_5)
        self.pushButton_16.clicked.connect(self.casing_info_save)

    def openLasFiles(self):
        fnames = QFileDialog.getOpenFileNames(self, '打开LAS文件', './')  # 注意这里返回值是元组
        if fnames[0]:
            for fname in fnames[0]:
                self.textEdit_4.append(fname)

    def readLasFiles(self):
        fileDir = self.textEdit_4.toPlainText()
        fileDir = fileDir.replace('file:///', '')
        fileDir = fileDir.replace('file:/', '')

        # 解决中文乱码问题
        # myfont = fm.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)
        # matplotlib.rcParams["axes.unicode_minus"] = False
        # 读取las数据
        # log = las.LASReader(u'ning209H19-4_resample_jz.LAS', null_subs=np.nan)
        # log = las.LASReader(fileDir, null_subs=np.nan)
        self.mat_view = Matplot_class(fileDir)  # 关键一步，创建Matplot_class类对象

    def table_casing(self):
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_5.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_5.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始井深(m)', '结束井深(m)', '套管外径(mm)', '套管内径(mm)', '壁厚(mm)']
        self.tableWidget_5.setHorizontalHeaderLabels(self.headers)

        self.tableWidget_5.setColumnWidth(0, 100)
        self.tableWidget_5.setColumnWidth(1, 100)
        self.tableWidget_5.setColumnWidth(2, 100)
        self.tableWidget_5.setColumnWidth(3, 100)
        self.tableWidget_5.setColumnWidth(4, 80)

        # self.tableWidget_5.setRowHeight(0, 50)
        # self.tableWidget_5.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget_5.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def add_line_for_tableWidget_5(self):
        self.row_tableWidget_5 = self.tableWidget_5.rowCount()
        self.tableWidget_5.setRowCount(self.row_tableWidget_5 + 1)

        # 添加默认表格数据
        self.tableWidget_5.setItem(self.row_tableWidget_5, 0, QTableWidgetItem('0'))
        self.tableWidget_5.setItem(self.row_tableWidget_5, 1, QTableWidgetItem('9999'))
        self.tableWidget_5.setItem(self.row_tableWidget_5, 2, QTableWidgetItem('139.7'))
        self.tableWidget_5.setItem(self.row_tableWidget_5, 3, QTableWidgetItem('114.3'))
        self.tableWidget_5.setItem(self.row_tableWidget_5, 4, QTableWidgetItem('12.7'))


    def delete_line_for_tableWidget_5(self):
        # self.table.cellChanged.disconnect()
        self.row = self.tableWidget_5.rowCount()
        self.tableWidget_5.setRowCount(self.row - 1)

    def casing_info_save(self):
        self.row_tableWidget_5 = self.tableWidget_5.rowCount()
        xls = xlwt.Workbook()
        sht1 = xls.add_sheet('Sheet1')
        # 添加字段
        sht1.write(0, 0, self.tableWidget_5.item(0, 0).text())
        sht1.write(0, 1, self.tableWidget_5.item(0, 1).text())
        sht1.write(0, 2, self.tableWidget_5.item(0, 2).text())
        sht1.write(0, 3, self.tableWidget_5.item(0, 3).text())
        sht1.write(0, 4, self.tableWidget_5.item(0, 4).text())
        xls.save('.\\casing_data.xls')

    ############################################################################################
    # 损伤评价
    ############################################################################################

    def table2(self):
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_2.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_2.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始深度(m)', '结束深度(m)', '最大损伤点深度(m)', '臂号', '单臂测量值(mm)', '最大测量值(mm)', '最小内径(mm)', '平均内径(mm)', '最大内径(mm)']
        self.tableWidget_2.setHorizontalHeaderLabels(self.headers)

        self.tableWidget_2.setColumnWidth(0, 80)
        self.tableWidget_2.setColumnWidth(1, 80)
        self.tableWidget_2.setColumnWidth(2, 115)
        self.tableWidget_2.setColumnWidth(3, 40)
        self.tableWidget_2.setColumnWidth(4, 100)
        self.tableWidget_2.setColumnWidth(5, 100)
        self.tableWidget_2.setColumnWidth(6, 100)
        self.tableWidget_2.setColumnWidth(7, 100)
        self.tableWidget_2.setColumnWidth(8, 100)

        # self.tableWidget_2.setRowHeight(0, 50)
        # self.tableWidget_2.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget_2.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def add_line_for_tableWidget_2(self):
        # 读取文件中的数值
        data = pd.read_excel('Penetration.xlsx', index=False)
        self.start_Depth = data.loc[0, 'value']
        self.end_Depth = data.loc[1, 'value']
        self.critical_Depth = data.loc[2, 'value']
        self.finger_Number = data.loc[3, 'value']
        self.finger_Value = data.loc[4, 'value']
        self.normal_Value = data.loc[5, 'value']
        self.min_Diameter = data.loc[6, 'value']
        self.ave_Diameter = data.loc[7, 'value']
        self.max_Diameter = data.loc[8, 'value']
        # self.table.cellChanged.disconnect()
        self.row_tableWidget_2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(self.row_tableWidget_2 + 1)
        # 添加表格数据
        self.tableWidget_2.setItem(self.row_tableWidget_2, 0, QTableWidgetItem(str(self.start_Depth)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 1, QTableWidgetItem(str(self.end_Depth)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 2, QTableWidgetItem(str(self.critical_Depth)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 3, QTableWidgetItem(str(int(self.finger_Number))))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 4, QTableWidgetItem(str(self.finger_Value)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 5, QTableWidgetItem(str(self.normal_Value)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 6, QTableWidgetItem(str(self.min_Diameter)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 7, QTableWidgetItem(str(self.ave_Diameter)))
        self.tableWidget_2.setItem(self.row_tableWidget_2, 8, QTableWidgetItem(str(self.max_Diameter)))

    def delete_line_for_tableWidget_2(self):
        # self.table.cellChanged.disconnect()
        self.row = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(self.row - 1)

    def generate_results_from_tableWidget_2(self):
        self.row_tableWidget_2 = self.tableWidget_2.rowCount()
        text_all = ''
        data = pd.DataFrame({'损伤井段(m)': '',
                             '最大损伤点深度(m)': '',
                             '单臂测量值(mm)': '',
                             '最小内径(mm)': '',
                             '平均内径(mm)': '',
                             '最大内径(mm)': '',
                             '损伤量(mm)': '',
                             '损伤程度(%)': '',
                             '损伤级别': ''},
                            index=[1])
        for row in range(0, self.row_tableWidget_2):
            self.row_tableWidget_5 = self.tableWidget_5.rowCount()
            if self.row_tableWidget_5 == 1:
                inner_Diameter = self.tableWidget_5.item(0, 3).text()
                inner_Diameter = float(inner_Diameter)
                thickness = self.tableWidget_5.item(0, 4).text()
                thickness = float(thickness)
                print('最大损伤点深度落在套管第一段')
            elif self.row_tableWidget_5 == 2:
                if float(self.tableWidget_2.item(row, 2).text()) < float(self.tableWidget_5.item(0, 2).text()):# 最大损伤点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第一段')
                elif float(self.tableWidget_2.item(row, 2).text()) >= float(self.tableWidget_5.item(1, 1).text()):# 最大损伤点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第二段')
            elif self.row_tableWidget_5 == 3:
                if float(self.tableWidget_2.item(row, 2).text()) < float(self.tableWidget_5.item(0, 2).text()):# 最大损伤点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第一段')
                elif (float(self.tableWidget_2.item(row, 2).text()) >= float(self.tableWidget_5.item(1, 1).text())) and \
                        (float(self.tableWidget_2.item(row, 2).text()) < float(self.tableWidget_5.item(1, 1).text())):# 最大损伤点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第二段')
                elif (float(self.tableWidget_2.item(row, 2).text()) >= float(self.tableWidget_5.item(2, 1).text())) and \
                        (float(self.tableWidget_2.item(row, 2).text()) < float(self.tableWidget_5.item(2, 1).text())):# 最大损伤点深度落在套管第三段
                    inner_Diameter = self.tableWidget_5.item(2, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(2, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第三段')

            well_interval = ''.join([self.tableWidget_2.item(row, 0).text(), '-', self.tableWidget_2.item(row, 1).text()])
            penetration_value = float(self.tableWidget_2.item(row, 4).text()) - float(self.tableWidget_2.item(row, 5).text())
            penetration_value = round(penetration_value, 2)
            penetration_degree = penetration_value / thickness * 100
            penetration_degree = round(penetration_degree, 2)

            # 损伤级别判定
            penetration_describe = ''
            if penetration_degree < 10:
                penetration_describe = '一级损伤'
            elif 10 <= penetration_degree < 20:
                penetration_describe = '二级损伤'
            elif 20 <= penetration_degree < 40:
                penetration_describe = '三级损伤'
            elif 40 <= penetration_degree < 85:
                penetration_describe = '四级损伤'
            elif penetration_degree >= 85:
                penetration_describe = '五级损伤'

            data_single_layer = pd.DataFrame({'损伤井段(m)': well_interval,
                                              '最大损伤点深度(m)': self.tableWidget_2.item(row, 2).text(),
                                              '单臂测量值(mm)': self.tableWidget_2.item(row, 3).text(),
                                              '最小内径(mm)': self.tableWidget_2.item(row, 6).text(),
                                              '平均内径(mm)': self.tableWidget_2.item(row, 7).text(),
                                              '最大内径(mm)': self.tableWidget_2.item(row, 8).text(),
                                              '损伤量(mm)': str(penetration_value),
                                              '损伤程度(%)': str(penetration_degree),
                                              '损伤级别': str(penetration_describe)},
                                             index=[1])
            data = pd.concat([data, data_single_layer], ignore_index=True)
            text = ''.join(['井段', well_interval, 'm，存在套管损伤，最大损伤点深度为', self.tableWidget_2.item(row, 2).text(), 'm，第', \
                            self.tableWidget_2.item(row, 3).text(), '号臂测得的最大值为', self.tableWidget_2.item(row, 4).text(), \
                            'mm，该臂在正常段的测量值为', self.tableWidget_2.item(row, 5).text(), 'mm，在最大损伤点深度处测量得到的最小内径为', \
                            self.tableWidget_2.item(row, 6).text(), 'mm，测量平均内径为', self.tableWidget_2.item(row, 7).text(), \
                            'mm，测量最大内径为', self.tableWidget_2.item(row, 8).text(), 'mm，最大损伤量为', str(penetration_value), \
                            'mm，损伤程度为', str(penetration_degree), '%，根据解释标准评价为', str(penetration_describe), '。\n'])
            text_all = ''.join([text_all, text])
        data.drop([0], inplace=True)
        print(data)
        writer = pd.ExcelWriter('损伤评价表.xlsx')
        data.to_excel(writer, 'Sheet1')
        writer.save()
        
        #生成描述建议
        self.textEdit.setText(text_all)

    ############################################################################################
    # 结垢评价
    ############################################################################################

    def table3(self):
        self.tableWidget_3.setColumnCount(9)
        self.tableWidget_3.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_3.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_3.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始深度(m)', '结束深度(m)', '最大结垢点深度(m)', '臂号', '单臂测量值(mm)', '最大测量值(mm)', '最小内径(mm)', '平均内径(mm)',
                        '最大内径(mm)']
        self.tableWidget_3.setHorizontalHeaderLabels(self.headers)

        self.tableWidget_3.setColumnWidth(0, 80)
        self.tableWidget_3.setColumnWidth(1, 80)
        self.tableWidget_3.setColumnWidth(2, 115)
        self.tableWidget_3.setColumnWidth(3, 40)
        self.tableWidget_3.setColumnWidth(4, 100)
        self.tableWidget_3.setColumnWidth(5, 100)
        self.tableWidget_3.setColumnWidth(6, 100)
        self.tableWidget_3.setColumnWidth(7, 100)
        self.tableWidget_3.setColumnWidth(8, 100)

        # self.tableWidget_3.setRowHeight(0, 50)
        # self.tableWidget_3.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget_3.horizontalHeader().setVisible(False)  # 隐藏水平表头

    def add_line_for_tableWidget_3(self):
        # 读取文件中的数值
        data = pd.read_excel('Projection.xlsx', index=False)
        self.start_Depth = data.loc[0, 'value']
        self.end_Depth = data.loc[1, 'value']
        self.critical_Depth = data.loc[2, 'value']
        self.finger_Number = data.loc[3, 'value']
        self.finger_Value = data.loc[4, 'value']
        self.normal_Value = data.loc[5, 'value']
        self.min_Diameter = data.loc[6, 'value']
        self.ave_Diameter = data.loc[7, 'value']
        self.max_Diameter = data.loc[8, 'value']
        # self.table.cellChanged.disconnect()
        self.row_tableWidget_3 = self.tableWidget_3.rowCount()
        self.tableWidget_3.setRowCount(self.row_tableWidget_3 + 1)
        # 添加表格数据
        self.tableWidget_3.setItem(self.row_tableWidget_3, 0, QTableWidgetItem(str(self.start_Depth)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 1, QTableWidgetItem(str(self.end_Depth)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 2, QTableWidgetItem(str(self.critical_Depth)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 3, QTableWidgetItem(str(int(self.finger_Number))))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 4, QTableWidgetItem(str(self.finger_Value)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 5, QTableWidgetItem(str(self.normal_Value)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 6, QTableWidgetItem(str(self.min_Diameter)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 7, QTableWidgetItem(str(self.ave_Diameter)))
        self.tableWidget_3.setItem(self.row_tableWidget_3, 8, QTableWidgetItem(str(self.max_Diameter)))

    def delete_line_for_tableWidget_3(self):
        # self.table.cellChanged.disconnect()
        self.row = self.tableWidget_3.rowCount()
        self.tableWidget_3.setRowCount(self.row - 1)

    def generate_results_from_tableWidget_3(self):
        self.row_tableWidget_3 = self.tableWidget_3.rowCount()
        text_all = ''
        data = pd.DataFrame({'结垢井段(m)': '',
                             '最大结垢点深度(m)': '',
                             '单臂测量值(mm)': '',
                             '最小内径(mm)': '',
                             '平均内径(mm)': '',
                             '最大内径(mm)': '',
                             '结垢量(mm)': '',
                             '结垢程度(%)': '',
                             '结垢级别': ''},
                            index=[1])
        for row in range(0, self.row_tableWidget_3):
            self.row_tableWidget_5 = self.tableWidget_5.rowCount()
            if self.row_tableWidget_5 == 1:
                inner_Diameter = self.tableWidget_5.item(0, 3).text()
                inner_Diameter = float(inner_Diameter)
                thickness = self.tableWidget_5.item(0, 4).text()
                thickness = float(thickness)
                print('最大结垢点深度落在套管第一段')
            elif self.row_tableWidget_5 == 2:
                if float(self.tableWidget_3.item(row, 2).text()) < float(
                        self.tableWidget_5.item(0, 2).text()):  # 最大结垢点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大结垢点深度落在套管第一段')
                elif float(self.tableWidget_3.item(row, 2).text()) >= float(
                        self.tableWidget_5.item(1, 1).text()):  # 最大结垢点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大结垢点深度落在套管第二段')
            elif self.row_tableWidget_5 == 3:
                if float(self.tableWidget_3.item(row, 2).text()) < float(
                        self.tableWidget_5.item(0, 2).text()):  # 最大结垢点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大结垢点深度落在套管第一段')
                elif (float(self.tableWidget_3.item(row, 2).text()) >= float(self.tableWidget_5.item(1, 1).text())) and \
                        (float(self.tableWidget_3.item(row, 2).text()) < float(
                            self.tableWidget_5.item(1, 1).text())):  # 最大结垢点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大结垢点深度落在套管第二段')
                elif (float(self.tableWidget_3.item(row, 2).text()) >= float(self.tableWidget_5.item(2, 1).text())) and \
                        (float(self.tableWidget_3.item(row, 2).text()) < float(
                            self.tableWidget_5.item(2, 1).text())):  # 最大损伤点深度落在套管第三段
                    inner_Diameter = self.tableWidget_5.item(2, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(2, 4).text()
                    thickness = float(thickness)
                    print('最大结垢点深度落在套管第三段')

            well_interval = ''.join(
                [self.tableWidget_3.item(row, 0).text(), '-', self.tableWidget_3.item(row, 1).text()])
            projection_value = float(self.tableWidget_3.item(row, 5).text()) - float(self.tableWidget_3.item(row, 4).text())
            projection_value = round(projection_value, 2)
            projection_degree = projection_value / (inner_Diameter / 2) * 100
            projection_degree = round(projection_degree, 2)

            # 结垢级别判定
            projection_describe = ''
            if projection_degree < 10:
                projection_describe = '一级结垢'
            elif 10 <= projection_degree < 20:
                projection_describe = '二级结垢'
            elif 20 <= projection_degree < 40:
                projection_describe = '三级结垢'
            elif 40 <= projection_degree < 85:
                projection_describe = '四级结垢'
            elif projection_degree >= 85:
                projection_describe = '五级结垢'

            data_single_layer = pd.DataFrame({'结垢井段(m)': well_interval,
                                              '最大结垢点深度(m)': self.tableWidget_3.item(row, 2).text(),
                                              '单臂测量值(mm)': self.tableWidget_3.item(row, 3).text(),
                                              '最小内径(mm)': self.tableWidget_3.item(row, 6).text(),
                                              '平均内径(mm)': self.tableWidget_3.item(row, 7).text(),
                                              '最大内径(mm)': self.tableWidget_3.item(row, 8).text(),
                                              '结垢量(mm)': str(projection_value),
                                              '结垢程度(%)': str(projection_degree),
                                              '结垢级别': str(projection_describe)},
                                             index=[1])
            data = pd.concat([data, data_single_layer], ignore_index=True)
            text = ''.join(['井段', well_interval, 'm，存在套管损伤，最大结垢点深度为', self.tableWidget_3.item(row, 2).text(), 'm，第', \
                            self.tableWidget_3.item(row, 3).text(), '号臂测得的最小值为', self.tableWidget_3.item(row, 4).text(), \
                            'mm，该臂在正常段的测量值为', self.tableWidget_3.item(row, 5).text(), 'mm，在最大结垢点深度处测量得到的最小内径为', \
                            self.tableWidget_3.item(row, 6).text(), 'mm，测量平均内径为', self.tableWidget_3.item(row, 7).text(), \
                            'mm，测量最大内径为', self.tableWidget_3.item(row, 8).text(), 'mm，最大结垢量为', str(projection_value), \
                            'mm，结垢程度为', str(projection_degree), '%，根据解释标准评价为', str(projection_describe), '。\n'])
            text_all = ''.join([text_all, text])
        data.drop([0], inplace=True)
        print(data)
        writer = pd.ExcelWriter('结垢评价表.xlsx')
        data.to_excel(writer, 'Sheet1')
        writer.save()

        # 生成描述建议
        self.textEdit_2.setText(text_all)

    ############################################################################################
    # 变形评价
    ############################################################################################
    def table4(self):
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(0)
        row = 0  # 第几行（从0开始）
        col = 0  # 第几列（从0开始）
        # self.tableWidget_4.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        self.tableWidget_4.horizontalHeader().setSectionsClickable(False)  # 禁止点击表头的列
        self.headers = ['起始深度(m)', '结束深度(m)', '最大变形点深度(m)', '最小内径(mm)', '平均内径(mm)', '最大内径(mm)']
        self.tableWidget_4.setHorizontalHeaderLabels(self.headers)

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
        data = pd.read_excel('Transformation.xlsx', index=False)
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
            self.row_tableWidget_5 = self.tableWidget_5.rowCount()
            if self.row_tableWidget_5 == 1:
                inner_Diameter = self.tableWidget_5.item(0, 3).text()
                inner_Diameter = float(inner_Diameter)
                thickness = self.tableWidget_5.item(0, 4).text()
                thickness = float(thickness)
                print('最大损伤点深度落在套管第一段')
            elif self.row_tableWidget_5 == 2:
                if float(self.tableWidget_2.item(row, 2).text()) < float(
                        self.tableWidget_5.item(0, 2).text()):  # 最大损伤点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第一段')
                elif float(self.tableWidget_2.item(row, 2).text()) >= float(
                        self.tableWidget_5.item(1, 1).text()):  # 最大损伤点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第二段')
            elif self.row_tableWidget_5 == 3:
                if float(self.tableWidget_2.item(row, 2).text()) < float(
                        self.tableWidget_5.item(0, 2).text()):  # 最大损伤点深度落在套管第一段
                    inner_Diameter = self.tableWidget_5.item(0, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(0, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第一段')
                elif (float(self.tableWidget_2.item(row, 2).text()) >= float(self.tableWidget_5.item(1, 1).text())) and \
                        (float(self.tableWidget_2.item(row, 2).text()) < float(
                            self.tableWidget_5.item(1, 1).text())):  # 最大损伤点深度落在套管第二段
                    inner_Diameter = self.tableWidget_5.item(1, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(1, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第二段')
                elif (float(self.tableWidget_2.item(row, 2).text()) >= float(self.tableWidget_5.item(2, 1).text())) and \
                        (float(self.tableWidget_2.item(row, 2).text()) < float(
                            self.tableWidget_5.item(2, 1).text())):  # 最大损伤点深度落在套管第三段
                    inner_Diameter = self.tableWidget_5.item(2, 3).text()
                    inner_Diameter = float(inner_Diameter)
                    thickness = self.tableWidget_5.item(2, 4).text()
                    thickness = float(thickness)
                    print('最大损伤点深度落在套管第三段')

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
            text = ''.join(['井段', well_interval, 'm，存在套管变形特征，变形长度为', str(transformation_length),\
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
