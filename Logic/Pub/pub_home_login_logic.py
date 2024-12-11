import sys
import csv
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import os

# Assuming pub_home_logic.py is the main window logicimport sys

from logic.pub.pub_home_logic import PubHomeLogic
from gui.pub.pub_home_login_gui import Ui_MainWindow  # Import the generated UI class

def load_server_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'common', 'server_adress.json')
    with open(config_path, 'r') as file:
        return json.load(file)

class PubHomeLoginLogic(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Connect the login button to the login function
        self.ui.loginButton.clicked.connect(self.handle_login)

        # Load server configuration
        self.server_config = load_server_config()

    def handle_login(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        try:
            with open('login.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['User'] == username and row['Password'] == password:
                        self.open_pub_home(row['ID'], username)
                        return
            self.show_error_message("Invalid username or password.")
        except FileNotFoundError:
            self.show_error_message("The login.csv file was not found.")
        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

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
from logic.pub.pub_home_logic import PubHomeLogic

def load_server_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'common', 'server_adress.json')
    with open(config_path, 'r') as file:
        return json.load(file)

class PubHomeLoginLogic(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pub_home_login.ui', self)  # Load the UI file

        # Connect the login button to the login function
        self.loginButton.clicked.connect(self.handle_login)

        # Load server configuration
        self.server_config = load_server_config()

    def handle_login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        try:
            with open('login.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['User'] == username and row['Password'] == password:
                        self.open_pub_home(row['ID'], username)
                        return
            self.show_error_message("Invalid username or password.")
        except FileNotFoundError:
            self.show_error_message("The login.csv file was not found.")
        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

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