from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget, QHeaderView, QPushButton, QTableWidgetItem, QFrame
import sys
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QSize


class win(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('表格学习')
        titles = ['编号', '姓名', '工资', '入职日期', ' 性别']
        self.table = QTableWidget(self)  # 创建空表格
        self.table.resize(450, 300)
        # self.table = QTableWidget(4,3,self)  #创建4行3列的表格
        self.table.setRowCount(9)  # 设置行数--不包括标题列
        self.table.setColumnCount(5)  # 设置列数
        self.table.setHorizontalHeaderLabels(titles)  # 标题列---水平标题
        # 参数 标题列表
        # self.table.setVerticalHeaderLabels(titles)  # 标题列---垂直标题

        # self.table.horizontalHeader().setStyleSheet("background-color: blue")#表格头添加背景颜色
        # 没有效果  ？？？

        self.table.setEditTriggers(QTableWidget.AnyKeyPressed)  # 单元格用户能否、如何编辑
        # QTableWidget.NoEditTriggers   单元格用户不可编辑
        # QTableWidget.DoubleClicked    连续双击即可编辑
        # QTableWidget.SelectedClicked  在被选中的情况下单击一次即可编辑
        # QTableWidget.CurrentChanged    选中的单元格改变了即可编辑
        # QTableWidget.AnyKeyPressed   按下任何符号键即可编辑

        self.table.setSelectionBehavior(QTableWidget.SelectItems)  # 设置选中行
        # 鼠标点选时，默认选中一个单元格---QTableWidget.SelectItems
        # QTableWidget.SelectRows   鼠标点击选中一行
        # QTableWidget.SelectColumns  鼠标点击选中一列

        self.table.setAlternatingRowColors(True)  # 行是否自动变色

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置列宽的适应方式
        # QHeaderView.Stretch   拉伸--表格总宽度充满表格
        # QHeaderView.Fixed    固定宽度
        # QHeaderView.ResizeToContents    适应内容

        s = self.table.columnCount()  # 返回列数

        QTableWidget.resizeRowsToContents(self.table)  # 设置行高与内容匹配
        # QTableWidget.resizeColumnsToContents(self.table)

        # self.table.horizontalHeader().setFixedHeight(50)  # 设置表列头高度
        # self.table.horizontalHeader().setFixedWidth(820)  # 设置列宽（没啥用）

        # self.table.setColumnWidth(1, 350)   #设置某列的宽度
        # setSectionResizeMode 设置后,这个指令无效

        # self.table.setRowHeight(0, 120)  #设置某行的高度

        self.table.horizontalHeader().setVisible(True)  # 水平表格头是否隐藏
        # self.table.verticalHeader().setVisible(False)  #垂直表格头是否隐藏

        lb = QPushButton('按钮')
        # self.table.setCellWidget(0, 1, lb)  #在指定单元格内放置控件
        # 0行1列----不包括标题头

        newItem = QTableWidgetItem('1')  # 创建表格项---文本项目
        self.table.setItem(0, 0, newItem)  # 给指定单元格设置数据
        newItem = QTableWidgetItem('12')
        self.table.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('123')
        self.table.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('1234')
        self.table.setItem(3, 0, newItem)
        newItem = QTableWidgetItem('12')
        self.table.setItem(4, 0, newItem)

        pb = QPushButton('测试按钮', self)
        pb.move(50, 470)
        pb.clicked.connect(self.AA)

        self.table.hideRow(1)  # 隐藏指定行
        self.table.showRow(1)  # 显示指定行

        item = self.table.item(1, 0)  # 返回指定单元格的对象
        s = self.table.item(1, 0).text()  # 返回指定单元格的文本内容
        item.setForeground(QBrush(QColor(255, 0, 0)))  # 设置指定单元格的前景色
        item.setBackground(QColor(250, 0, 0))  # 设置指定单元格的背景景色

        item.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)  # 给指定单元格设置对齐方式

        # self.table.sortItems(0, Qt.DescendingOrder)  #指定列排序
        # 参数1  列序号
        # 参数2  Qt.DescendingOrder   降序；Qt.AscEndingOrder  升序

        headItem = self.table.horizontalHeaderItem(1)  # 获取指定列的标题项的对象
        s = self.table.horizontalHeaderItem(1).text()  # 获取指定列的标题文本内容
        headItem.setFont(QFont("黑体", 14, QFont.Bold))  # 给指定列的标题设置字体
        headItem.setForeground(QBrush(Qt.blue))  # 给指定列的标题设置文本颜色

        headItem.setBackground(QColor(0, 0, 250))  # 给指定列的标题设置背景颜色
        # 没有效果  ？？？

        items = self.table.findItems('12', Qt.MatchExactly)  # 寻找
        # Qt.MatchContains   只要包含指定文本的就算
        # Qt.MatchExactly    完全匹配才算
        # 返回值：满足条件的单元格对象的列表
        item = items[0]
        item.setSelected(False)  # 设置指定单元格是否选中
        s = item.row()  # 返回单元格对象的行号

        # self.table.setSpan(2, 0, 4, 1)  #合并单元格
        # 2行0列开始，占据4行1列

        font = self.table.horizontalHeader().font()  # 获取水平标题头的字体
        font.setBold(True)
        font.setPointSize(13)
        self.table.horizontalHeader().setFont(font)  # 给水平标题头设置字体
        # headItem.setFont已经设置过的好像不起效果【特异性原则】

        # self.table.setFrameShape(QFrame.NoFrame)  # 设置表格外层无边框
        # self.table.setShowGrid(False)  # 是否显示单元格网格线,False 则不显示
        # self.table.horizontalHeader().setHighlightSections(True)  # 设置表格列头是否塌陷
        # 看不出效果   ？？？

        newItem = QTableWidgetItem(QIcon("./大象.png"), "大象")  # 创建表格项---图片项目
        # 参数2  描述
        self.table.setIconSize(QSize(100, 100))  # 设置图片大小
        newItem.setFlags(Qt.ItemIsEnabled)  # 用户点击表格时，图片被选中
        self.table.setColumnWidth(2, 100)  # 设置指定列的列宽
        self.table.setRowHeight(2, 100)  # 设置指定行的行高
        self.table.setItem(2, 2, newItem)  # 给指定单元格设置图片项

        # self.table.clear()  #清除所有数据--包括标题头
        self.table.clearContents()  # 清除所有数据--不包括标题头

        print(s)

    def AA(self):
        s = self.table.currentRow()  # 返回当前行序号
        # self.table.insertRow(s)  #在指定行的上面插入一行
        # self.table.removeRow(s)   #删除指定行

        s = self.table.currentColumn()  # 返回当前列序号
        # self.table.insertColumn(s)  #在指定列的前面插入一列
        # self.table.removeColumn(s)  #删除指定列

        print(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(app.exec_())