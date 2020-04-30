# -*- coding: utf-8 -*-
import io
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, MultiCursor, RadioButtons, Button
import matplotlib.font_manager as fm
import las

# 解决中文乱码问题
# myfont = fm.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)
# matplotlib.rcParams["axes.unicode_minus"] = False
# 读取las数据
log = las.LASReader(u'ning209H19-4_resample_jz.LAS', null_subs=np.nan)
fig1 = plt.figure('MIT油套管损伤结垢变形评价系统', figsize=(10, 8))

# RadioButtons行为定义
global damage_Tag
damage_Tag = ''
def actionfunc(damage_type):
    global damage_Tag
    global span3_red
    global span3_green
    global span3_yellow
    global span3_cyan
    # 损伤SpanSelector对象
    span3_red = SpanSelector(ax3, onselect3, 'vertical', useblit=True,
                             rectprops=dict(alpha=0.5, facecolor='red'), span_stays=True)
    # 结垢SpanSelector对象
    span3_green = SpanSelector(ax3, onselect3, 'vertical', useblit=True,
                               rectprops=dict(alpha=0.5, facecolor='green'), span_stays=True)
    # 变形SpanSelector对象
    span3_yellow = SpanSelector(ax3, onselect3, 'vertical', useblit=True,
                                rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
    if damage_type == 'Penetration':
        damage_Tag = 'Penetration'
        print('damage_Tag', damage_Tag)
        # del span3_red
        del span3_green
        del span3_yellow
        del span3_cyan
    elif damage_type == 'Projection':
        damage_Tag = 'Projection'
        print('damage_Tag', damage_Tag)
        del span3_red
        # del span3_green
        del span3_yellow
        del span3_cyan
    elif damage_type == 'Transformation':
        damage_Tag = 'Transformation'
        print('damage_Tag', damage_Tag)
        del span3_red
        del span3_green
        # del span3_yellow
        del span3_cyan
# 创建按钮
class ButtonHandler():
    def __init__(self):
        pass

    def Start(self):
        pass

    def Stop(self):
        pass

# 定义RadioButtons
axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.18, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, (u'Penetration', u'Projection', u'Transformation'))
plt.subplots_adjust(left=0.35)

radio.on_clicked(actionfunc)

# 创建按钮并设置单击事件处理函数
callback = ButtonHandler()
axnext = plt.axes([0.05, 0.5, 0.18, 0.1])
bnext = Button(axnext, 'Add to table')
bnext.on_clicked(callback.Start)
axprev = plt.axes([0.05, 0.3, 0.18, 0.1])
bprev = Button(axprev, 'Delete from table')
bprev.on_clicked(callback.Stop)

#####################################################################################
#####################################################################################
# 坐标轴1
ax1 = plt.subplot(141)
line1, = ax1.plot(log.data['FING01'], log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING02'] + 2.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING03'] + 5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING04'] + 7.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING05'] + 10, log.data['DEPT'], 'r-', lw=0.5)
ax1.plot(log.data['FING06'] + 12.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING07'] + 15, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING08'] + 17.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING09'] + 20, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING10'] + 22.5, log.data['DEPT'], 'r-', lw=0.5)
ax1.plot(log.data['FING11'] + 25, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING12'] + 27.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING13'] + 30, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING14'] + 32.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING15'] + 35, log.data['DEPT'], 'r-', lw=0.5)
ax1.plot(log.data['FING16'] + 37.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING17'] + 40, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING18'] + 42.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING19'] + 45, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING20'] + 47.5, log.data['DEPT'], 'r-', lw=0.5)
ax1.plot(log.data['FING21'] + 50, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING22'] + 52.5, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING23'] + 55, log.data['DEPT'], 'g-', lw=0.5)
ax1.plot(log.data['FING24'] + 57.5, log.data['DEPT'], 'g-', lw=0.5)

ax1.set_xlim(40, 120)
ax1.set_ylim(log.start, log.stop)
ax1.invert_yaxis()

def onselect1(ymin, ymax):
    indmin, indmax = np.searchsorted(log.data['DEPT'], (ymin, ymax))
    indmax = min(len(log.data['DEPT']) - 1, indmax)
    thisx = log.data['FING01'][indmin:indmax]
    thisy = log.data['DEPT'][indmin:indmax]
    line2.set_data(thisx, thisy)
    ax2.set_ylim(thisy[-1], thisy[0])
    line3.set_data(thisx, thisy)
    ax3.set_ylim(thisy[-1], thisy[0])
    ax4.set_ylim(thisy[-1], thisy[0])
    plt.gcf().canvas.draw()

span1 = SpanSelector(ax1, onselect1, 'vertical', useblit=False,
                     rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
# plt.ylabel(log.curves.DEPT.descr + " (%s)" % log.curves.DEPT.units)
# plt.xlabel(log.curves.FING01.descr + " (%s)" % log.curves.FING01.units)
# plt.title(log.well.WELL.data)
plt.ylabel('Measured Depth(m)')
plt.title('Original')

plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_position(('data', 0))
plt.grid()
#####################################################################################
#####################################################################################
# 坐标轴2
ax2 = plt.subplot(142)
line2, = ax2.plot(log.data['FING01'], log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING02'] + 2.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING03'] + 5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING04'] + 7.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING05'] + 10, log.data['DEPT'], 'r-', lw=0.5)
ax2.plot(log.data['FING06'] + 12.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING07'] + 15, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING08'] + 17.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING09'] + 20, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING10'] + 22.5, log.data['DEPT'], 'r-', lw=0.5)
ax2.plot(log.data['FING11'] + 25, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING12'] + 27.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING13'] + 30, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING14'] + 32.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING15'] + 35, log.data['DEPT'], 'r-', lw=0.5)
ax2.plot(log.data['FING16'] + 37.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING17'] + 40, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING18'] + 42.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING19'] + 45, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING20'] + 47.5, log.data['DEPT'], 'r-', lw=0.5)
ax2.plot(log.data['FING21'] + 50, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING22'] + 52.5, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING23'] + 55, log.data['DEPT'], 'g-', lw=0.5)
ax2.plot(log.data['FING24'] + 57.5, log.data['DEPT'], 'g-', lw=0.5)

