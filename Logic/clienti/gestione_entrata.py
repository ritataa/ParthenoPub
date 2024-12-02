import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.clienti.gestione_entrata_client_gui import Ui_Gestione_Entrata


class GestioneEntrataLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Gestione_Entrata()
        self.ui.setupUi(self)

        # Connect the button to the `chiediEntrata` method
        self.ui.buttonBox.accepted.connect(self.chiediEntrata)

    def chiediEntrata(self):
        """Send a request to the server to check table availability."""
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Get the number of people from the combo box
        numero_persone = int(self.ui.comboBox_2.currentText())

        # Construct the payload with the selected number of people
        payload = {"numero_persone": numero_persone}
        res = launchMethod(request_constructor_str(payload, "richiestaEntrata"), server_coords['address'], server_coords['port'])
        res = json.loads(res)

        # Display a message based on the server's response
        if res["stato"] == 'accettata':
            QMessageBox.information(self, "Entrata Accettata", "C'è un tavolo disponibile!")
        else:
            QMessageBox.warning(self, "Entrata Rifiutata", "Non ci sono tavoli disponibili al momento.")

def run():
    dialog = GestioneEntrataLogic()
    dialog.exec_()


if __name__ == "__main__":
    run()
