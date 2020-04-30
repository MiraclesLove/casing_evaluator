#demo_14:关于TableWidGet的使用，注意：在table表头分为水平和垂直两种，及horizontal header和vertical header两类。

from PyQt5.QtWidgets import (QTableWidget,QApplication,QWidget,QTableWidgetItem,QHBoxLayout)
from PyQt5.QtCore import Qt
import PyQt5.QtGui as QtGui

import sys
class Example(QWidget):
    data=[{'num':'101','name':'JONES','sal':200,'date':'1999-10-10','sex':'女'},
          {'num': '102', 'name': 'SITH', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
          {'num': '103', 'name': 'SDF', 'sal': 200, 'date': '1999-12-10', 'sex': '女'},
          {'num': '104', 'name': 'JSSS', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
          {'num': '105', 'name': 'JEEE', 'sal': 200, 'date': '1912-10-10', 'sex': '女'}
          ]

    def __init__(self):
            super().__init__()
            self.initUI()

    def initUI(self):
            titles = ['编号', '姓名', '工资', '入职日期', ' 性别']
            self.setWindowTitle('员工信息')
            self.table = QTableWidget()
            self.table.setRowCount(9)                                   #行下标最大值
            self.table.setColumnCount(5)                                #列
            self.table.setHorizontalHeaderLabels(titles)                #标题列


            #表格或者窗体背景图片
            palette =  QtGui.QPalette()
            icon =  QtGui.QPixmap('a.jpg')
            palette.setBrush(self.table.backgroundRole(),  QtGui.QBrush(icon))  # 添加背景图片
            self.setPalette(palette)
            #表格行
            self.table.horizontalHeader().setStyleSheet("background-color: gray");
            # self.table.setEditTriggers(QTableWidget.NoEditTriggers)#单元格不可编辑
            # self.table.setSelectionBehavior(QTableWidget.SelectRows)  #选中列还是行，这里设置选中行
            # self.table.setSelectionMode(QTableWidget.SingleSelection) #只能选中一行或者一列
            #self.table.horizontalHeader().setStretchLastSection(True)  #列宽度占满表格(最后一个列拉伸处理沾满表格)
            #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch);#所有列自适应表格宽度

            #1、设置每一个标题单元格样式
            # for i in range(self.table.columnCount()):
            #       headItem = self.table.horizontalHeaderItem(i)
            #       headItem.setFont(QFont("song", 14, QFont.Bold))
            #       headItem.setForeground(QBrush(Qt.gray))
            #       headItem.setBackgroundColor(QColor(0, 60, 10))      # 设置单元格背景颜色
            #       #headItem.setTextColor(QColor(200, 111, 30))        # 设置文字颜色
            #       headItem.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

            #2、设置整个表格列标题样式
            font = self.table.horizontalHeader().font()
            font.setBold(True)
            self.table.horizontalHeader().setFont(font)
            #self.table.setFrameShape(QFrame.NoFrame)                   #设置表格外层无边框
            #self.table.setShowGrid(False)                              #是否显示单元格网格线False 则不显示
            #self.table.horizontalHeader().setHighlightSections(False)  #设置表格列头不塌陷
            #self.table.horizontalHeader().setFixedHeight(35)           #设置表列头高度
            #self.table.horizontalHeader().setVisible(False)            #设置隐藏列头
            #self.table.horizontalHeader().setFixedWidth(820)           #设置列标题头所在行，宽度（没啥用）


            #设置表格的滚动调样式：self.table.horizontalScrollBar().setStyleSheet.... ,窗体的也可以设置：self.horizontalScrollBar().setStyleSheet...
            self.table.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
                                                "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                "QScrollBar::handle:hover{background:gray;}"
                                                "QScrollBar::sub-line{background:transparent;}"
                                                "QScrollBar::add-line{background:transparent;}");
            self.table.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                "QScrollBar::handle:hover{background:gray;}"
                                                "QScrollBar::sub-line{background:transparent;}"
                                                "QScrollBar::add-line{background:transparent;}");
            #遍历数据，并形成行索引，列索引；
            item = [(j, c,Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)]
            for v in item:
                  print('行下标%s,列下标%s,值：%s' % (v[1], v[0], list(v[2])[v[0]]))
                  self.table.setItem(v[1], v[0], QTableWidgetItem(str(list(v[2])[v[0]]))) #注意，纯数值，则需要str否则放不进去，不显示
                  self.table.setColumnWidth(v[0], 120)                                    #设置列宽度，列索引，宽度
                  self.table.setRowHeight(v[1], 20)                                       #设置行高度，行索引，高度
                  # 设置入职日期列，居中
                  #print(type(self.table.item(v[1], 2)),v[1])
                  if self.table.item(v[1], 3):
                        self.table.item(v[1], 3).setTextAlignment(Qt.AlignHCenter)
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)

            mainLayout = QHBoxLayout()
            mainLayout.addWidget(self.table)
            self.setLayout(mainLayout)
            self.setGeometry(200,300,600,400)
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())

# 测试循环遍历上面集合，按照下标直接定位每一个元素的值
# data = [{'num': '101', 'name': 'JONES', 'sal': 200, 'date': '1999-10-10', 'sex': '女'},
#         {'num': '102', 'name': 'SITH', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#         {'num': '103', 'name': 'SDF', 'sal': 200, 'date': '1999-12-10', 'sex': '女'},
#         {'num': '104', 'name': 'JSSS', 'sal': 200, 'date': '1999-11-10', 'sex': '女'},
#         {'num': '105', 'name': 'JEEE', 'sal': 200, 'date': '1912-10-10', 'sex': '女'}
#         ]
# print([(j, c, Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)])
# for v in [(j, c, Example.data[c].values()) for j in range(len(Example.data)) for c in range(5)]:
# print('行下标%s,列下标%s,值：%s' % (v[1], v[0], list(v[2])[v[0]]))





'''
Qt.AlignLeft
Qt.AlignRight
Qt.AlignHCenter
Qt.AlignJustify
'''
'''
设置表格的编辑属性：QAbstractItemView.NoEditTriggers：不可编辑

                                    QAbstractItemView.CurrentChanged:改变了即可编辑

                                    QAbstractItemView.DoubleClicked:连续双击即可编辑

                                    QAbstractItemView.SelectedClicked:在被选中的情况下单击一次即可编辑

                                    QAbstractItemView.EditKeyPressed:在按下平台的编辑键那个项目上即可编辑

选择时每次选择一行：myTable.setSelectionBehavior(QAbstractItemView.SelectRows)，

'''