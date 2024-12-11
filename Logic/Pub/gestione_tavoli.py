import sys
import csv
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from gui.pub.gestione_tavoli_gui import Ui_MainWindow
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod

class GestioneTavoliApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Load table data from CSV
        self.load_tavoli_from_csv('db/tavoli.csv')

        # Connect buttons to their respective functions
        self.pushButton.clicked.connect(self.aggiorna_stato)  # Aggiorna Stato
        self.pushButton_2.clicked.connect(self.segna_libero)  # Segna Libero

    def load_tavoli_from_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.tableWidget.setRowCount(0)
                for row in reader:
                    self.add_table_row(row)
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore nel caricamento del file CSV: {e}")

    def add_table_row(self, row):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(row['ID']))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(row['TavoloID']))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(row['NumeroPosti']))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(row['NumeroPersone']))
        stato = "Libero" if row['Stato'] == '0' else "Occupato"
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(stato))

    def aggiorna_stato(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Errore", "Seleziona un tavolo per aggiornare lo stato!")
            return

        stato_item = self.tableWidget.item(selected_row, 4)
        new_stato = "Occupato" if stato_item.text() == "Libero" else "Libero"
        self.tableWidget.setItem(selected_row, 4, QTableWidgetItem(new_stato))

        self.save_tavoli_to_csv('db/tavoli.csv')

    def segna_libero(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Errore", "Seleziona un tavolo per segnarlo come libero!")
            return

        self.tableWidget.setItem(selected_row, 4, QTableWidgetItem("Libero"))
        self.save_tavoli_to_csv('db/tavoli.csv')

    def save_tavoli_to_csv(self, file_path):
        try:
            with open(file_path, mode='w', newline='') as csvfile:
                fieldnames = ['ID', 'TavoloID', 'NumeroPosti', 'NumeroPersone', 'Stato']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in range(self.tableWidget.rowCount()):
                    writer.writerow({
                        'ID': self.tableWidget.item(row, 0).text(),
                        'TavoloID': self.tableWidget.item(row, 1).text(),
                        'NumeroPosti': self.tableWidget.item(row, 2).text(),
                        'NumeroPersone': self.tableWidget.item(row, 3).text(),
                        'Stato': '0' if self.tableWidget.item(row, 4).text() == "Libero" else '1'
                    })
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore nel salvataggio del file CSV: {e}")

    def connect_to_server(self):
        try:
            server_config = loadJSONFromFile('server_address.json')
            response = launchMethod(request_constructor_str(None, "GetTavoli"), server_config['address'], server_config['port'])
            tavoli = json.loads(response).get('result', [])
            # Update the GUI with server data if needed
        except Exception as e:
            QMessageBox.critical(self, "Errore di connessione", f"Impossibile connettersi al server: {e}")

def main():
    app = QApplication(sys.argv)
    window = GestioneTavoliApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()