import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.pub.gestione_tavoli_gui import Ui_GestioneTavoli


class GestioneTavoliLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneTavoli()
        self.ui.setupUi(self)

        # Connessione al server per ottenere i tavoli
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        
        # Chiamata al server per ottenere la lista dei tavoli
        response = launchMethod(
            request_constructor_str(None, "GetTavoli"),
            server_coords['address'],
            server_coords['port']
        )
        tavoli = json.loads(response).get('result', [])

        # Aggiungere i tavoli alla lista dell'interfaccia
        for tavolo in tavoli:
            self.ui.lista_tavoli.addItem(f"Tavolo #{tavolo['id']} - {tavolo['stato']}")

        # Collega il pulsante per aggiornare lo stato del tavolo
        self.ui.aggiornaStatoButton.clicked.connect(self.aggiornaStato)

    def aggiornaStato(self):
        # Recupero il tavolo selezionato
        tavolo_selezionato = self.ui.lista_tavoli.currentItem()
        if not tavolo_selezionato:
            QMessageBox.warning(self, "Errore", "Seleziona un tavolo per aggiornare lo stato!")
            return
        
        tavolo_id = tavolo_selezionato.text().split(" - ")[0].split("#")[1]
        
        payload = {
            "tavolo_id": tavolo_id,
            "azione": "aggiorna"
        }

        # Carica le coordinate del server
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Invia la richiesta per aggiornare lo stato del tavolo
        response = launchMethod(
            request_constructor_str(payload, 'aggiornaStatoTavolo'),
            server_coords['address'],
            server_coords['port']
        )

        # Gestione della risposta dal server
        res = json.loads(response)
        
        if res["result"] == 'OK':
            QMessageBox.information(None, "Success", "Stato del tavolo aggiornato con successo")
        else:
            QMessageBox.warning(None, "Error", "Errore nell'aggiornamento dello stato del tavolo")
        
        # A questo punto ricarica i tavoli per mostrare eventuali cambiamenti
        self.aggiornaListaTavoli()

def aggiornaListaTavoli(self):
        # Funzione per ricaricare la lista dei tavoli
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        
        response = launchMethod(
            request_constructor_str(None, "GetTavoli"),
            server_coords['address'],
            server_coords['port']
        )
        tavoli = json.loads(response).get('result', [])
        
        self.ui.lista_tavoli.clear()  # Pulisce la lista esistente
        for tavolo in tavoli:
            self.ui.lista_tavoli.addItem(f"Tavolo #{tavolo['id']} - {tavolo['stato']}")


def run():
    dialog = GestioneTavoliLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()