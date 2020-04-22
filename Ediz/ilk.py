import time
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Goster()
    def Goster(self):
        self.setGeometry(100,100,400,400)
        dugme = QPushButton("   Aç ",self)
        dugme.clicked.connect(self.git)
        self.show()

    def git(self):
        self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")
        self.browser.get("https://www.instagram.com")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())