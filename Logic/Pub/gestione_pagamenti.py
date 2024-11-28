import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import request_constructor_str, launchMethod
from gui.pub.gestione_pagamenti_gui import Ui_GestionePagamenti


class GestionePagamentiLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestionePagamenti()
        self.ui.setupUi(self)

        # Connessione al server per ottenere i pagamenti
        pagamenti = json.loads(launchMethod(request_constructor_str(None, "GetPagamenti")))
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

        # Invia la richiesta per confermare il pagamento
        res = launchMethod(request_constructor_str(payload, 'confermaPagamento'))
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