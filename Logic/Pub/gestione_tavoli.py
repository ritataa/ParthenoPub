import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import request_constructor_str, launchMethod
from gui.pub.gestione_tavoli_gui import Ui_GestioneTavoli


class GestioneTavoliLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneTavoli()
        self.ui.setupUi(self)

        # Connessione al server per ottenere i tavoli
        tavoli = json.loads(launchMethod(request_constructor_str(None, "GetTavoli")))
        tavoli = tavoli['result']

        # Aggiungere i tavoli alla lista dell'interfaccia
        for tavolo in tavoli:
            self.ui.lista_tavoli.addItem(f"Tavolo #{tavolo['id']} - {tavolo['stato']}")

        # Collega il pulsante per aggiornare lo stato del tavolo
        self.ui.aggiornaStatoButton.clicked.connect(self.aggiornaStato)

    def aggiornaStato(self):
        # Recupero il tavolo selezionato
        tavolo_selezionato = self.ui.lista_tavoli.currentItem().text()
        tavolo_id = tavolo_selezionato.split(" - ")[0].split("#")[1]
        
        payload = {
            "tavolo_id": tavolo_id,
            "azione": "aggiorna"
        }

        # Invia la richiesta per aggiornare lo stato del tavolo
        res = launchMethod(request_constructor_str(payload, 'aggiornaStatoTavolo'))
        res = json.loads(res)
        
        if res["result"] == 'OK':
            QMessageBox.information(None, "Success", "Stato del tavolo aggiornato con successo")
        else:
            QMessageBox.warning(None, "Error", "Errore nell'aggiornamento dello stato del tavolo")
        
        print(res)

def run():
    dialog = GestioneTavoliLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()