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