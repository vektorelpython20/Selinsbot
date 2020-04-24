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
        self.btTakip.clicked.connect(self.Takip)
        self.show()

    def Takip(self):
        self.selinsBot.KullaniciTakip(self.txtTakip.text())

    def git(self):
        self.selinsBot = SelinsBotCore(self.txtUser.text(),self.txtPass.text())
    
 

    # def HesapWinAc(self):
    #     self.hesapBilgi = HesapBilgi(self)
    #     self.hesapBilgi.Hesap.show()


class SelinsBotCore:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.girisYap()
    
    def girisYap(self):
        self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(4)
        epostaGiris = self.browser.find_element_by_name("username")
        sifreGiris = self.browser.find_element_by_name("password")
        epostaGiris.send_keys(self.username)
        sifreGiris.send_keys(self.password)
        sifreGiris.send_keys(Keys.ENTER)
        #simdi değil
        time.sleep(5)
        giris = self.browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        giris.click() 
    
    def KullaniciTakip(self,kullaniciAdi):
        self.browser.get(f"https://www.instagram.com/{kullaniciAdi}/")
        time.sleep(4)
        takipButton =  self.browser.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if (takipButton.text != ""):
            takipButton.click()
            time.sleep(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())