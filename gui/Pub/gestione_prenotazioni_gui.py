from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout

class Ui_GestionePrenotazioni:
    def setupUi(self, Dialog):
        Dialog.setObjectName("GestionePrenotazioniDialog")
        Dialog.resize(400, 300)
        
        # Layout principale verticale
        self.layout = QVBoxLayout(Dialog)

        # Etichetta per il titolo
        self.label = QLabel("Prenotazioni:", Dialog)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Lista delle prenotazioni
        self.lista_prenotazioni = QListWidget(Dialog)
        self.layout.addWidget(self.lista_prenotazioni)

        # Layout per i pulsanti
        self.button_layout = QHBoxLayout()

        # Pulsante per aggiornare le prenotazioni
        self.aggiornaPrenotazioniButton = QPushButton("Aggiorna Prenotazioni", Dialog)
        self.button_layout.addWidget(self.aggiornaPrenotazioniButton)

        # Pulsante per cancellare una prenotazione
        self.cancellaPrenotazioneButton = QPushButton("Cancella Prenotazione", Dialog)
        self.button_layout.addWidget(self.cancellaPrenotazioneButton)

        # Pulsante per confermare una prenotazione
        self.confermaPrenotazioneButton = QPushButton("Conferma Prenotazione", Dialog)
        self.button_layout.addWidget(self.confermaPrenotazioneButton)

        self.layout.addLayout(self.button_layout)

        # Imposta il titolo della finestra
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Gestione Prenotazioni")