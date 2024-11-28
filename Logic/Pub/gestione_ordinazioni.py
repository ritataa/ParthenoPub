import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import request_constructor_str, launchMethod
from gui.pub.gestione_ordinazioni_gui import Ui_GestioneOrdinazioni


class GestioneOrdinazioniLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneOrdinazioni()
        self.ui.setupUi(self)

        # Connessione al server per ottenere gli ordini
        ordini = json.loads(launchMethod(request_constructor_str(None, "GetOrdini")))
        ordini = ordini['result']

        # Aggiungere gli ordini alla lista dell'interfaccia
        for ordine in ordini:
            self.ui.lista_ordini.addItem(f"Ordine #{ordine['id']} - {ordine['cliente']}")

        # Collega il pulsante per processare l'ordine
        self.ui.processaOrdineButton.clicked.connect(self.processaOrdine)

    def processaOrdine(self):
        # Recupero l'ordine selezionato
        ordine_selezionato = self.ui.lista_ordini.currentItem().text()
        ordine_id = ordine_selezionato.split(" - ")[0].split("#")[1]
        
        payload = {
            "ordine_id": ordine_id,
            "azione": "processa"
        }

        # Invia la richiesta per processare l'ordine
        res = launchMethod(request_constructor_str(payload, 'processaOrdine'))
        res = json.loads(res)
        
        if res["result"] == 'OK':
            QMessageBox.information(None, "Success", "Ordine processato con successo")
        else:
            QMessageBox.warning(None, "Error", "Errore nel processamento dell'ordine")
        
        print(res)

def run():
    dialog = GestioneOrdinazioniLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()