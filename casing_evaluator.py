# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casing_evaluator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1071, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1071, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1071, 780))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 60, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(580, 130, 181, 22))
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(580, 80, 181, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 200, 91, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 250, 981, 491))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 40, 239, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(660, 70, 311, 371))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(660, 50, 71, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 70, 611, 371))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 40, 239, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(660, 70, 301, 371))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(660, 50, 71, 16))
        self.label_5.setObjectName("label_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 70, 611, 371))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(200, 40, 239, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(660, 70, 301, 371))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(660, 50, 71, 16))
        self.label_6.setObjectName("label_6")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 70, 611, 371))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(250, 200, 731, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 200, 91, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(800, 90, 171, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 30, 239, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(50, 60, 511, 121))
        self.tableWidget_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 40, 71, 16))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 23))
        self.menubar.setObjectName("menubar")
        self.menushuomign = QtWidgets.QMenu(self.menubar)
        self.menushuomign.setObjectName("menushuomign")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionload_las_data = QtWidgets.QAction(MainWindow)
        self.actionload_las_data.setObjectName("actionload_las_data")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actioncopyright = QtWidgets.QAction(MainWindow)
        self.actioncopyright.setObjectName("actioncopyright")
        self.actiontype_casing_data = QtWidgets.QAction(MainWindow)
        self.actiontype_casing_data.setObjectName("actiontype_casing_data")
        self.menushuomign.addAction(self.actionabout)
        self.menushuomign.addAction(self.actioncopyright)
        self.menubar.addAction(self.menushuomign.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIT油套管快速评价系统"))
        self.label_7.setText(_translate("MainWindow", "开始测井时间"))
        self.label_8.setText(_translate("MainWindow", "结束测井时间"))
        self.pushButton_12.setText(_translate("MainWindow", "载入LAS数据"))
        self.pushButton.setText(_translate("MainWindow", "增加一行"))
        self.pushButton_2.setText(_translate("MainWindow", "删除一行"))
        self.pushButton_7.setText(_translate("MainWindow", "生成描述"))
        self.label.setText(_translate("MainWindow", "损伤统计表"))
        self.label_4.setText(_translate("MainWindow", "损伤描述"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "损伤统计"))
        self.pushButton_4.setText(_translate("MainWindow", "增加一行"))
        self.pushButton_3.setText(_translate("MainWindow", "删除一行"))
        self.pushButton_8.setText(_translate("MainWindow", "生成描述"))
        self.label_2.setText(_translate("MainWindow", "结垢统计表"))
        self.label_5.setText(_translate("MainWindow", "结垢描述"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "结垢统计"))
        self.pushButton_5.setText(_translate("MainWindow", "增加一行"))
        self.pushButton_6.setText(_translate("MainWindow", "删除一行"))
        self.pushButton_9.setText(_translate("MainWindow", "生成描述"))
        self.label_6.setText(_translate("MainWindow", "变形描述"))
        self.label_3.setText(_translate("MainWindow", "变形统计表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "变形统计"))
        self.pushButton_13.setText(_translate("MainWindow", "解析LAS数据"))
        self.pushButton_10.setText(_translate("MainWindow", "生成快速解释结论"))
        self.pushButton_14.setText(_translate("MainWindow", "增加一行"))
        self.pushButton_15.setText(_translate("MainWindow", "删除一行"))
        self.pushButton_16.setText(_translate("MainWindow", "确认输入"))
        self.label_9.setText(_translate("MainWindow", "井身结构表"))
        self.menushuomign.setTitle(_translate("MainWindow", "说明"))
        self.actionload_las_data.setText(_translate("MainWindow", "load las"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actioncopyright.setText(_translate("MainWindow", "copyright"))
        self.actiontype_casing_data.setText(_translate("MainWindow", "casing data"))
