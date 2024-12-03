import json
import os
import csv
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QInputDialog, QMessageBox, QApplication, QTableWidgetItem
from common.communication import loadJSONFromFile
from SelMultiplexClient import launchMethod
from gui.pub.gestione_richieste_clienti_gui import Ui_Form

class GestioneRichiesteClientiLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.pushButton.clicked.connect(self.visualizza_dettagli)
        self.ui.pushButton_2.clicked.connect(self.aggiorna_tabella)

        # Load initial data into the table
        self.carica_dati_tabella()

    def carica_dati_tabella(self):
        # Load data from richiesta_cameriere.csv into the table
        file_path = os.path.join('db', 'richiesta_cameriere.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.ui.tableWidget.setRowCount(0)
            for row in reader:
                row_position = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)
                self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(row['Numero Tavolo']))
                self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(row['Motivo']))
                self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(row['Stato']))
    def aggiorna_tabella(self):
        # Reload data from CSV file
        self.carica_dati_tabella()

    def visualizza_dettagli(self):
        # Show details for the selected row
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            numero_tavolo = self.ui.tableWidget.item(selected_row, 0).text()
            motivo = self.ui.tableWidget.item(selected_row, 1).text()
            stato = self.ui.tableWidget.item(selected_row, 2).text()
            QMessageBox.information(self, "Dettagli Richiesta", f"Numero Tavolo: {numero_tavolo}\nMotivo: {motivo}\nStato: {stato}")

    def segna_come_gestita(self):
        # Mark the selected request as handled
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            numero_tavolo = self.ui.tableWidget.item(selected_row, 0).text()
            file_path = os.path.join('db', 'richiesta_cameriere.csv')
            rows = []
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Numero Tavolo'] == numero_tavolo:
                        row['Stato'] = '1'  # Mark as handled
                    rows.append(row)

            # Write updated data back to CSV
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['Numero Tavolo', 'Motivo', 'Stato']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            self.aggiorna_tabella()
            QMessageBox.information(self, "Successo", "Richiesta segnata come gestita.")

    def invia_richiesta_al_server(self, action, data):
        # Load server configuration
        config = loadJSONFromFile('server_address.json')
        server_address = config['address']
        server_port = config['port']

        # Prepare request data
        request_data = {"action": action, **data}
        request_str = json.dumps(request_data)

        # Send request to server
        response = launchMethod(request_str, server_address, server_port)
        return json.loads(response)

    def run(self):
        self.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = GestioneRichiesteClientiLogic()
    window.run()