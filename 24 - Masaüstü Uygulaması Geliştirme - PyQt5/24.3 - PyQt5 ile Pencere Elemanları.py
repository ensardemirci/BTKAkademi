import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon('../icon.png'))
    win.setToolTip('My ToolTip')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soyadınız: ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    def clicked(self):
        print(f'{txt_name.text()} {txt_surname.text()} Merhaba')
        print('Butona Tıklandı')

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Kaydet')
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    win.show()
    sys.exit(app.exec_())
window()