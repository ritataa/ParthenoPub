import csv
import json
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox,QDialog, QTableWidgetItem
from Common.communication import loadJSONFromFile, request_constructor_str 
from gui.Pub.gestione_pagamenti_gui import Ui_MainWindow
from SelMultiplexClient import launchMethod


class GestionePagamentiLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
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
