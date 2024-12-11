import json
import os
import csv
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication,QDialog, QTableWidgetItem
from PyQt5 import uic
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.pub.gestione_prenotazioni_gui import Ui_MainWindow
class GestionePrenotazioni(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_connections()
        self.load_server_config()

    def load_ui(self):
        uic.loadUi('gestione_prenotazioni.ui', self)

    def setup_connections(self):
        self.aggiungiPrenotazioneButton.clicked.connect(self.aggiungiPrenotazione)
        self.modificaPrenotazioneButton.clicked.connect(self.modificaPrenotazione)
        self.eliminaPrenotazioneButton.clicked.connect(self.eliminaPrenotazione)
        self.aggiornaElencoButton.clicked.connect(self.load_csv)

    def load_csv(self):
        try:
            with open('db/prenota_tavolo.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.tabellaPrenotazioni.setRowCount(0)
                for row in reader:
                    self.add_row_to_table(row)
        except FileNotFoundError:
            QMessageBox.warning(self, "Errore", "File prenota_tavolo.csv non trovato.")

    def add_row_to_table(self, row):
        row_position = self.tabellaPrenotazioni.rowCount()
        self.tabellaPrenotazioni.insertRow(row_position)
        self.tabellaPrenotazioni.setItem(row_position, 0, QTableWidgetItem(row['id']))
        self.tabellaPrenotazioni.setItem(row_position, 1, QTableWidgetItem(row['cliente']))
        self.tabellaPrenotazioni.setItem(row_position, 2, QTableWidgetItem(row['data']))

    def save_csv(self):
        try:
            with open('db/prenota_tavolo.csv', 'w', newline='') as csvfile:
                fieldnames = ['id', 'cliente', 'data']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in range(self.tabellaPrenotazioni.rowCount()):
                    writer.writerow({
                        'id': self.tabellaPrenotazioni.item(row, 0).text(),
                        'cliente': self.tabellaPrenotazioni.item(row, 1).text(),
                        'data': self.tabellaPrenotazioni.item(row, 2).text()
                    })
        except Exception as e:
            QMessageBox.warning(self, "Errore", f"Errore durante il salvataggio: {e}")

    def load_server_config(self):
        try:
            server_config = loadJSONFromFile('server_address.json')
            self.server_address = server_config['address']
            self.server_port = server_config['port']
        except Exception as e:
            QMessageBox.warning(self, "Errore", f"Errore nel caricamento della configurazione del server: {e}")

    def aggiungiPrenotazione(self):
        # Implement logic to add a reservation
        pass

    def modificaPrenotazione(self):
        # Implement logic to modify a reservation
        pass

    def eliminaPrenotazione(self):
        # Implement logic to delete a reservation
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = GestionePrenotazioni()
    window.show()
    sys.exit(app.exec_())
    import json
import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.pub.gestione_prenotazioni_gui import Ui_GestionePrenotazioni

class GestionePrenotazioniLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestionePrenotazioni()
        self.ui.setupUi(self)  # Passa 'self' per associarlo correttamente all'istanza di QDialog
        
        # Collega i pulsanti alle loro funzioni
        self.ui.aggiornaPrenotazioniButton.clicked.connect(self.aggiornaPrenotazioni)
        self.ui.cancellaPrenotazioneButton.clicked.connect(self.cancellaPrenotazione)
        self.ui.confermaPrenotazioneButton.clicked.connect(self.confermaPrenotazione)

    def aggiornaPrenotazioni(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        
        # Chiamata al server per ottenere le prenotazioni
        response = launchMethod(
            request_constructor_str(None, "GetPrenotazioni"), 
            server_coords['address'], 
            server_coords['port']
        )
        
        # Elabora la risposta e mostra le prenotazioni
        try:
            prenotazioni = json.loads(response).get("result", [])
            self.ui.lista_prenotazioni.clear()  # Pulisce la lista esistente
            for prenotazione in prenotazioni:
                self.ui.lista_prenotazioni.addItem(
                    f"Prenotazione #{prenotazione['id']} - {prenotazione['cliente']} - {prenotazione['data']}"
                )
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Errore", "Impossibile decodificare la risposta del server.")

    def cancellaPrenotazione(self):
        prenotazione_selezionata = self.ui.lista_prenotazioni.currentItem()
        if not prenotazione_selezionata:
            QMessageBox.warning(self, "Errore", "Seleziona una prenotazione da cancellare!")
            return
        
        prenotazione_id = prenotazione_selezionata.text().split("#")[1].split(" - ")[0]
        payload = {"prenotazione_id": prenotazione_id}
        
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        
        # Chiamata al server per cancellare la prenotazione
        response = launchMethod(
            request_constructor_str(payload, "CancellaPrenotazione"),
            server_coords['address'],
            server_coords['port']
        )
        
        # Gestione della risposta
        result = json.loads(response).get("result")
        if result == "OK":
            QMessageBox.information(self, "Successo", "Prenotazione cancellata con successo!")
            self.aggiornaPrenotazioni()
        else:
            QMessageBox.warning(self, "Errore", "Errore durante la cancellazione della prenotazione.")

    def confermaPrenotazione(self):
        prenotazione_selezionata = self.ui.lista_prenotazioni.currentItem()
        if not prenotazione_selezionata:
            QMessageBox.warning(self, "Errore", "Seleziona una prenotazione da confermare!")
            return
        
        prenotazione_id = prenotazione_selezionata.text().split("#")[1].split(" - ")[0]
        payload = {"prenotazione_id": prenotazione_id}
        
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        
        # Chiamata al server per confermare la prenotazione
        response = launchMethod(
            request_constructor_str(payload, "ConfermaPrenotazione"),
            server_coords['address'],
            server_coords['port']
        )
        
        # Gestione della risposta
        result = json.loads(response).get("result")
        if result == "OK":
            QMessageBox.information(self, "Successo", "Prenotazione confermata con successo!")
            self.aggiornaPrenotazioni()
        else:
            QMessageBox.warning(self, "Errore", "Errore durante la conferma della prenotazione.")