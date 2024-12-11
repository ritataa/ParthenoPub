import sys
import json
from PyQt5 import QtWidgets
from gui.schermata_iniziale_gui import Ui_MainWindow
import logic.clienti.cliente_home_logic as cliente_logic
import logic.pub.pub_home_login_logic as server_logic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.clienteButton.clicked.connect(self.open_cliente_window)
        self.ui.serverButton.clicked.connect(self.open_server_window)

        # Load server configurations
        self.server_config = self.load_server_config()

    def load_server_config(self):
        try:
            with open('common/server_adress.json', 'r') as file:
                config = json.load(file)
            return config
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load server configuration: {e}")
            return None

    def open_cliente_window(self):
        try:
            self.close()
            cliente_logic.main()  # Assuming cliente_home_logic.py has a main function to start the window
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open Cliente window: {e}")

    def open_server_window(self):
        try:
            self.close()
            server_logic.main()  # Assuming pub_home_login_logic.py has a main function to start the window
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to open Server window: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()