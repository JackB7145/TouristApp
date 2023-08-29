#Initializing required libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from textToImage import getCountryImage
from translator import translate
from geoInfo import countryData
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
import time

#Defining neccesary variables
last = 0

#Initializing the GUI window
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(621, 1070)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(621, 1070))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 40, 271, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background: #C6D0F9;"
"border-radius : 10%;"
"padding-left: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 390, 161, 261))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(470, 390, 151, 261))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(0, 650, 161, 61))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(470, 650, 151, 61))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(0, 710, 311, 51))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(0, 130, 51, 261))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(570, 130, 51, 261))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(0, 40, 161, 41))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label.setStyleSheet("background-color: #657EE4;\n"
"color: white;\n"
"border-radius : 10%;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_13.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(0, 80, 161, 51))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(160, 80, 311, 51))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(160, 0, 311, 41))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayoutWidget_17 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_17.setGeometry(QtCore.QRect(470, 0, 151, 41))
        self.gridLayoutWidget_17.setObjectName("gridLayoutWidget_17")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayoutWidget_18 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_18.setGeometry(QtCore.QRect(470, 40, 151, 41))
        self.gridLayoutWidget_18.setObjectName("gridLayoutWidget_18")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: #657EE4;\n"
"color: white;\n"
"border-radius : 10%;")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.geoInfo)
        self.gridLayout_18.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayoutWidget_19 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_19.setGeometry(QtCore.QRect(470, 80, 151, 51))
        self.gridLayoutWidget_19.setObjectName("gridLayoutWidget_19")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 621, 261))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/sunset.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(50, 450, 121, 41))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_5.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayoutWidget_20 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_20.setGeometry(QtCore.QRect(50, 500, 121, 41))
        self.gridLayoutWidget_20.setObjectName("gridLayoutWidget_20")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.gridLayoutWidget_20)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_20)
        self.label_6.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_20.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayoutWidget_21 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_21.setGeometry(QtCore.QRect(50, 550, 121, 41))
        self.gridLayoutWidget_21.setObjectName("gridLayoutWidget_21")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.gridLayoutWidget_21)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_21)
        self.label_7.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_21.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayoutWidget_22 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_22.setGeometry(QtCore.QRect(50, 600, 121, 41))
        self.gridLayoutWidget_22.setObjectName("gridLayoutWidget_22")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.gridLayoutWidget_22)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_22)
        self.label_8.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_22.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayoutWidget_23 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_23.setGeometry(QtCore.QRect(50, 650, 133, 41))
        self.gridLayoutWidget_23.setObjectName("gridLayoutWidget_23")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.gridLayoutWidget_23)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_23)
        self.label_9.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_23.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayoutWidget_24 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_24.setGeometry(QtCore.QRect(190, 650, 380, 41))
        self.gridLayoutWidget_24.setObjectName("gridLayoutWidget_24")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.gridLayoutWidget_24)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_24)
        self.label_20.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_24.addWidget(self.label_20, 0, 0, 1, 1)
        self.gridLayoutWidget_25 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_25.setGeometry(QtCore.QRect(190, 500, 380, 41))
        self.gridLayoutWidget_25.setObjectName("gridLayoutWidget_25")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_25)
        self.label_17.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout_25.addWidget(self.label_17, 0, 0, 1, 1)
        self.gridLayoutWidget_27 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_27.setGeometry(QtCore.QRect(190, 600, 380, 41))
        self.gridLayoutWidget_27.setObjectName("gridLayoutWidget_27")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.gridLayoutWidget_27)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_27)
        self.label_19.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_27.addWidget(self.label_19, 0, 0, 1, 1)
        self.gridLayoutWidget_28 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_28.setGeometry(QtCore.QRect(190, 450, 380, 41))
        self.gridLayoutWidget_28.setObjectName("gridLayoutWidget_28")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.gridLayoutWidget_28)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_28)
        self.label_16.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_28.addWidget(self.label_16, 0, 0, 1, 1)
        self.gridLayoutWidget_29 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_29.setGeometry(QtCore.QRect(190, 550, 380, 41))
        self.gridLayoutWidget_29.setObjectName("gridLayoutWidget_29")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.gridLayoutWidget_29)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_29)
        self.label_18.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_29.addWidget(self.label_18, 0, 0, 1, 1)
        self.gridLayoutWidget_30 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_30.setGeometry(QtCore.QRect(310, 710, 311, 51))
        self.gridLayoutWidget_30.setObjectName("gridLayoutWidget_30")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.gridLayoutWidget_30)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayoutWidget_31 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_31.setGeometry(QtCore.QRect(10, 760, 291, 51))
        self.gridLayoutWidget_31.setObjectName("gridLayoutWidget_31")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.gridLayoutWidget_31)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("border-radius : 10%; background: #C6D0F9; padding-left: 10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_31.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.gridLayoutWidget_32 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_32.setGeometry(QtCore.QRect(310, 760, 311, 51))
        self.gridLayoutWidget_32.setObjectName("gridLayoutWidget_32")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.gridLayoutWidget_32)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: #657EE4;\n"
