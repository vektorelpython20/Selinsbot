from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic 
class HesapBilgi(QWidget):
    def __init__(self,parent=None):
        super(HesapBilgi,self).__init__(parent)
        self.Hesap = uic.loadUi(r"UI\HesapForm.ui")
        self.Goster()

    def Goster(self):
        self.Hesap.btIptal.clicked.connect(self.Hesap.close)
        self.Hesap.btGiris.clicked.connect(self.GirisDoldur)
    

    def GirisDoldur(self):
        pass
    
    
    