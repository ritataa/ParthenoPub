from PyQt5.QtWidgets import QMainWindow

from Common.communication import formato_data
from gui.Clienti.cliente_home_gui import Ui_ClienteHome 
from Logic.Clienti.gestione_richiesta_menu import GestioneRichiestaMenuLogic
from Logic.Clienti.gestione_invio_ordine import GestioneInvioOrdineLogic
from Logic.Clienti.gestione_entrata import GestioneEntrataLogic


class ClienteHomeLogic(QMainWindow):
    user = None

    def __init__(self,user):
        self.user = user
        super().__init__()
        self.ui = Ui_ClienteHome()  
        self.ui.setupUi(self)  

        self.ui.pushButton_richiedi_menu.clicked.connect(self.showRichiestaMenu)
        self.ui.pushButton_prenota_entrata.clicked.connect(self.showPrenotaEntrata)
        self.ui.pushButton_invia_ordine.clicked.connect(self.showInviaOrdine)


    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.MtrLabel.setText(user[0])
        self.ui.NameLastnameLabel.setText(f"{user[1]}, {user[2]}")
        self.ui.DateLabel.setText(f"{formato_data()}")

    def showRichiestaMenu(self):
        dialog = GestioneRichiestaMenuLogic()
        dialog.exec_()


    def showPrenotaEntrata(self):
        dialog = GestioneEntrataLogic()
        dialog.exec_()

    def showInviaOrdine(self):
        dialog = GestioneInvioOrdineLogic()
        dialog.exec_()



def run(user):
    window = ClienteHomeLogic(user)
    window.show()

if __name__ == "__main__":
    run()