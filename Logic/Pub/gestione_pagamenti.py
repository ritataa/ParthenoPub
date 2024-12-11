import csv
import json
import os
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QDialog, QTableWidgetItem
from common.communication import loadJSONFromFile, request_constructor_str 
from gui.pub.gestione_pagamenti_gui import Ui_Gestione_Pagamenti
from SelMultiplexClient import launchMethod


class GestionePagamenti(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestionePagamenti()
        self.ui.setupUi(self)

        # Load server configuration
        self.server_config = self.load_server_config()

        # Load table data
        self.load_table_data()

        # Connect button actions
        self.ui.aggiungiTavoloButton.clicked.connect(self.add_table)
        self.ui.aggiornaStatoButton.clicked.connect(self.update_table_status)

    def load_server_config(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        return loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

    def load_table_data(self):
        conn = sqlite3.connect('db/stato.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stato")
        rows = cursor.fetchall()
        conn.close()

        self.ui.tableWidget.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))

    def add_table(self):
        tavolo_id = self.ui.tavoloIDInput.text()
        numero_persone = self.ui.numeroPersoneInput.text()
        prezzo = self.ui.prezzoInput.text()

        conn = sqlite3.connect('db/aggiungi_tavolo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tavoli (ID, NumeroPersone, Prezzo) VALUES (?, ?, ?)",
                       (tavolo_id, numero_persone, prezzo))
        conn.commit()
        conn.close()

        self.load_table_data()
        QMessageBox.information(self, "Success", "Tavolo aggiunto con successo")

    def update_table_status(self):
        tavolo_id = self.ui.tavoloIDInput.text()
        nuovo_stato = 1 if self.ui.statoCheckbox.isChecked() else 0

        conn = sqlite3.connect('db/stato.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE stato SET Stato = ? WHERE ID = ?", (nuovo_stato, tavolo_id))
        conn.commit()
        conn.close()

        self.load_table_data()
        QMessageBox.information(self, "Success", "Stato del tavolo aggiornato con successo")

    def confermaPagamento(self):
        pagamento_selezionato = self.ui.lista_pagamenti.currentItem().text()
        pagamento_id = pagamento_selezionato.split(" - ")[0].split("#")[1]

        payload = {
            "pagamento_id": pagamento_id,
            "azione": "conferma"
        }

        res = launchMethod(request_constructor_str(payload, 'confermaPagamento'), self.server_config['address'], self.server_config['port'])
        res = json.loads(res)

        if res["result"] == 'OK':
            QMessageBox.information(self, "Success", "Pagamento confermato con successo")
        else:
            QMessageBox.warning(self, "Error", "Errore nella conferma del pagamento")

def run():
    app = QApplication([])
    window = GestionePagamenti()
    window.show()
    app.exec_()

if __name__ == "__main__":
    run() 
    import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import loadJSONFromFile,request_constructor_str # type: ignore
from SelMultiplexClient import launchMethod
from gui.pub.gestione_pagamenti_gui import Ui_GestionePagamenti # type: ignore


class GestionePagamentiLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestionePagamenti()
        self.ui.setupUi(self)

        # Carica la configurazione del server
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Connessione al server per ottenere i pagamenti
        pagamenti = launchMethod(request_constructor_str(None, "GetPagamenti"), server_coords['address'], server_coords['port'])
        pagamenti = json.loads(pagamenti)
        pagamenti = pagamenti['result']

        # Aggiungere i pagamenti alla lista dell'interfaccia
        for pagamento in pagamenti:
            self.ui.lista_pagamenti.addItem(f"Pagamento #{pagamento['id']} - {pagamento['cliente']} - {pagamento['importo']}€")

        # Collega il pulsante per confermare il pagamento
        self.ui.confermaPagamentoButton.clicked.connect(self.confermaPagamento)

    def confermaPagamento(self):
        # Recupero il pagamento selezionato
        pagamento_selezionato = self.ui.lista_pagamenti.currentItem().text()
        pagamento_id = pagamento_selezionato.split(" - ")[0].split("#")[1]
        
        payload = {
            "pagamento_id": pagamento_id,
            "azione": "conferma"
        }

        # Carica la configurazione del server
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Invia la richiesta per confermare il pagamento
        res = launchMethod(request_constructor_str(payload, 'confermaPagamento'), server_coords['address'], server_coords['port'])
        res = json.loads(res)
        
        if res["result"] == 'OK':
            QMessageBox.information(None, "Success", "Pagamento confermato con successo")
        else:
            QMessageBox.warning(None, "Error", "Errore nella conferma del pagamento")
        
        print(res)

def run():
    dialog = GestionePagamentiLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()
