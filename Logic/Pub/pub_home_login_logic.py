import sys
import csv
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import os
from SelMultiplexClient import launchMethod
from Common.communication import customHash, request_constructor_str, loadJSONFromFile



from Logic.Pub.pub_home_logic import PubHomeLogic
from gui.Pub.pub_home_login_gui import Ui_MainWindow  # Import the generated UI class



class PubHomeLoginLogic(QtWidgets.QMainWindow):

    show_pub_home = pyqtSignal()
    user = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Connect the login button to the login function
        self.ui.LoginButton.clicked.connect(self.checkLogin)

    def checkLogin(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        password = str(customHash(self.ui.PasswordField.text()))
        username = self.ui.UserField.text()
        combobox = self.ui.ComboBoxSelect.currentText()
        result = None
        
        if combobox == "Students":
            toSend = {"Matricola": username, "Password": password}
            result = launchMethod(request_constructor_str(toSend, "StudentsLogin"), server_coords['address'], server_coords['port'])

        elif combobox == "Office":
            toSend = {"Email": username, "Password": password}
            result = launchMethod(request_constructor_str(toSend, "OfficeLogin"), server_coords['address'], server_coords['port'])

        result = result.replace("\n", "")
        result = result.replace("\r", "")
        if result == "false":
            QMessageBox.critical(None, "Login - Error",
                                "Email, Password or User type incorrect.\nCheck your info and retry.")
        else:
            try:
                if combobox == "Students":
                    self.openStudentHomeWindow(result)
                if combobox == "Office":
                    self.openSegreteriaHomeWindow(result)
            except Exception as e:
                print(e)
    def show_error_message(self, message):
        QMessageBox.critical(self, "Login Error", message)

    def open_pub_home(self, user_id, username):
        self.hide()  # Hide the login window
        user_info = {
            "id": user_id,
            "name": username  # Only include the username and user_id
        }
        self.pub_home = PubHomeLogic(user_info)
        self.pub_home.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = PubHomeLoginLogic()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

