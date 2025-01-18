import sys
import csv
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from Common.communication import formato_data
import os
from SelMultiplexClient import launchMethod
from Common.communication import customHash, request_constructor_str, loadJSONFromFile



from Logic.Pub.pub_home_logic import PubHomeLogic
from gui.Pub.pub_home_login_gui import Ui_MainWindow  # Import the generated UI class



class PubHomeLoginLogic(QMainWindow):

    show_pub_home = pyqtSignal()
    user = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Connect the login button to the login function
        self.ui.LoginButton.clicked.connect(self.checkLogin)

    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.MtrLabel.setText(user[0])
        self.ui.NameLastnameLabel.setText(f"{user[1]}, {user[2]}")
        self.ui.DateLabel.setText(f"{formato_data()}")

    def checkLogin(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        password = str(customHash(self.ui.PasswordField.text()))
        username = self.ui.UserField.text()
        
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

def run():
    app = QApplication(sys.argv)
    window = PubHomeLoginLogic()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
