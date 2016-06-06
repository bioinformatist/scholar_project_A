# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainMainWindow(object):
    def setupUi(self, mainMainWindow):
        mainMainWindow.setObjectName("mainMainWindow")
        mainMainWindow.resize(650, 381)
        self.centralwidget = QtWidgets.QWidget(mainMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.minTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.minTextEdit.setGeometry(QtCore.QRect(220, 30, 111, 31))
        self.minTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.minTextEdit.setObjectName("minTextEdit")
        self.intervalLabel = QtWidgets.QLabel(self.centralwidget)
        self.intervalLabel.setGeometry(QtCore.QRect(98, 32, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.intervalLabel.setFont(font)
        self.intervalLabel.setObjectName("intervalLabel")
        self.posNegCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.posNegCheckBox.setGeometry(QtCore.QRect(220, 170, 281, 16))
        self.posNegCheckBox.setObjectName("posNegCheckBox")
        self.toLabel = QtWidgets.QLabel(self.centralwidget)
        self.toLabel.setGeometry(QtCore.QRect(340, 39, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.maxTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.maxTextEdit.setGeometry(QtCore.QRect(360, 30, 121, 31))
        self.maxTextEdit.setObjectName("maxTextEdit")
        self.createPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createPushButton.setGeometry(QtCore.QRect(494, 32, 91, 23))
        self.createPushButton.setObjectName("createPushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(220, 110, 111, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 140, 131, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.problemNumSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.problemNumSpinBox.setGeometry(QtCore.QRect(220, 70, 42, 22))
        self.problemNumSpinBox.setProperty("value", 20)
        self.problemNumSpinBox.setObjectName("problemNumSpinBox")
        self.problemNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.problemNumLabel.setGeometry(QtCore.QRect(30, 70, 181, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.problemNumLabel.setFont(font)
        self.problemNumLabel.setObjectName("problemNumLabel")
        self.problemOutputTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.problemOutputTextEdit.setGeometry(QtCore.QRect(220, 200, 271, 151))
        self.problemOutputTextEdit.setObjectName("problemOutputTextEdit")
        self.problemOutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.problemOutputLabel.setGeometry(QtCore.QRect(90, 200, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.problemOutputLabel.setFont(font)
        self.problemOutputLabel.setObjectName("problemOutputLabel")
        mainMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainMainWindow)
        self.statusbar.setObjectName("statusbar")
        mainMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainMainWindow)
        self.createPushButton.clicked.connect(mainMainWindow.create_problem)
        QtCore.QMetaObject.connectSlotsByName(mainMainWindow)

    def retranslateUi(self, mainMainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainMainWindow.setWindowTitle(_translate("mainMainWindow", "MainWindow"))
        self.minTextEdit.setHtml(_translate("mainMainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8c8c8c;\">最小值 (minimum)</span></p></body></html>"))
        self.intervalLabel.setText(_translate("mainMainWindow", "区间 (Interval)："))
        self.posNegCheckBox.setText(_translate("mainMainWindow", "结果中包含负数 (Containing negtive results)"))
        self.toLabel.setText(_translate("mainMainWindow", "~"))
        self.maxTextEdit.setHtml(_translate("mainMainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8c8c8c;\">最大值（maximum）</span></p></body></html>"))
        self.createPushButton.setText(_translate("mainMainWindow", "生成 (Create)"))
        self.radioButton.setText(_translate("mainMainWindow", "加法 (Addition)"))
        self.radioButton_2.setText(_translate("mainMainWindow", "减法 (Subtraction)"))
        self.problemNumLabel.setText(_translate("mainMainWindow", "题目个数 (Problem Number)："))
        self.problemOutputLabel.setText(_translate("mainMainWindow", "题目 (Problems)："))
