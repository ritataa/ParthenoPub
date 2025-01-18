from PyQt5.QtWidgets import QMainWindow

from gui.Pub.pub_home_gui import Ui_GestionePub
from Logic.Pub.gestione_richieste_clienti import GestioneRichiesteClientiLogic
from Logic.Pub.gestione_ordinazioni import GestioneOrdinazioniLogic
from Logic.Pub.gestione_pagamenti import GestionePagamentiLogic
from Logic.Pub.gestione_prenotazioni import GestionePrenotazioniLogic
from Logic.Pub.gestione_tavoli import GestioneTavoliApp
from Logic.Pub.gestione_ordini_cameriere import GestioneOrdiniCameriere
class PubHomeLogic(QMainWindow):
    user = None

    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_GestionePub()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.btn_richieste_clienti.clicked.connect(self.showDialogGestioneClienti)
        self.ui.btn_ordinazioni.clicked.connect(self.showDialogGestioneOrdini)
        self.ui.btn_visualizza_tavoli.clicked.connect(self.showDialogGestioneTavoli)
        self.ui.btn_pagamenti.clicked.connect(self.showDialogGestionePagamenti)
        self.ui.btn_visualizza_prenotazioni.clicked.connect(self.showDialogGestionePrenotazioni)
        self.ui.btn_cameriere.clicked.connect(self.showDialogGestioneCameriere)
        


    def showWindow(self):
        self.show()

    def showDialogGestioneClienti(self):
        dialog = GestioneRichiesteClientiLogic()
        dialog.exec_()

    def showDialogGestioneOrdini(self):
        dialog = GestioneOrdinazioniLogic()
        dialog.exec_()

    def showDialogGestioneTavoli(self):
        dialog = GestioneTavoliApp()
        dialog.exec_()

    def showDialogGestionePagamenti(self):
        dialog = GestionePagamentiLogic()
        dialog.exec_()

    def showDialogGestionePrenotazioni(self):
        dialog = GestionePrenotazioniLogic()
        dialog.exec_()

    def showDialogGestioneCameriere(self):
        dialog = GestioneOrdiniCameriere()
        dialog.exec_()


def run(user):
    window = PubHomeLogic(user)
    window.show()

if __name__ == "__main__":
    run('["1", "parthenopub","1234"]')