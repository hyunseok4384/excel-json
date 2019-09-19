#pip install simplejson
#pip install openpyxl
#pip install xlrd
#pip install xlwt
#pip install pandas
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import uic
from lib.vcsaui import Ui_MainWindow
import pandas as pd
import simplejson as js
import openpyxl
import sys
import os
from lib.vCenter_Infra_parameter import InfraParamerter
from lib.vCenterDeploy65_parameter import VCSAParameter

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthLock()
        self.initSignal()
        self.InfraSig = None
        self.VCSASig = None
        self.fname1 = None
        self.fname2 = None


    def initAuthLock(self):
        self.createButton.setEnabled(False)

    def initSignal(self):
        self.createButton.clicked.connect(self.createParameter)
        self.VCSAButton.clicked.connect(self.pathSelect1)
        self.InfraButton.clicked.connect(self.pathSelect2)

    @pyqtSlot()
    def createParameter(self):
        try:
            InfraParamerter(self.fname2[0])
        except:
            QMessageBox.about(self,"Fail!!","Infra Parameter is tadasikunai!!!")
            self.VCSAPath.setText(None)
            self.InfraPath.setText(None)
            self.InfraSig = None
            self.VCSASig = None
            self.initAuthLock()

        try:
            VCSAParameter(self.fname1[0])
        except:
            QMessageBox.about(self,"Fail!!","VCSA Parameter is tadasikunai!!!")
            self.VCSAPath.setText(None)
            self.InfraPath.setText(None)
            self.InfraSig = None
            self.VCSASig = None
            self.initAuthLock()
        if self.InfraSig is None and self.VCSASig is None:
            if os.path.isfile(r"C:\VCSA-Parameter\infra_parameter.json"):
                os.remove(r"C:\VCSA-Parameter\infra_parameter.json")
            if os.path.isfile(r"C:\VCSA-Parameter\vcenter6.5_parameter.json"):
                os.remove(r"C:\VCSA-Parameter\vcenter6.5_parameter.json")

        if self.InfraSig is not None and self.VCSASig is not None:
            QMessageBox.about(self,"Success!!","omedetou!!!")
            self.VCSAPath.setText(None)
            self.InfraPath.setText(None)
            self.InfraSig = None
            self.VCSASig = None
            self.initAuthLock()

    @pyqtSlot()
    def pathSelect1(self):
        self.fname1 = QFileDialog.getOpenFileName(self)
        self.VCSAPath.setText(self.fname1[0])
        self.VCSASig = 1
        if self.InfraSig is not None:
            self.createButton.setEnabled(True)

    @pyqtSlot()
    def pathSelect2(self):
        self.fname2 = QFileDialog.getOpenFileName(self)
        self.InfraPath.setText(self.fname2[0])
        self.InfraSig = 1
        if self.VCSASig is not None:
            self.createButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view_main = Main()
    view_main.show()
    app.exec_()
