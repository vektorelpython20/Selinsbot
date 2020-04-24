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
        self.btBirak.clicked.connect(self.TakipBirak)
        self.show()

    def TakipBirak(self):
        self.selinsBot.KullaniciTakipBirak(self.txtTakip.text())

    def Takip(self):
        self.selinsBot.KullaniciTakip(self.txtTakip.text())

    def git(self):
        self.selinsBot = SelinsBotCore(self.txtUser.text(),self.txtPass.text())
    
 

    # def HesapWinAc(self):
    #     self.hesapBilgi = HesapBilgi(self)
    #     self.hesapBilgi.Hesap.show()


class SelinsBotCore:
    def __init__(self,username,password,bekle=4):
        self.username = username
        self.password = password
        self.bekle = bekle
        self.girisYap()
    
    def girisYap(self):
        self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(self.bekle)
        epostaGiris = self.browser.find_element_by_name("username")
        sifreGiris = self.browser.find_element_by_name("password")
        epostaGiris.send_keys(self.username)
        sifreGiris.send_keys(self.password)
        sifreGiris.send_keys(Keys.ENTER)
        #simdi değil
        time.sleep(self.bekle)
        giris = self.browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        giris.click() 
    
    def KullaniciTakip(self,kullaniciAdi):
        self.browser.get(f"https://www.instagram.com/{kullaniciAdi}/")
        time.sleep(self.bekle)
        takipButton =  self.browser.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if (takipButton.text != ""):
            takipButton.click()
            time.sleep(self.bekle)
        else:
            print("Zaten Takipteyiz")


    def KullaniciTakipBirak(self,kullaniciAdi):
        self.browser.get(f"https://www.instagram.com/{kullaniciAdi}/")
        time.sleep(self.bekle)
        takipButton = self.browser.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if (takipButton.text == ""):
            takipButton.click()
            time.sleep(self.bekle)
            dogrulamaButton = self.browser.find_element_by_xpath('//button[text() = "Takibi Bırak"]')
            dogrulamaButton.click()
        self.browser.get(f"https://www.instagram.com/")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())



# self.browser.find_element_by_id()
# <div id="mouseover">
#-----------------
# self.browser.find_element_by_class_name()
#<div class="mouseover">
#-----------------
# self.browser.find_element_by_css_selector()
# self.browser.find_element_by_css_selector("#liste > fieldset > label:nth-child(1)")
# <div id="liste">
#     <fieldset>
#         <label>deneme</label>
#         <label>deneme2</label>
#     </fieldset>
# </div>
# self.browser.find_element_by_css_selector("label[data='deneme']")
# self.browser.find_element_by_css_selector("span[id^='deneme']") # başlamalı
# self.browser.find_element_by_css_selector("li[class$='deneme']") # bitmeli
# self.browser.find_element_by_css_selector("li[class*='deneme']") # içermeli
# <span name="adresbilgisi">
# self.browser.find_element_by_css_name("adresbilgisi")
#<footer> Benimdir </footer>
# self.browser.find_element_by_tag("footer")
# self.browser.find_element_partial_link_text("Ben")
# self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[4]/ul/li[5]/a")


