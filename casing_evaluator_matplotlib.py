# -*- coding: utf-8 -*-
import io
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, MultiCursor, RadioButtons, Button
import matplotlib.font_manager as fm
import las
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog

class Matplot_class:
    def __init__(self, fileDir):
        self.lines = []#生成的成果list
        self.log = las.LASReader(fileDir, null_subs=np.nan)
        self.fig1 = plt.figure('MIT油套管损伤结垢变形评价系统', figsize=(10, 8))
        # 定义RadioButtons
        axcolor = 'lightgoldenrodyellow'
        rax = plt.axes([0.05, 0.7, 0.18, 0.15], facecolor=axcolor)
        radio = RadioButtons(rax, (u'Penetration', u'Projection', u'Transformation'))
        plt.subplots_adjust(left=0.35)
        radio.on_clicked(self.actionfunc)
        #####################################################################################
        # 坐标轴1
        self.ax1 = plt.subplot(141)
        self.line1, = self.ax1.plot(self.log.data['FING01'], self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING02'] + 2.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING03'] + 5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING04'] + 7.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING05'] + 10, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax1.plot(self.log.data['FING06'] + 12.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING07'] + 15, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING08'] + 17.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING09'] + 20, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING10'] + 22.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax1.plot(self.log.data['FING11'] + 25, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING12'] + 27.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING13'] + 30, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING14'] + 32.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING15'] + 35, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax1.plot(self.log.data['FING16'] + 37.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING17'] + 40, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING18'] + 42.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING19'] + 45, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING20'] + 47.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax1.plot(self.log.data['FING21'] + 50, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING22'] + 52.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING23'] + 55, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax1.plot(self.log.data['FING24'] + 57.5, self.log.data['DEPT'], 'g-', lw=0.5)

        self.ax1.set_xlim(40, 120)
        self.ax1.set_ylim(self.log.start, self.log.stop)
        self.ax1.invert_yaxis()

        span1 = SpanSelector(self.ax1, self.onselect1, 'vertical', useblit=False,
                             rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
        # plt.ylabel(self.log.curves.DEPT.descr + " (%s)" % self.log.curves.DEPT.units)
        # plt.xlabel(self.log.curves.FING01.descr + " (%s)" % self.log.curves.FING01.units)
        # plt.title(self.log.well.WELL.data)
        plt.ylabel('Measured Depth(m)')
        plt.title('Original')

        plt.gca().spines['bottom'].set_position(('data', 0))
        plt.gca().spines['top'].set_position(('data', 0))
        plt.grid()
        #####################################################################################
        # 坐标轴2
        self.ax2 = plt.subplot(142)
        self.line2, = self.ax2.plot(self.log.data['FING01'], self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING02'] + 2.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING03'] + 5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING04'] + 7.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING05'] + 10, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax2.plot(self.log.data['FING06'] + 12.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING07'] + 15, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING08'] + 17.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING09'] + 20, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING10'] + 22.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax2.plot(self.log.data['FING11'] + 25, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING12'] + 27.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING13'] + 30, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING14'] + 32.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING15'] + 35, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax2.plot(self.log.data['FING16'] + 37.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING17'] + 40, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING18'] + 42.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING19'] + 45, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING20'] + 47.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax2.plot(self.log.data['FING21'] + 50, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING22'] + 52.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING23'] + 55, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax2.plot(self.log.data['FING24'] + 57.5, self.log.data['DEPT'], 'g-', lw=0.5)

        self.ax2.set_xlim(40, 120)
        self.ax2.set_ylim(self.log.start, self.log.stop)
        self.ax2.invert_yaxis()

        span2 = SpanSelector(self.ax2, self.onselect2, 'vertical', useblit=False,
                             rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
        plt.title('Middle')
        plt.gca().spines['bottom'].set_position(('data', 0))
        plt.gca().spines['top'].set_position(('data', 0))
        self.ax2.grid()
        #####################################################################################
        # 坐标轴3
        self.ax3 = plt.subplot(143)
        self.line3, = self.ax3.plot(self.log.data['FING01'], self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING02'] + 2.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING03'] + 5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING04'] + 7.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING05'] + 10, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax3.plot(self.log.data['FING06'] + 12.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING07'] + 15, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING08'] + 17.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING09'] + 20, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING10'] + 22.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax3.plot(self.log.data['FING11'] + 25, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING12'] + 27.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING13'] + 30, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING14'] + 32.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING15'] + 35, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax3.plot(self.log.data['FING16'] + 37.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING17'] + 40, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING18'] + 42.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING19'] + 45, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING20'] + 47.5, self.log.data['DEPT'], 'r-', lw=0.5)
        self.ax3.plot(self.log.data['FING21'] + 50, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING22'] + 52.5, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING23'] + 55, self.log.data['DEPT'], 'g-', lw=0.5)
        self.ax3.plot(self.log.data['FING24'] + 57.5, self.log.data['DEPT'], 'g-', lw=0.5)

        self.ax3.set_xlim(40, 120)
        self.ax3.set_ylim(self.log.start, self.log.stop)
        self.ax3.invert_yaxis()

        # self.span3_cyan = SpanSelector(self.ax3, self.onselect3, 'vertical', useblit=True,
        #                           rectprops=dict(alpha=0.5, facecolor='cyan'), span_stays=True)

        plt.title('Large')
        plt.gca().spines['bottom'].set_position(('data', 0))
        plt.gca().spines['top'].set_position(('data', 0))
        self.ax3.grid()
        #####################################################################################
        # 坐标轴4
        self.ax4 = plt.subplot(144)
        line4, = self.ax4.plot(self.log.data['MAXDIA'], self.log.data['DEPT'], 'r--', lw=0.5)
        self.ax4.plot(self.log.data['MINDIA'], self.log.data['DEPT'], 'b-', lw=0.5)
        self.ax4.plot(self.log.data['AVEDIA'], self.log.data['DEPT'], 'k--', lw=0.5)

        self.ax4.set_xlim(20, 150)
        self.ax4.set_ylim(self.log.start, self.log.stop)
        self.ax4.invert_yaxis()

        plt.title('Min-Max')
        plt.gca().spines['bottom'].set_position(('data', 0))
        plt.gca().spines['top'].set_position(('data', 0))
        self.ax4.grid()

        multi = MultiCursor(plt.gcf().canvas, (self.ax1, self.ax2, self.ax3, self.ax4), color='r', lw=1,
                            horizOn=True, vertOn=False)
        #########################

        plt.show()

    def onselect1(self, ymin, ymax):
        indmin, indmax = np.searchsorted(self.log.data['DEPT'], (ymin, ymax))
        indmax = min(len(self.log.data['DEPT']) - 1, indmax)
        thisx = self.log.data['FING01'][indmin:indmax]
        thisy = self.log.data['DEPT'][indmin:indmax]
        self.line2.set_data(thisx, thisy)
        self.ax2.set_ylim(thisy[-1], thisy[0])
        self.line3.set_data(thisx, thisy)
        self.ax3.set_ylim(thisy[-1], thisy[0])
        self.ax4.set_ylim(thisy[-1], thisy[0])
        plt.gcf().canvas.draw()

    def onselect2(self, ymin, ymax):
        indmin, indmax = np.searchsorted(self.log.data['DEPT'], (ymin, ymax))
        indmax = min(len(self.log.data['DEPT']) - 1, indmax)
        thisx = self.log.data['FING01'][indmin:indmax]
        thisy = self.log.data['DEPT'][indmin:indmax]
        self.line3.set_data(thisx, thisy)
        self.ax3.set_ylim(thisy[-1], thisy[0])
        self.ax4.set_ylim(thisy[-1], thisy[0])
        plt.gcf().canvas.draw()

    def onselect3(self, ymin, ymax):
        ymin = round(ymin, 2)
        ymax = round(ymax, 2)
        if ymin != ymax:
            self.lines = [] #清空一下
            print('井段为：', ymin, '-', ymax)
            self.lines.append(ymin)
            self.lines.append(ymax)
        elif ymin == ymax:
            print('极值深度为：', ymax)
            self.lines.append(ymax)
            index = np.where(abs(self.log.data['DEPT'] - ymax) <= 0.01)
            index = index[0][0]
            FING01_value = self.log.data['FING01'][index]
            FING02_value = self.log.data['FING02'][index]
            FING03_value = self.log.data['FING03'][index]
            FING04_value = self.log.data['FING04'][index]
            FING05_value = self.log.data['FING05'][index]
            FING06_value = self.log.data['FING06'][index]
            FING07_value = self.log.data['FING07'][index]
            FING08_value = self.log.data['FING08'][index]
            FING09_value = self.log.data['FING09'][index]
            FING10_value = self.log.data['FING10'][index]
            FING11_value = self.log.data['FING11'][index]
            FING12_value = self.log.data['FING12'][index]
            FING13_value = self.log.data['FING13'][index]
            FING14_value = self.log.data['FING14'][index]
            FING15_value = self.log.data['FING15'][index]
            FING16_value = self.log.data['FING16'][index]
            FING17_value = self.log.data['FING17'][index]
            FING18_value = self.log.data['FING18'][index]
            FING19_value = self.log.data['FING19'][index]
            FING20_value = self.log.data['FING20'][index]
            FING21_value = self.log.data['FING21'][index]
            FING22_value = self.log.data['FING22'][index]
            FING23_value = self.log.data['FING23'][index]
            FING24_value = self.log.data['FING24'][index]
            self.Min_value = self.log.data['MINDIA'][index]
            self.Ave_value = self.log.data['AVEDIA'][index]
            self.Max_value = self.log.data['MAXDIA'][index]
            print(str(self.Min_value), ' ', str(self.Ave_value), ' ', str(self.Max_value))
            self.lines.append(self.Min_value)
            self.lines.append(self.Ave_value)
            self.lines.append(self.Max_value)
            print(self.lines)
            #保存list到文件
            self.lines_temp = pd.DataFrame(self.lines, columns=['value'])
            writer = pd.ExcelWriter('temp.xlsx', index=False)
            self.lines_temp.to_excel(writer, 'Sheet1')
            writer.save()

            fig2 = plt.figure('截面图')
            # 设置下面所需要的参数
            barSlices1 = 24
            barSlices2 = 100

            # theta指每个标记所在射线与极径的夹角，下面表示均分角度
            theta1 = np.linspace(0.0, 2 * np.pi, barSlices1, endpoint=False)
            theta2 = np.linspace(0.0, 2 * np.pi, barSlices2, endpoint=False)

            # # r表示点距离圆心的距离，np.random.rand(barSlices)表示返回返回服从“0-1”均匀分布的随机样本值
            # r = 2 * np.random.rand(barSlices) + 50
            r = [FING01_value, FING02_value, FING03_value, FING04_value, FING05_value, FING06_value, FING07_value,
                 FING08_value, FING09_value, FING10_value, FING11_value, FING12_value, FING13_value, FING14_value,
                 FING15_value, FING16_value, FING17_value, FING18_value, FING19_value, FING20_value, FING21_value,
                 FING22_value, FING23_value, FING24_value]

            # 网上搜的方法，不知道怎么就可以闭合了(黑人问号)
            r = np.concatenate((r, [r[0]]))  # 闭合
            theta1 = np.concatenate((theta1, [theta1[0]]))  # 闭合
            theta2 = np.concatenate((theta2, [theta2[0]]))  # 闭合

            inside_radius = [57.15] * barSlices2
            outside_radius = [69.85] * barSlices2

            inside_radius = np.concatenate((inside_radius, [inside_radius[0]]))  # 闭合
            outside_radius = np.concatenate((outside_radius, [outside_radius[0]]))  # 闭合

            # 绘图之前先清理一下
            plt.clf()
            # polar表示绘制极坐标图，颜色，线宽，标志点样式
            plt.polar(theta1, r, color="blue", linewidth=1, marker="", mfc="b", ms=10)
            plt.gca().set_theta_zero_location('N')
            # plt.gca().set_rlim(0, 57.15)  # 设置显示的极径范围
            plt.gca().set_rlim(0, 69.85)
            plt.gca().fill(theta1, r, facecolor='w', alpha=0.2)  # 填充颜色
            plt.gca().fill_between(theta2, outside_radius, inside_radius, facecolor='cyan', alpha=0.8)  # 填充之间颜色
            plt.gca().patch.set_facecolor('1')
            plt.gca().set_rgrids(np.arange(0, 100, 100))

            # label = np.array([j for j in range(1, 25)])  # 定义标签
            # plt.gca().set_thetagrids(np.arange(0, 360, 15), label)
            plt.gca().set_thetagrids(np.arange(0, 360, 360))

            text_show = ''.join(['Depth:', str(ymax), 'm\nOD: 69.85mm\nID: 57.15mm\nWT: 12.7mm'])
            plt.text(7 * np.pi / 4, 80, text_show)
            # 绘图展示
            plt.show()
    
    # RadioButtons行为定义
    def actionfunc(self, damage_type):
        # 损伤SpanSelector对象
        self.span3_red = SpanSelector(self.ax3, self.onselect3, 'vertical', useblit=True,
                                 rectprops=dict(alpha=0.5, facecolor='red'), span_stays=True)
        # 结垢SpanSelector对象
        self.span3_green = SpanSelector(self.ax3, self.onselect3, 'vertical', useblit=True,
                                   rectprops=dict(alpha=0.5, facecolor='green'), span_stays=True)
        # 变形SpanSelector对象
        self.span3_yellow = SpanSelector(self.ax3, self.onselect3, 'vertical', useblit=True,
                                    rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
        if damage_type == 'Penetration':
            print(damage_type)
            # del self.span3_red
            del self.span3_green
            del self.span3_yellow
            # del self.span3_cyan
        elif damage_type == 'Projection':
            print(damage_type)
            del self.span3_red
            # del self.span3_green
            del self.span3_yellow
            # del self.span3_cyan
        elif damage_type == 'Transformation':
            print(damage_type)
            del self.span3_red
            del self.span3_green
            # del self.span3_yellow
            # del self.span3_cyan