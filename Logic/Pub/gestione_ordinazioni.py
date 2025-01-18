import json
import os
from PyQt5.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout
from Common.communication import loadJSONFromFile, request_constructor_str
from SelMultiplexClient import launchMethod
from gui.Pub.gestione_ordinazioni_gui import Ui_GestioneOrdinazioni

class GestioneOrdinazioniLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestioneOrdinazioni()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.AggiornaButton.clicked.connect(self.Aggiorna)

        self.data = None
        self.Aggiorna()
    

    def Aggiorna(self):

        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
    
        rows = launchMethod(request_constructor_str({}, "ClientsRichiesteInvioOrdine"), server_coords['address'], server_coords['port'])
        rows = json.loads(rows)

        if rows["result"] == "false":
            QMessageBox.information(self, "Attenzione", "Nessuna ordinazione disponibile")
            self.data = None
        else:
            if self.data == None:
                for r in rows["result"]:
                    self.createRow(r)
                self.data = rows
            elif self.data != rows:
                self.data = rows
                self.clearTableView()
                for r in rows["result"]:
                    self.createRow(r)

    def createRow(self, data):
        layout = QHBoxLayout()

        print(data)

        del data[3]
        for d in data[1:]:
            layout.addWidget(QLabel(d))

        button_layout = QVBoxLayout()

        newButton_approve = QPushButton("Consegnato")
        newButton_approve.clicked.connect(lambda: self.SegnaConsegnato(data[0]))
        button_layout.addWidget(newButton_approve)

        
        layout.addLayout(button_layout)

        # Set the layout of the widget
        self.ui.TableView.addLayout(layout)

    def SegnaConsegnato(self, ID:str):
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        row = launchMethod(request_constructor_str({"ID":ID, "Stato":"1"}, "AggiornaStatoOrdine"), server_coords['address'], server_coords['port'])
        row = json.loads(row)

        if row.get("result") == "success":
            QMessageBox.information(None, "Consegnato - Successo", "Ordine consegnato con successo")
            self.transferToPagamenti(ID)
        else:
            QMessageBox.warning(None, "Errore", "Errore nell'aggiornamento dello stato dell'ordine")

        self.clearTableView()
        self.Aggiorna()

    def transferToPagamenti(self, ID: str):
    
        ROOT_DIR = os.path.abspath(os.curdir)
        server_coords = loadJSONFromFile(os.path.join(ROOT_DIR, "server_address.json"))
        row = launchMethod(request_constructor_str({"ID":ID, "Stato":"1"}, "AggiornaStatoOrdine"), server_coords['address'], server_coords['port'])
        row = json.loads(row)
        
        if row.get("result") == "OK":
            QMessageBox.information(None, "Trasferimento - Successo", "Dettagli dell'ordine trasferiti con successo nel file dei pagamenti")
        else:
            QMessageBox.warning(None, "Errore", "Errore nel trasferimento dei dettagli dell'ordine nel file dei pagamenti")


    def clearTableView(self):
        while self.ui.TableView.count():
            item = self.ui.TableView.takeAt(0)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    layout = item.layout()
                    if layout:
                        self.clearLayout(layout)


    def clearTableView(self):
        # Remove all layouts from TableView
        while self.ui.TableView.count():
            item = self.ui.TableView.takeAt(0)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    layout = item.layout()
                    if layout:
                        # Recursively clear layout's items
                        self.clearLayout(layout)

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())