ax2.set_xlim(40, 120)
ax2.set_ylim(log.start, log.stop)
ax2.invert_yaxis()

def onselect2(ymin, ymax):
    indmin, indmax = np.searchsorted(log.data['DEPT'], (ymin, ymax))
    indmax = min(len(log.data['DEPT']) - 1, indmax)
    thisx = log.data['FING01'][indmin:indmax]
    thisy = log.data['DEPT'][indmin:indmax]
    line3.set_data(thisx, thisy)
    ax3.set_ylim(thisy[-1], thisy[0])
    ax4.set_ylim(thisy[-1], thisy[0])
    plt.gcf().canvas.draw()

span2 = SpanSelector(ax2, onselect2, 'vertical', useblit=False,
                     rectprops=dict(alpha=0.5, facecolor='yellow'), span_stays=True)
plt.title('Middle')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_position(('data', 0))
ax2.grid()

#####################################################################################
#####################################################################################
# 坐标轴3
ax3 = plt.subplot(143)
line3, = ax3.plot(log.data['FING01'], log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING02'] + 2.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING03'] + 5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING04'] + 7.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING05'] + 10, log.data['DEPT'], 'r-', lw=0.5)
ax3.plot(log.data['FING06'] + 12.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING07'] + 15, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING08'] + 17.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING09'] + 20, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING10'] + 22.5, log.data['DEPT'], 'r-', lw=0.5)
ax3.plot(log.data['FING11'] + 25, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING12'] + 27.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING13'] + 30, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING14'] + 32.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING15'] + 35, log.data['DEPT'], 'r-', lw=0.5)
ax3.plot(log.data['FING16'] + 37.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING17'] + 40, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING18'] + 42.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING19'] + 45, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING20'] + 47.5, log.data['DEPT'], 'r-', lw=0.5)
ax3.plot(log.data['FING21'] + 50, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING22'] + 52.5, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING23'] + 55, log.data['DEPT'], 'g-', lw=0.5)
ax3.plot(log.data['FING24'] + 57.5, log.data['DEPT'], 'g-', lw=0.5)

ax3.set_xlim(40, 120)
ax3.set_ylim(log.start, log.stop)
ax3.invert_yaxis()

def onselect3(ymin, ymax):
    print('damage_Tag now is ', damage_Tag)
    ymin = round(ymin, 2)
    ymax = round(ymax, 2)
    if ymin != ymax:
        print('井段为：', ymin, '-', ymax)
    elif ymin == ymax:
        print('极值深度为：', ymax)
        index = np.where(abs(log.data['DEPT'] - ymax) <= 0.01)
        index = index[0][0]
        FING01_value = log.data['FING01'][index]
        FING02_value = log.data['FING02'][index]
        FING03_value = log.data['FING03'][index]
        FING04_value = log.data['FING04'][index]
        FING05_value = log.data['FING05'][index]
        FING06_value = log.data['FING06'][index]
        FING07_value = log.data['FING07'][index]
        FING08_value = log.data['FING08'][index]
        FING09_value = log.data['FING09'][index]
        FING10_value = log.data['FING10'][index]
        FING11_value = log.data['FING11'][index]
        FING12_value = log.data['FING12'][index]
        FING13_value = log.data['FING13'][index]
        FING14_value = log.data['FING14'][index]
        FING15_value = log.data['FING15'][index]
        FING16_value = log.data['FING16'][index]
        FING17_value = log.data['FING17'][index]
        FING18_value = log.data['FING18'][index]
        FING19_value = log.data['FING19'][index]
        FING20_value = log.data['FING20'][index]
        FING21_value = log.data['FING21'][index]
        FING22_value = log.data['FING22'][index]
        FING23_value = log.data['FING23'][index]
        FING24_value = log.data['FING24'][index]
        Min_value = log.data['MINDIA'][index]
        Ave_value = log.data['AVEDIA'][index]
        Max_value = log.data['MAXDIA'][index]
        print(str(Min_value), ' ', str(Ave_value), ' ', str(Max_value))
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
        plt.text(7*np.pi/4, 80, text_show)
        # 绘图展示
        plt.show()

span3_cyan = SpanSelector(ax3, onselect3, 'vertical', useblit=True,
                     rectprops=dict(alpha=0.5, facecolor='cyan'), span_stays=True)

plt.title('Large')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_position(('data', 0))
ax3.grid()

#####################################################################################
#####################################################################################
# 坐标轴4
ax4 = plt.subplot(144)
line4, = ax4.plot(log.data['MAXDIA'], log.data['DEPT'], 'r--', lw=0.5)
ax4.plot(log.data['MINDIA'], log.data['DEPT'], 'b-', lw=0.5)
ax4.plot(log.data['AVEDIA'], log.data['DEPT'], 'k--', lw=0.5)

ax4.set_xlim(20, 150)
ax4.set_ylim(log.start, log.stop)
ax4.invert_yaxis()

plt.title('Min-Max')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_position(('data', 0))
ax4.grid()

multi = MultiCursor(plt.gcf().canvas, (ax1, ax2, ax3, ax4), color='r', lw=1,
                    horizOn=True, vertOn=False)
#########################

plt.show()