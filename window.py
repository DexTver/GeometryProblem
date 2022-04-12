# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeometryProblem(object):
    def setupUi(self, GeometryProblem):
        GeometryProblem.setObjectName("GeometryProblem")
        GeometryProblem.setEnabled(True)
        GeometryProblem.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeometryProblem.sizePolicy().hasHeightForWidth())
        GeometryProblem.setSizePolicy(sizePolicy)
        GeometryProblem.setMinimumSize(QtCore.QSize(800, 600))
        GeometryProblem.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(GeometryProblem)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.AngleLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.AngleLayout.setContentsMargins(0, 0, 0, 0)
        self.AngleLayout.setObjectName("AngleLayout")
        self.SecondCoordAngle = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.SecondCoordAngle.setObjectName("SecondCoordAngle")
        self.AngleLayout.addWidget(self.SecondCoordAngle, 0, 2, 1, 1)
        self.FirstCoordAngle = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.FirstCoordAngle.setObjectName("FirstCoordAngle")
        self.AngleLayout.addWidget(self.FirstCoordAngle, 0, 0, 1, 1)
        self.ThirdCoordAngle = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.ThirdCoordAngle.setObjectName("ThirdCoordAngle")
        self.AngleLayout.addWidget(self.ThirdCoordAngle, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.CicleLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.CicleLayout.setContentsMargins(0, 0, 0, 0)
        self.CicleLayout.setObjectName("CicleLayout")
        self.SecondCoordCircle = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.SecondCoordCircle.setObjectName("SecondCoordCircle")
        self.CicleLayout.addWidget(self.SecondCoordCircle, 0, 1, 1, 1)
        self.CenterCoordCircle = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.CenterCoordCircle.setObjectName("CenterCoordCircle")
        self.CicleLayout.addWidget(self.CenterCoordCircle, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.CalculateBut = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateBut.setGeometry(QtCore.QRect(10, 340, 161, 21))
        self.CalculateBut.setObjectName("CalculateBut")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.ScaleSlider = QtWidgets.QSlider(self.centralwidget)
        self.ScaleSlider.setGeometry(QtCore.QRect(180, 510, 191, 22))
        self.ScaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ScaleSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ScaleSlider.setTickInterval(10)
        self.ScaleSlider.setObjectName("ScaleSlider")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 480, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.LeftBut = QtWidgets.QPushButton(self.centralwidget)
        self.LeftBut.setGeometry(QtCore.QRect(400, 480, 51, 51))
        self.LeftBut.setObjectName("LeftBut")
        self.UpBut = QtWidgets.QPushButton(self.centralwidget)
        self.UpBut.setGeometry(QtCore.QRect(450, 480, 51, 25))
        self.UpBut.setObjectName("UpBut")
        self.RightBut = QtWidgets.QPushButton(self.centralwidget)
        self.RightBut.setGeometry(QtCore.QRect(500, 480, 51, 51))
        self.RightBut.setObjectName("RightBut")
        self.DownBut = QtWidgets.QPushButton(self.centralwidget)
        self.DownBut.setGeometry(QtCore.QRect(450, 506, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DownBut.setFont(font)
        self.DownBut.setObjectName("DownBut")
        self.DrawBut = QtWidgets.QPushButton(self.centralwidget)
        self.DrawBut.setGeometry(QtCore.QRect(580, 480, 181, 51))
        self.DrawBut.setObjectName("DrawBut")
        self.AddCircleBut = QtWidgets.QPushButton(self.centralwidget)
        self.AddCircleBut.setGeometry(QtCore.QRect(10, 175, 158, 23))
        self.AddCircleBut.setObjectName("AddCircleBut")
        self.LoadFileBut = QtWidgets.QPushButton(self.centralwidget)
        self.LoadFileBut.setGeometry(QtCore.QRect(10, 210, 158, 41))
        self.LoadFileBut.setObjectName("LoadFileBut")
        self.AddAngleBut = QtWidgets.QPushButton(self.centralwidget)
        self.AddAngleBut.setGeometry(QtCore.QRect(10, 75, 158, 23))
        self.AddAngleBut.setObjectName("AddAngleBut")
        self.WarningLabel = QtWidgets.QLabel(self.centralwidget)
        self.WarningLabel.setGeometry(QtCore.QRect(10, 480, 161, 81))
        self.WarningLabel.setText("")
        self.WarningLabel.setTextFormat(QtCore.Qt.AutoText)
        self.WarningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WarningLabel.setWordWrap(False)
        self.WarningLabel.setObjectName("WarningLabel")
        self.ClearBut = QtWidgets.QPushButton(self.centralwidget)
        self.ClearBut.setGeometry(QtCore.QRect(10, 380, 158, 41))
        self.ClearBut.setObjectName("ClearBut")
        GeometryProblem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GeometryProblem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        GeometryProblem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GeometryProblem)
        self.statusbar.setObjectName("statusbar")
        GeometryProblem.setStatusBar(self.statusbar)

        self.retranslateUi(GeometryProblem)
        QtCore.QMetaObject.connectSlotsByName(GeometryProblem)

    def retranslateUi(self, GeometryProblem):
        _translate = QtCore.QCoreApplication.translate
        GeometryProblem.setWindowTitle(_translate("GeometryProblem", "Geometry"))
        self.label.setText(_translate("GeometryProblem", "Добавить оружность"))
        self.label_2.setText(_translate("GeometryProblem", "Добавить \"широкий\" угол"))
        self.CalculateBut.setText(_translate("GeometryProblem", "Посчитать ответ"))
        self.label_3.setText(_translate("GeometryProblem", "Наибольшая площадь"))
        self.label_4.setText(_translate("GeometryProblem", "Масштаб"))
        self.LeftBut.setText(_translate("GeometryProblem", "<"))
        self.UpBut.setText(_translate("GeometryProblem", "^"))
        self.RightBut.setText(_translate("GeometryProblem", ">"))
        self.DownBut.setText(_translate("GeometryProblem", "⌄"))
        self.DrawBut.setText(_translate("GeometryProblem", "Нарисовать"))
        self.AddCircleBut.setText(_translate("GeometryProblem", "Добавить"))
        self.LoadFileBut.setText(_translate("GeometryProblem", "Загрузить из файла"))
        self.AddAngleBut.setText(_translate("GeometryProblem", "Добавить"))
        self.ClearBut.setText(_translate("GeometryProblem", "Очистить"))
