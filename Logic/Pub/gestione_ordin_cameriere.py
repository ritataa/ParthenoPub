import json
import os
import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QDialog


from SelMultiplexClient import launchMethod
from Common.communication import request_constructor_str, loadJSONFromFile
from gui.Pub.gestione_ordin_cameriere_gui import Ui_Form

class SegreteriaDialogAggiungiappelloLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        mgen = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuGen"), server_coords['address'], server_coords['port']))
        mgen = mgen['result']
        for m in mgen:
            newstr = f"[{m[1]}] {m[0]} - {m[2]} EURO"
            self.ui.comboBox_nomeMenuGen.addItem(newstr)

        mbirre = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuBirre"), server_coords['address'], server_coords['port']))
        mbirre = mbirre['result']
        for m in mbirre:
            newstr = f"[{m[1]}] {m[0]} - {m[2]} EURO"
            self.ui.comboBox_nomeBirre.addItem(newstr)
            
        mdolci = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuDolci"), server_coords['address'], server_coords['port']))
        mdolci = mdolci['result']
        for m in mdolci:
            newstr = f"[{m[1]}] {m[0]} - {m[2]} EURO"
            self.ui.comboBox_nomeDolci.addItem(newstr)

        self.ui.pushButton_invia.clicked.connect(self.inviaOrdine)
        self.ui.pushButton_aggRichiesta.clicked.connect(self.aggiornaRichiesta)

    def inviaOrdine(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        selected1 = self.ui.comboBox_nomeMenuGen.currentText()
        pattern = r'\[(.*?)\]'
        selected = re.search(pattern, selected)
        ordineG = selected.group(1)
    
        selected2 = self.ui.comboBox_nomeBirre.currentText()
        pattern = r'\[(.*?)\]'
        selected = re.search(pattern, selected)
        ordineG = selected.group(1)
    
        payload = {
            "ordineG": ordineG,
            
        }

        res = launchMethod(request_constructor_str(payload, 'inserisciAppello'), server_coords['address'], server_coords['port'])
        res = json.loads(res)
        if res["result"] == 'OK':
            QMessageBox.information(None, "Success", "Appello inserito con successo")
        print(res)


def run():
    dialog = Ui_segreteria_dialog_inserisci_appello()
    dialog.exec_()


if __name__ == "__main__":
    run()