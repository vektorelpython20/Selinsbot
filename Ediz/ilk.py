import time
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#------------------------------------------
# from Hesap import HesapBilgi

class Uygulama(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"UI\AnaMenu.ui",self)
        self.Goster()       

              
    def Goster(self):
        self.btTarayici.clicked.connect(self.git)
        # self.actionHesap_Bilgileri.triggered.connect(self.HesapWinAc)
        self.show()



    # def HesapWinAc(self):
    #     self.hesapBilgi = HesapBilgi(self)
    #     self.hesapBilgi.Hesap.show()


    def git(self):
        self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(4)
        eposta = self.txtUser.text()
        sifre = self.txtPass.text()
        epostaGiris = self.browser.find_element_by_name("username")
        sifreGiris = self.browser.find_element_by_name("password")

        epostaGiris.send_keys(eposta)
        sifreGiris.send_keys(sifre)
        sifreGiris.send_keys(Keys.ENTER)
        time.sleep(5)
        time.sleep()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())