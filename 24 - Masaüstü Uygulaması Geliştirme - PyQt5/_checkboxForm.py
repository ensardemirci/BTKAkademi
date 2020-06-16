# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSecilen = QtWidgets.QPushButton(self.centralwidget)
        self.btnSecilen.setGeometry(QtCore.QRect(110, 250, 151, 61))
        self.btnSecilen.setObjectName("btnSecilen")
        self.lbResult = QtWidgets.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(500, 90, 181, 151))
        self.lbResult.setText("")
        self.lbResult.setObjectName("lbResult")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 50, 141, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.sbKitap = QtWidgets.QCheckBox(self.widget)
        self.sbKitap.setObjectName("sbKitap")
        self.verticalLayout.addWidget(self.sbKitap)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSecilen.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.sbKitap.setText(_translate("MainWindow", "Kİtap"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
