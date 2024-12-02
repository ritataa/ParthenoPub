import json
import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.clienti.gestione_richiesta_menu_client_gui import Ui_GestioneRichiestaMenu

class GestioneRichiestaMenuLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneRichiestaMenu()
        self.ui.setupUi(self)

        # Connect buttons to the method with the appropriate menu type
        self.ui.pushButton.clicked.connect(lambda: self.aggiornaMenu("generale"))
        self.ui.pushButton_2.clicked.connect(lambda: self.aggiornaMenu("birra"))
        self.ui.pushButton_3.clicked.connect(lambda: self.aggiornaMenu("dolci"))

    def aggiornaMenu(self, menu_type):
        """Request the menu from the server and update the list in the GUI."""
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        try:
            # Request the menu from the server
            payload = {"menu_type": menu_type}
            res = launchMethod(request_constructor_str("GetMenu", payload), server_coords['address'], server_coords['port'])
            res = json.loads(res)

            # Update the menu list
            self.ui.lista_menu.clear()
            if "result" in res and isinstance(res["result"], list):
                for item in res["result"]:
                    self.ui.lista_menu.addItem(f"{item['Nome']} - {item['Prezzo']}€")
            else:
                QMessageBox.warning(self, "Errore", f"Impossibile ottenere il menu: {res['result']}")

        except Exception as e:
            QMessageBox.warning(self, "Errore", f"Impossibile aggiornare il menu: {e}")

def run():
    dialog = GestioneRichiestaMenuLogic()
    dialog.exec_()

if __name__ == "__main__":
    run()