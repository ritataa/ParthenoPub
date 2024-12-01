import json
import os

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QInputDialog, QMessageBox
from common.communication import loadJSONFromFile
from SelMultiplexClient import launchMethod
from gui.pub.gestione_clienti_gui import Ui_GestioneClienti

class GestioneClienti(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneClienti()
        self.ui.setupUi(self)

        # Collega i pulsanti alle loro rispettive funzioni
        self.ui.button_mostra.clicked.connect(self.mostra_clienti)
        self.ui.button_aggiungi.clicked.connect(self.aggiungi_cliente)
        self.ui.button_modifica.clicked.connect(self.modifica_cliente)

    def mostra_clienti(self):
        # Carica le configurazioni del server dal file JSON
        ROOT_DIR = os.path.abspath(os.curdir)
        server_address, server_port = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Chiamata al server per ottenere i clienti
        request_data = {"action": "get_clienti"}  # Esempio di richiesta
        request_str = json.dumps(request_data)  # Converte la richiesta in formato JSON

        # Utilizza launchMethod per inviare la richiesta al server
        response = launchMethod(request_str, server_address, server_port)

        # Elabora la risposta (assumiamo che sia una lista di clienti)
        clienti = json.loads(response)
        self.mostra_sul_gui(clienti)

    def mostra_sul_gui(self, clienti):
        # Funzione per visualizzare i clienti sulla GUI
        self.lista_clienti.clear()  # Pulisce la lista esistente
        for cliente in clienti:
            self.lista_clienti.addItem(f"{cliente['nome']} {cliente['cognome']}")

    def aggiungi_cliente(self):
        # Finestra per inserire un nuovo cliente
        nome, ok_nome = QInputDialog.getText(self, 'Aggiungi Cliente', 'Inserisci il nome del cliente:')
        cognome, ok_cognome = QInputDialog.getText(self, 'Aggiungi Cliente', 'Inserisci il cognome del cliente:')

        if ok_nome and ok_cognome:
            # Dati del cliente da inviare al server
            request_data = {"action": "aggiungi_cliente", "nome": nome, "cognome": cognome}
            request_str = json.dumps(request_data)

            # Carica le configurazioni del server
            ROOT_DIR = os.path.abspath(os.curdir)
            server_address, server_port = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

            # Invia la richiesta al server per aggiungere il cliente
            response = launchMethod(request_str, server_address, server_port)
            result = json.loads(response)

            if result["result"] == "OK":
                QMessageBox.information(self, "Success", "Cliente aggiunto con successo")
                self.mostra_clienti()  # Ricarica la lista clienti
            else:
                QMessageBox.warning(self, "Error", "Errore nell'aggiunta del cliente")

    def modifica_cliente(self):
        # Verifica se è selezionato un cliente nella lista
        cliente_selezionato = self.lista_clienti.currentItem()
        if cliente_selezionato:
            cliente_info = cliente_selezionato.text()
            # Estrai nome e cognome dal testo (supponiamo il formato "Nome Cognome")
            nome, cognome = cliente_info.split(" ")

            # Finestra per modificare i dati del cliente
            nuovo_nome, ok_nome = QInputDialog.getText(self, 'Modifica Cliente', 'Modifica il nome del cliente:', text=nome)
            nuovo_cognome, ok_cognome = QInputDialog.getText(self, 'Modifica Cliente', 'Modifica il cognome del cliente:', text=cognome)

            if ok_nome and ok_cognome:
                # Dati modificati del cliente da inviare al server
                request_data = {"action": "modifica_cliente", "nome": nuovo_nome, "cognome": nuovo_cognome}
                request_str = json.dumps(request_data)

                # Carica le configurazioni del server
                ROOT_DIR = os.path.abspath(os.curdir)
                server_address, server_port = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

                # Invia la richiesta al server per modificare il cliente
                response = launchMethod(request_str, server_address, server_port)
                result = json.loads(response)

                if result["result"] == "OK":
                    QMessageBox.information(self, "Success", "Cliente modificato con successo")
                    self.mostra_clienti()  # Ricarica la lista clienti
                else:
                    QMessageBox.warning(self, "Error", "Errore nella modifica del cliente")
        else:
            QMessageBox.warning(self, "Error", "Seleziona un cliente da modificare")

def run():
    dialog = GestioneClienti()
    dialog.exec_()

if __name__ == "__main__":
    run()