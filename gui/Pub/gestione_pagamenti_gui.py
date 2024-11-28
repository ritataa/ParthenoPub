from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QListWidget, QVBoxLayout

class Ui_GestionePagamenti:
    def setupUi(self, Dialog):
        Dialog.setObjectName("GestionePagamentiDialog")
        Dialog.resize(400, 300)

        # Lista dei pagamenti
        self.lista_pagamenti = QListWidget(Dialog)

        # Pulsante per confermare il pagamento
        self.confermaPagamentoButton = QPushButton(Dialog)
        self.confermaPagamentoButton.setText("Conferma Pagamento")

        # Layout
        layout = QVBoxLayout(Dialog)
        layout.addWidget(self.lista_pagamenti)
        layout.addWidget(self.confermaPagamentoButton)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Gestione Pagamenti")