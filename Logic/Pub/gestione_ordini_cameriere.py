import json
import os
import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QDialog


from SelMultiplexClient import launchMethod
from Common.communication import request_constructor_str, loadJSONFromFile
from gui.Pub.gestione_ordini_cameriere_gui import Ui_Form

class GestioneOrdiniCameriere(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        # Initialize an empty list to store orders
        self.orders = []

        mgen = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuGen"), server_coords['address'], server_coords['port']))
        mgen = mgen['result']
        for m in mgen:
            newstr1 = f"[{m[0]}] {m[1]} - {m[2]} EURO"
            self.ui.comboBox_nomeMenuGen.addItem(newstr1)

        mbirre = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuBirre"), server_coords['address'], server_coords['port']))
        mbirre = mbirre['result']
        for m in mbirre:
            newstr2 = f"[{m[0]}] {m[1]} - {m[2]} EURO"
            self.ui.comboBox_nomeBirre.addItem(newstr2)
            
        mdolci = json.loads(
            launchMethod(request_constructor_str(None, "InsertMenuDolci"), server_coords['address'], server_coords['port']))
        mdolci = mdolci['result']
        for m in mdolci:
            newstr3 = f"[{m[0]}] {m[1]} - {m[2]} EURO"
            self.ui.comboBox_nomeDolci.addItem(newstr3)

        tav = json.loads(
            launchMethod(request_constructor_str(None, "GetTavolo"), server_coords['address'], server_coords['port']))
        tav = tav['result']
        for t in tav:
            newstr4 = f"{t[0]}"
            self.ui.comboBox_tavolo.addItem(newstr4)
        
        # Quantità per i menu (Generale, Birre, Dolci)
        quantities = [str(i) for i in range(1, 11)]  # Da 1 a 10

        # Popolazione ComboBox delle quantità
        for qty in quantities:
            self.ui.comboBox_quantita.addItem(qty)  # Per il menu generale
            self.ui.comboBox_quantita_2.addItem(qty)   # Per il menu birre
            self.ui.comboBox_quantita_3.addItem(qty)   # Per il menu dolci
        
        self.ui.pushButton_invia.clicked.connect(self.inviaOrdine)
    
    def inviaOrdine(self):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))

        #tavolo
        tavolo = self.ui.comboBox_tavolo.currentText()
        

        #Menu Gen
        selected2 = self.ui.comboBox_nomeMenuGen.currentText()
        pattern = r'\[(.*?)\]'  #regex cerca un testo tra parentesi quadre []
        selected2 = re.search(pattern, selected2)
        ordineG = selected2.group(1)

        #quantita gen
        quantG = self.ui.comboBox_quantita.currentText()

        #Menu Birre
        selected3 = self.ui.comboBox_nomeBirre.currentText()
        pattern = r'\[(.*?)\]'
        selected3 = re.search(pattern, selected3)
        ordineB = selected3.group(1)

        #quantita birre
        quantB = self.ui.comboBox_quantita_2.currentText()

        #Menu Dolci
        selected4 = self.ui.comboBox_nomeDolci.currentText()
        pattern = r'\[(.*?)\]'
        selected4 = re.search(pattern, selected4)
        ordineD = selected4.group(1)

        #quantita dolci
        quantD = self.ui.comboBox_quantita_3.currentText()
    
        payload = {
            "tavolo": tavolo,
            "ordineG": ordineG,
            "quantitaG": quantG,
            "ordineB": ordineB,
            "quantitaB": quantB,
            "ordineD": ordineD,
            "quantitaD": quantD
            
        }
            # Add the new order to the list of orders
        self.orders.append(payload)
    
        for payload in self.orders:
            res = launchMethod(request_constructor_str(payload, 'inviaOrdine'), server_coords['address'], server_coords['port'])
            res = json.loads(res)
            if res["result"] == 'OK':
                QMessageBox.information(None, "Success", "Ordine inviato con successo")
        print(res)

        # Clear the orders list after sending
        self.orders.clear()

def run():
    dialog = Ui_Form()
    dialog.exec_()


if __name__ == "__main__":
    run()