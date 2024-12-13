import json
import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from Common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.Clienti.gestione_richiesta_menu_client_gui import Ui_MainWindow

class GestioneRichiestaMenuLogic(QDialog):
    def __init__(self,table_number):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Store the table number
        self.table_number = table_number


        # Connect buttons to the method with the appropriate menu type
        self.ui.pushButton.clicked.connect(lambda: self.aggiornaMenu("generale"))
        self.ui.pushButton_2.clicked.connect(lambda: self.aggiornaMenu("birra"))
        self.ui.pushButton_3.clicked.connect(lambda: self.aggiornaMenu("dolci"))

    def aggiornaMenu(self, menu_type):
        """Send a request to the server for the specified menu type."""
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        try:
            # Retrieve the selected table number from the comboBox
            table_number = self.table_number

            # Construct the payload with the table number and menu type
            payload = {"numero_tavolo": table_number, "menu_type": menu_type}
            res = launchMethod(request_constructor_str("richiestaMenu", payload), server_coords['address'], server_coords['port'])
            res = json.loads(res)

            if res["stato"] == "successo":
                QMessageBox.information(self, "Successo", f"Richiesta per il menu {menu_type} inviata con successo.")
            else:
                QMessageBox.warning(self, "Errore", res["messaggio"])

        except Exception as e:
            QMessageBox.warning(self, "Errore", f"Impossibile inviare la richiesta: {e}")

def run():

    dialog = GestioneRichiestaMenuLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()