from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from Common.communication import launchMethod, load_server_address_from_json
import json
import os

class GestionePrenotazioni(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestione Prenotazioni")
        self.setGeometry(100, 100, 400, 300)
        
        # Layout per la finestra
        self.layout = QVBoxLayout()
        
        # Etichetta per visualizzare le informazioni
        self.label = QLabel("Visualizza le prenotazioni:", self)
        self.layout.addWidget(self.label)
        
        # Aggiungi un bottone per interagire con il sistema di prenotazioni
        self.button = QPushButton("Mostra Prenotazioni", self)
        self.button.clicked.connect(self.mostra_prenotazioni)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
    
    def mostra_prenotazioni(self):
        # Carica le configurazioni del server dal file JSON
        ROOT_DIR = os.path.abspath(os.curdir)
        server_address, server_port = load_server_address_from_json(os.path.join(ROOT_DIR, "server_address.json"))
        
        # Chiamata al server per ottenere le prenotazioni
        request_data = {"action": "get_prenotazioni"}  # Esempio di richiesta
        request_str = json.dumps(request_data)  # Converte la richiesta in formato JSON
        
        # Utilizza launchMethod per inviare la richiesta al server
        response = launchMethod(request_str, server_address, server_port)
        
        # Elabora la risposta (assumiamo che sia una lista di prenotazioni)
        prenotazioni = json.loads(response)
        self.mostra_sul_gui(prenotazioni)


    def mostra_sul_gui(self, prenotazioni):
        # Funzione per visualizzare le prenotazioni sul GUI
        prenotazioni_text = "\n".join([f"Prenotazione {i+1}: {p}" for i, p in enumerate(prenotazioni)])
        self.label.setText(f"Prenotazioni:\n{prenotazioni_text}")