from PyQt5.QtWidgets import QMainWindow
from common.communication import formato_data  # Adattato a quanto presente nel progetto
from gui.pub.pub_home_gui import Ui_Pub_Home  # GUI specifica per il Pub
from logic.pub.gestione_clienti import GestioneClienti
from logic.pub.gestione_ordinazioni import GestioneOrdinazioniLogic
from logic.pub.gestione_pagamenti import GestionePagamentiLogic
from logic.pub.gestione_prenotazioni import GestionePrenotazioniLogic
from logic.pub.gestione_tavoli import GestioneTavoliLogic


class PubHomeLogic(QMainWindow):
    user = None  # Per mantenere i dettagli dell'utente

    def __init__(self, user):
        """
        Inizializza la finestra principale della gestione del pub.
        
        Args:
            user: Informazioni sull'utente (ad esempio ID o dati del manager del pub).
        """
        self.user = user
        super().__init__()
        self.ui = Ui_Pub_Home()
        self.ui.setupUi(self)

        # Collegamento dei pulsanti della GUI alle rispettive funzioni
        self.ui.ButtonGestioneClienti.clicked.connect(self.showDialogGestioneClienti)
        self.ui.ButtonGestioneOrdini.clicked.connect(self.showDialogGestioneOrdini)
        self.ui.ButtonGestioneTavoli.clicked.connect(self.showDialogGestioneTavoli)
        self.ui.ButtonGestioneMenu.clicked.connect(self.showDialogGestionePagamenti)
        self.ui.ButtonGestioneMenu.clicked.connect(self.showDialogGestionePrenotazioni)

    def showWindow(self, user):
        """
        Mostra la finestra principale con i dettagli dell'utente.
        
        Args:
            user: Informazioni aggiornate sull'utente.
        """
        self.show()
        self.user = user
        self.ui.LabelUserName.setText(f"Utente: {user['name']}")  # Adattato per mostrare il nome dell'utente
        self.ui.LabelCurrentDate.setText(f"Data: {formato_data()}")

    # Metodi per mostrare i dialog delle diverse funzionalità
    def showDialogGestioneClienti(self):
        """
        Mostra il dialog per la gestione dei clienti.
        """
        dialog = GestioneClienti()
        dialog.exec_()

    def showDialogGestioneOrdini(self):
        """
        Mostra il dialog per la gestione degli ordini.
        """
        dialog = GestioneOrdinazioniLogic()
        dialog.exec_()

    def showDialogGestioneTavoli(self):
        """
        Mostra il dialog per la gestione dei tavoli.
        """
        dialog = GestioneTavoliLogic()
        dialog.exec_()

    def showDialogGestionePagamenti(self):
        """
        Mostra il dialog per la gestione del menu.
        """
        dialog = GestionePagamentiLogic()
        dialog.exec_()

    def showDialogGestionePrenotazioni(self):
        """
        Mostra il dialog per la gestione del menu.
        """
        dialog = GestionePrenotazioniLogic()
        dialog.exec_()

def run(user):
    """
    Funzione per avviare la finestra principale del pub.
    
    Args:
        user: Dettagli dell'utente che avvia l'applicazione.
    """
    window = PubHomeLogic(user)
    window.show()


if __name__ == "__main__":
    # Esempio di chiamata con un utente predefinito
    run({
        "id": "001",
        "name": "Rita",
        "role": "Manager",
        "email": "rita.tammaro@example.com"
    })