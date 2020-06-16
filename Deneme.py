import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)
        self.ui.sbKitap.stateChanged.connect(self.show_state)

        self.ui.btnSecilen.clicked.connect(self.getAllC)

    def show_state(self, value):
        cb = self.sender()
        print(cb.text())

    def getAllC(self):
        result = ''
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lbResult.setText(result)



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()