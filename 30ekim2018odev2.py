import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
uyg= QApplication(sys.argv)
pencere=QWidget()
izgara=QGridLayout()
class devirHizi(QDialog):
    def __init__(self,ebeveyn=None):
        super(devirHizi,self).__init__(ebeveyn)
        grid=QGridLayout()
        grid.addWidget(QLabel("Toplam İşten Ayrılan Personel Sayısı:"),0,0)
        self.cikPerSayi=QLineEdit()
        grid.addWidget(self.cikPerSayi,0,1)
        grid.addWidget(QLabel("Aylık Çalışan Sayısı Toplamı:"),1,0)
        
        self.aylikCaSayi=QLineEdit()
        grid.addWidget(self.aylikCaSayi,1,1)
        grid.addWidget(QLabel("Hesaplanmak İstenilen Ay:"),2,0)
        self.ay=QSpinBox()
        self.ay.setRange(1,12)
        self.ay.setValue(1)
        grid.addWidget(self.ay,2,1)
        grid.addWidget(QLabel("Turn Over Sonuç:"),3,0)
        self.ortCalisan=QLabel("")
        grid.addWidget(self.ortCalisan,3,1)
        hesaplaDugme=QPushButton("Hesapla")
        grid.addWidget(hesaplaDugme,4,1)
        self.connect(hesaplaDugme,SIGNAL("pressed()"),self.hesapla)
        self.setLayout(grid)
        self.setWindowTitle("Turn Over")
        self.resize(250,150)
    def hesapla(self):
        isAyPer=int(self.cikPerSayi.text())
        ayCalisan=int(self.aylikCaSayi.text())
        aylar=int(self.ay.text())
        ort=ayCalisan/aylar
        turnOver=isAyPer/ort*100
        self.ortCalisan.setText('<font color="blue"><b>%0.1f</b></font>'%turnOver)
        
uygulama=QApplication([])
pencere=devirHizi()
pencere.show()
uyg.exec_()
