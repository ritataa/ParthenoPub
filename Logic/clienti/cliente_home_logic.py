import json
import os
from PyQt5 import QtWidgets
from gui.clienti.cliente_home_gui import Ui_ClienteHome  # Import the generated UI class
from logic.clienti.gestione_richiesta_menu import GestioneRichiestaMenuLogic
from logic.clienti.gestione_invio_ordine import GestioneInvioOrdineLogic
from logic.clienti.gestione_entrata import GestioneEntrataLogic

def load_server_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'common', 'server_adress.json')
    with open(config_path, 'r') as file:
        return json.load(file)

class ClienteHomeLogic(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ClienteHome()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Load server configuration
        self.server_config = load_server_config()

        # Connect buttons to their respective functions
        self.ui.btn_richiedi_menu.clicked.connect(self.open_richiesta_menu)
        self.ui.btn_invia_ordine.clicked.connect(self.open_invio_ordine)
        self.ui.btn_prenota_entrata.clicked.connect(self.open_prenota_entrata)

    def open_richiesta_menu(self):
        gestione_richiesta_menu = GestioneRichiestaMenuLogic()
        gestione_richiesta_menu.exec_()

    def open_invio_ordine(self):
        gestione_invio_ordine = GestioneInvioOrdineLogic()
        gestione_invio_ordine.exec_()

    def open_prenota_entrata(self):
        gestione_entrata = GestioneEntrataLogic()
        gestione_entrata.exec_()

    def get_current_table_number(self):
    # Implement logic to retrieve the current table number
    # For example, return a hardcoded value or retrieve it from a UI element
        return 1  # Replace with actual logic

def main():
    app = QtWidgets.QApplication([])
    window = ClienteHomeLogic()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()