# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vcsa-ui01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 701, 101))
        self.groupBox.setObjectName("groupBox")
        self.VCSAPath = QtWidgets.QLineEdit(self.groupBox)
        self.VCSAPath.setGeometry(QtCore.QRect(20, 40, 591, 31))
        self.VCSAPath.setObjectName("VCSAPath")
        self.VCSAPath.setReadOnly(True)
        self.VCSAButton = QtWidgets.QToolButton(self.groupBox)
        self.VCSAButton.setGeometry(QtCore.QRect(620, 40, 61, 31))
        self.VCSAButton.setObjectName("VCSAButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 140, 701, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.InfraPath = QtWidgets.QLineEdit(self.groupBox_2)
        self.InfraPath.setGeometry(QtCore.QRect(20, 40, 591, 31))
        self.InfraPath.setObjectName("InfraPath")
        self.InfraPath.setReadOnly(True)
        self.InfraButton = QtWidgets.QToolButton(self.groupBox_2)
        self.InfraButton.setGeometry(QtCore.QRect(620, 40, 61, 31))
        self.InfraButton.setObjectName("InfraButton")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(530, 260, 191, 71))
        self.createButton.setObjectName("createButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "VCSA-Parameter"))
        self.VCSAButton.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Infra-Parameter"))
        self.InfraButton.setText(_translate("MainWindow", "..."))
        self.createButton.setText(_translate("MainWindow", "Create"))
