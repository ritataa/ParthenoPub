import json
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from Common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.Pub.gestione_ordinazioni_gui import Ui_MainWindow

class GestioneOrdinazioniLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
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
        # Request orders from the server
        try:
            response = launchMethod(request_constructor_str(None, "GetOrdini"), self.server_coords['address'], self.server_coords['port'])
            orders = json.loads(response).get("result", [])

            self.ui.tabellaOrdini.setRowCount(0)
            for order in orders:
                rowPosition = self.ui.tabellaOrdini.rowCount()
                self.ui.tabellaOrdini.insertRow(rowPosition)
                self.ui.tabellaOrdini.setItem(rowPosition, 0, QTableWidgetItem(order['ID']))
                self.ui.tabellaOrdini.setItem(rowPosition, 1, QTableWidgetItem(order['Tavolo']))
                self.ui.tabellaOrdini.setItem(rowPosition, 2, QTableWidgetItem(order['Nome']))
                self.ui.tabellaOrdini.setItem(rowPosition, 3, QTableWidgetItem(order['Tipo']))
                self.ui.tabellaOrdini.setItem(rowPosition, 4, QTableWidgetItem(order['Prezzo']))
                self.ui.tabellaOrdini.setItem(rowPosition, 5, QTableWidgetItem(order['Stato']))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Errore nel caricamento degli ordini: {e}")

    def markAsArrived(self):
        # Mark selected order as arrived
        selected_row = self.ui.tabellaOrdini.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Seleziona un ordine per segnarlo come arrivato.")
            return

        order_id = self.ui.tabellaOrdini.item(selected_row, 0).text()
        self.ui.tabellaOrdini.setItem(selected_row, 5, QTableWidgetItem('1'))

        # Send update to the server
        payload = {"order_id": order_id, "stato": "1"}
        try:
            response = launchMethod(request_constructor_str(payload, "AggiornaOrdine"), self.server_coords['address'], self.server_coords['port'])
            result = json.loads(response).get("result")

            if result == "OK":
                QMessageBox.information(self, "Successo", "Ordine aggiornato con successo!")
            else:
                QMessageBox.warning(self, "Errore", "Errore nell'aggiornamento dell'ordine.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Errore nella comunicazione con il server: {e}")

def run():
    app = QApplication([])
    dialog = GestioneOrdinazioniLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()