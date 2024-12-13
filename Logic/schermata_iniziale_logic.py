from PyQt5.QtWidgets import QMainWindow

from Common.communication import find_rows

from gui.schermata_iniziale_gui import Ui_MainWindow
from Logic.Clienti.cliente_home_logic import ClienteHomeLogic
from Logic.Pub.pub_home_login_logic import PubHomeLoginLogic


class MainWindow(QMainWindow):

    user = None
    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clienteButton.clicked.connect(self.showClienteHome)
        self.ui.serverButton.clicked.connect(self.showServerHome)


    def showClienteHome(self,user):
        dialog = ClienteHomeLogic()
        dialog.exec_()

    def showServerHome(self,user):
        dialog = PubHomeLoginLogic()
        dialog.exec_()

def run(user):
    window = MainWindow(user)
    window.show()

if __name__ == "__main__":
    run()