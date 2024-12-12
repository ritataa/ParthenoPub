import json
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.Clienti.gestione_invio_ordine_client_gui import Ui_MainWindow

class GestioneInvioOrdineLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the button to the `inviaRichiestaCameriere` method
        self.ui.pushButton.clicked.connect(self.inviaRichiestaCameriere)

    def inviaRichiestaCameriere(self):
        """Send a request to the server to call a waiter for the selected table."""
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Get the selected table number from the combo box
        numero_tavolo = int(self.ui.comboBox.currentText())

        # Construct the payload with the selected table number
        payload = {"numero_tavolo": numero_tavolo}
        try:
            res = launchMethod(request_constructor_str(payload, "richiestaCameriere"), server_coords['address'], server_coords['port'])
            res = json.loads(res)

            # Display a message based on the server's response
            if res.get("stato") == 'successo':
                QMessageBox.information(self, "Richiesta Inviata", "Un cameriere è stato chiamato al tavolo!")
            else:
                QMessageBox.warning(self, "Errore", "Impossibile chiamare un cameriere al momento.")

        except Exception as e:
            QMessageBox.warning(self, "Errore", f"Errore nella comunicazione con il server: {e}")

def main():
    import sys
    app = QApplication(sys.argv)
    window = GestioneInvioOrdineLogic()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()