from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QListWidget, QVBoxLayout, QLabel, QHBoxLayout

class Ui_GestioneClienti:
    def setupUi(self, Dialog):
        Dialog.setObjectName("GestioneClientiDialog")
        Dialog.resize(400, 300)

        # Layout principale verticale
        self.layout = QVBoxLayout(Dialog)

        # Etichetta per il titolo
        self.label = QLabel("Gestione Clienti", Dialog)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Lista dei clienti
        self.lista_clienti = QListWidget(Dialog)
        self.layout.addWidget(self.lista_clienti)

        # Layout per i pulsanti
        self.button_layout = QHBoxLayout()

        # Pulsante per mostrare i clienti
        self.button_mostra = QPushButton("Mostra Clienti", Dialog)
        self.button_layout.addWidget(self.button_mostra)

        # Pulsante per aggiungere un cliente
        self.button_aggiungi = QPushButton("Aggiungi Cliente", Dialog)
        self.button_layout.addWidget(self.button_aggiungi)

        # Pulsante per modificare un cliente
        self.button_modifica = QPushButton("Modifica Cliente", Dialog)
        self.button_layout.addWidget(self.button_modifica)

        self.layout.addLayout(self.button_layout)

        # Imposta il titolo della finestra
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Gestione Clienti")