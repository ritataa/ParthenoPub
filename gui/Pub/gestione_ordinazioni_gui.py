from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QListWidget, QVBoxLayout

class Ui_GestioneOrdinazioni:
    def setupUi(self, Dialog):
        Dialog.setObjectName("GestioneOrdinazioniDialog")
        Dialog.resize(400, 300)

        self.lista_ordini = QListWidget(Dialog)
        self.processaOrdineButton = QPushButton(Dialog)
        self.processaOrdineButton.setText("Processa Ordine")

        layout = QVBoxLayout(Dialog)
        layout.addWidget(self.lista_ordini)
        layout.addWidget(self.processaOrdineButton)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Gestione Ordinazioni")