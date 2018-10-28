import sys
from PyQt4 import QtGui
class PrettyWidget(QtGui.QWidget):
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 400,200)
        self.setWindowTitle('Öğrenci Bilgileri')

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        data = {'Adı':['Can','Semih','Büşra','Nevruze','Ayşe'],
                'Soyadı':['YBS','YBS','İktisat','YBS','Sosyal Hizmet'],
                'Bolumu':['Aydın','Yarar','Demirgüreşçi','Karakuş','Gün']}

        table = QtGui.QTableWidget(self)
        table.setRowCount(5)
        table.setColumnCount(3)

        horHeaders=['Adı','Soyadı','Bolumu']
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QtGui.QTableWidgetItem(item)
                table.setItem(m, n, newitem)

        table.setHorizontalHeaderLabels(horHeaders)        

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        grid.addWidget(table, 0,0)     
        self.show()
        
def main():
    app=QtGui.QApplication(sys.argv)
    w=PrettyWidget()
    app.exec_()

if __name__=='__main__':
    main()
