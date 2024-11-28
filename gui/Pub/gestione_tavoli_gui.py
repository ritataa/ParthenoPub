from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QListWidget, QVBoxLayout

class Ui_GestioneTavoli:
    def setupUi(self, Dialog):
        Dialog.setObjectName("GestioneTavoliDialog")
        Dialog.resize(400, 300)

        # Lista dei tavoli
        self.lista_tavoli = QListWidget(Dialog)

        # Pulsante per aggiornare lo stato del tavolo
        self.aggiornaStatoButton = QPushButton(Dialog)
        self.aggiornaStatoButton.setText("Aggiorna Stato Tavolo")

        # Layout
        layout = QVBoxLayout(Dialog)
        layout.addWidget(self.lista_tavoli)
        layout.addWidget(self.aggiornaStatoButton)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Gestione Tavoli")