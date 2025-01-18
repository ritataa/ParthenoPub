import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.schermata_iniziale_gui import Ui_MainWindow
from Logic.Clienti.cliente_home_logic import ClienteHomeLogic
from Logic.Pub.pub_home_login_logic import PubHomeLoginLogic

class MainWindow(QMainWindow):
    show_clienti_home = pyqtSignal()
    show_pub_home = pyqtSignal()
    user = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clienteButton.clicked.connect(self.showClienteHome)
        self.ui.serverButton.clicked.connect(self.showServerHome)

    def showClienteHome(self):
        self.show_clienti_home.emit()

    def showServerHome(self):
        self.show_pub_home.emit()

def run():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Collegare i segnali per aprire le rispettive finestre
    window.show_clienti_home.connect(lambda: ClienteHomeLogic(window.user).show())
    window.show_pub_home.connect(lambda: PubHomeLoginLogic(window.user).show())

    window.show()
    app.exec_()

if __name__ == "__main__":
    run()