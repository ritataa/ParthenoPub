import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from gui.schermata_iniziale_gui import Ui_MainWindow
import Logic.Clienti.cliente_home_logic as cliente_logic
import Logic.Pub.pub_home_login_logic as server_logic
from Common.communication import loadJSONFromFile  # Importa la funzione

class MainWindow(QtWidgets.QMainWindow):

    show_client_home = pyqtSignal()
    show_pub_home = pyqtSignal()
    user = []
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.clienteButton.clicked.connect(self.open_cliente_window)
        self.ui.serverButton.clicked.connect(self.open_server_window)

        # Load server configurations
        self.server_config = self.load_server_config()

    def load_server_config(self):
        try:
            # Usa la funzione importata per caricare il file JSON
            config_path = '/Users/rita/Desktop/ParthenoPub/ParthenoPub/server_address.json'
            config = loadJSONFromFile(config_path)
            return config
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load server configuration: {e}")
            return None

    def open_cliente_window(self):
        print("Cliente button clicked")
        try:
            self.close()
            cliente_logic.main()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open Cliente window: {e}")

    def open_server_window(self):
        try:
            self.close()
            server_logic.main()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open Server window: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()