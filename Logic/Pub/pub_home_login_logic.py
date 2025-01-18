import json
import os
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from SelMultiplexClient import launchMethod
from Common.communication import customHash, request_constructor_str, loadJSONFromFile


from gui.Pub.pub_home_login_gui import Ui_MainWindow  # Import the generated UI class
from Logic.Pub.pub_home_logic import PubHomeLogic  # Import the PubHomeLogic class



class PubHomeLoginLogic(QMainWindow):

    show_pub_home = pyqtSignal()
    user = []

    def __init__(self, user=None):
        super().__init__()
        self.user = user
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the login button to the login function
        self.ui.pushButton.clicked.connect(self.checkLogin)

    def showWindow(self, user):
        self.show()
        self.user = user
        

    def checkLogin(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        password = str(customHash(self.ui.lineEdit_2.text()))
        username = self.ui.lineEdit.text()
        result = None

        # Construct the payload for the server
        toSend = {"User": username, "Password": password}

        # Send the request to the server using the "GetUser" method
        result = launchMethod(request_constructor_str(toSend, "GetUser"), server_coords['address'], server_coords['port'])

        # Clean up the result string
        result = result.replace("\n", "").replace("\r", "")

        # Check the result and display appropriate messages
        if result == "false":
                QMessageBox.critical(self, "Login - Error", "Username or Password incorrect. Please try again.")
        else:
            try:
                self.open_pub_home_window(result)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")


    
    def open_pub_home_window(self, user):
        self.user = json.loads(user)
        self.show_pub_home.emit()
        self.close()
        pub_home_window = PubHomeLogic(self.user)
        pub_home_window.show()

def run():
    app = QApplication(sys.argv)
    window = PubHomeLoginLogic()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    input_data = {"header": "GetUser", "payload": {"User": "parthenopub", "Password": "1234"}}
    result = launchMethod(json.dumps(input_data), "127.0.0.1", 1024)
    print(result)

#if __name__ == "__main__":
#   run('["1", "parthenopub","1234"]')