"color: white;\n"
"border-radius : 10%;\n"
"")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.translated)
        self.gridLayout_32.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.gridLayoutWidget_33 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_33.setGeometry(QtCore.QRect(0, 810, 311, 261))
        self.gridLayoutWidget_33.setObjectName("gridLayoutWidget_33")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.gridLayoutWidget_33)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_33)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_33.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayoutWidget_34 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_34.setGeometry(QtCore.QRect(310, 810, 311, 261))
        self.gridLayoutWidget_34.setObjectName("gridLayoutWidget_34")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.gridLayoutWidget_34)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_34)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_34.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.gridLayoutWidget_26 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_26.setGeometry(QtCore.QRect(50, 400, 121, 41))
        self.gridLayoutWidget_26.setObjectName("gridLayoutWidget_26")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.gridLayoutWidget_26)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_26)
        self.label_15.setStyleSheet("background-color: #657EE4;\n"
"border-radius : 10%;\n"
"padding-left: 10%;\n"
"")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_26.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayoutWidget_35 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_35.setGeometry(QtCore.QRect(190, 400, 380, 41))
        self.gridLayoutWidget_35.setObjectName("gridLayoutWidget_35")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.gridLayoutWidget_35)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_35)
        self.label_14.setStyleSheet("background: #657EE4;\n"
"padding-left: 10%;\n"
"border-radius : 10%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_35.addWidget(self.label_14, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your country"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Country:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Travel"))
        self.label_5.setText(_translate("MainWindow", "Capital:"))
        self.label_6.setText(_translate("MainWindow", "Currency:"))
        self.label_7.setText(_translate("MainWindow", "Region:"))
        self.label_8.setText(_translate("MainWindow", "Subregion:"))
        self.label_9.setText(_translate("MainWindow", "Common Language(s): "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your language"))
        self.pushButton_2.setText(_translate("MainWindow", "Translate"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter your text here"))
        self.plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "Once the language is selected the newly translated text will appear here"))
        self.label_15.setText(_translate("MainWindow", "Name: "))

    #Getting and displaying the geogrpahical data
    def geoInfo(self):
        try:    
                #Defining variables
                global last
        
                #Determining if the button has been pressed to quckly
                if time.time() - last > 3 or last == 0:
                        last = time.time()
                        name, capital, currency, region, subregion, lang = countryData(self.lineEdit.text())
                        _translate = QtCore.QCoreApplication.translate
                        self.label_14.setText(_translate("MainWindow", name))
                        self.label_16.setText(_translate("MainWindow", capital))
                        self.label_17.setText(_translate("MainWindow", currency))
                        self.label_18.setText(_translate("MainWindow", region))
                        self.label_19.setText(_translate("MainWindow", subregion))
                        self.label_20.setText(_translate("MainWindow", lang))
                        
                        #Requesting the data
 
                        url = getCountryImage(self.lineEdit.text())
                       
                        image = QImage()
                        image.loadFromData(requests.get(url).content) 
                        self.label_3.setPixmap(QPixmap(image))
                else:
                     print("Cooldown iminent")
                

        except:
             pass

    #Translating text
    def translated(self):
        try:
                #Translating the data and displaying it
                _translate = QtCore.QCoreApplication.translate
                result = translate(self.plainTextEdit.toPlainText(), self.lineEdit_2.text())
                self.plainTextEdit_2.clear()
                self.plainTextEdit_2.insertPlainText(_translate("MainWindow", result))
        except:
             pass

#Luanching and Displaying the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())