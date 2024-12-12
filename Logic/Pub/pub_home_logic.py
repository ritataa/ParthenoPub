import os
import csv
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from Common.communication import formato_data
from gui.Pub.pub_home_gui import Ui_GestionePub
from Logic.Pub.gestione_richieste_clienti import GestioneRichiesteClientiLogic
from Logic.Pub.gestione_ordinazioni import GestioneOrdinazioniLogic
from Logic.Pub.gestione_pagamenti import GestionePagamentiLogic
from Logic.Pub.gestione_prenotazioni import GestionePrenotazioniLogic
from Logic.Pub.gestione_tavoli import GestioneTavoliApp

class PubHomeLogic(QMainWindow):
    user = None

    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_GestionePub()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.ButtonGestioneClienti.clicked.connect(self.showDialogGestioneClienti)
        self.ui.ButtonGestioneOrdini.clicked.connect(self.showDialogGestioneOrdini)
        self.ui.ButtonGestioneTavoli.clicked.connect(self.showDialogGestioneTavoli)
        self.ui.ButtonGestioneMenu.clicked.connect(self.showDialogGestionePagamenti)
        self.ui.ButtonGestioneMenu.clicked.connect(self.showDialogGestionePrenotazioni)

        # Load initial data
        self.loadTableData()
        self.loadRequestsData()
        self.loadReservationsData()
        self.loadOrdersData()
        self.loadPaymentsData()

    def loadTableData(self):
        try:
            with open('db/tavoli.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.ui.tabellaTavoli.setRowCount(0)
                for row in reader:
                    rowPosition = self.ui.tabellaTavoli.rowCount()
                    self.ui.tabellaTavoli.insertRow(rowPosition)
                    self.ui.tabellaTavoli.setItem(rowPosition, 0, QTableWidgetItem(row['ID']))
                    self.ui.tabellaTavoli.setItem(rowPosition, 1, QTableWidgetItem(row['Stato']))
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "Il file tavoli.csv non è stato trovato.")

    def loadRequestsData(self):
        # Implement similar logic for loading requests from CSV files
        pass

    def loadReservationsData(self):
        # Implement similar logic for loading reservations from CSV files
        pass

    def loadOrdersData(self):
        # Implement similar logic for loading orders from CSV files
        pass

    def loadPaymentsData(self):
        # Implement similar logic for loading payments from CSV files
        pass

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

    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.LabelUserName.setText(f"Utente: {user['name']}")
        self.ui.LabelCurrentDate.setText(f"Data: {formato_data()}")

def run(user):
    window = PubHomeLogic(user)
    window.show()

if __name__ == "__main__":
    run({
        "id": "001",
        "name": "Rita",
        "role": "Manager",
        "email": "rita.tammaro@example.com"
    })