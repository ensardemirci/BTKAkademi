from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_topla.clicked.connect(self.Hesapla)
        self.ui.btn_cikar.clicked.connect(self.Hesapla)
        self.ui.btn_carp.clicked.connect(self.Hesapla)
        self.ui.btn_bol.clicked.connect(self.Hesapla)

    def Hesapla(self):
        sender = self.sender()
        print(sender.text())
        result = 0
        if sender.text() == 'Toplam':
            result = float(self.ui.txt_sayi1.text()) + float(self.ui.txt_sayi2.text())
            print(result)
            self.ui.sonuc_lbl.setText(f'Sonuç: {str(result)}')

        elif sender.text() == 'Çıkarma':
            result = float(self.ui.txt_sayi1.text()) - float(self.ui.txt_sayi2.text())
            print(result)
            self.ui.sonuc_lbl.setText(f'Sonuç: {str(result)}')

        elif sender.text() == 'Çarpma':
            result = float(self.ui.txt_sayi1.text()) * float(self.ui.txt_sayi2.text())
            print(result)
            self.ui.sonuc_lbl.setText(f'Sonuç: {str(result)}')

        elif sender.text() == 'Bölme':
            result = float(self.ui.txt_sayi1.text()) / float(self.ui.txt_sayi2.text())
            print(result)
            self.ui.sonuc_lbl.setText(f'Sonuç: {str(result)}')
        else:
            pass



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()