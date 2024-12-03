import csv
import json
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.pub.gestione_ordinazioni_gui import Ui_GestioneOrdinazioni

class GestioneOrdinazioniLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneOrdinazioni()
        self.ui.setupUi(self)

        # Load server configuration
        ROOT_DIR = os.path.abspath(os.curdir)
        self.server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Load initial data
        self.loadOrders()

        # Connect buttons to their respective functions
        self.ui.aggiornaTabellaButton.clicked.connect(self.loadOrders)
        self.ui.segnaComeArrivatoButton.clicked.connect(self.markAsArrived)

    def loadOrders(self):
        # Load orders from CSV
        try:
            with open('db/invia_ordine.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.ui.tabellaOrdini.setRowCount(0)
                for row in reader:
                    rowPosition = self.ui.tabellaOrdini.rowCount()
                    self.ui.tabellaOrdini.insertRow(rowPosition)
                    self.ui.tabellaOrdini.setItem(rowPosition, 0, QTableWidgetItem(row['ID']))
                    self.ui.tabellaOrdini.setItem(rowPosition, 1, QTableWidgetItem(row['Tavolo']))
                    self.ui.tabellaOrdini.setItem(rowPosition, 2, QTableWidgetItem(row['Nome']))
                    self.ui.tabellaOrdini.setItem(rowPosition, 3, QTableWidgetItem(row['Tipo']))
                    self.ui.tabellaOrdini.setItem(rowPosition, 4, QTableWidgetItem(row['Prezzo']))
                    self.ui.tabellaOrdini.setItem(rowPosition, 5, QTableWidgetItem(row['Stato']))
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "Il file invia_ordine.csv non è stato trovato.")

    def markAsArrived(self):
        # Mark selected order as arrived
        selected_row = self.ui.tabellaOrdini.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Seleziona un ordine per segnarlo come arrivato.")
            return

        order_id = self.ui.tabellaOrdini.item(selected_row, 0).text()
        self.ui.tabellaOrdini.setItem(selected_row, 5, QTableWidgetItem('1'))

        # Update CSV file
        try:
            with open('db/invia_ordine.csv', 'r', newline='') as csvfile:
                reader = list(csv.DictReader(csvfile))
            with open('db/invia_ordine.csv', 'w', newline='') as csvfile:
                fieldnames = ['ID', 'Tavolo', 'Nome', 'Tipo', 'Prezzo', 'Stato']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['ID'] == order_id:
                        row['Stato'] = '1'
                    writer.writerow(row)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "Il file invia_ordine.csv non è stato trovato.")

def run():
    app = QApplication([])
    dialog = GestioneOrdinazioniLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()