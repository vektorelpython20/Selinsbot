import time
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#------------------------------------------
from Hesap import HesapBilgi

class Uygulama(QMainWindow):
    loginBilgi = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        uic.loadUi(r"UI\AnaMenu.ui",self)  
        self.Goster()       

              
    def Goster(self):
        self.actionHesap_Bilgileri.triggered.connect(self.HesapWinAc)
        self.loginBilgi.emit(["1","12123"])
        self.show()

    def HesapWinAc(self):
        self.hesapBilgi.Hesap.show()


    def git(self):
        self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
        self.browser.get("https://www.instagram.com")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())