# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestione_ordini_cameriere.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 614)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 90, 651, 386))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_quantita_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_quantita_3.setFont(font)
        self.label_quantita_3.setObjectName("label_quantita_3")
        self.gridLayout.addWidget(self.label_quantita_3, 9, 2, 1, 1)
        self.comboBox_nomeMenuGen = QtWidgets.QComboBox(self.widget)
        self.comboBox_nomeMenuGen.setObjectName("comboBox_nomeMenuGen")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.comboBox_nomeMenuGen.addItem("")
        self.gridLayout.addWidget(self.comboBox_nomeMenuGen, 4, 1, 1, 1)
        self.comboBox_quantita_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_quantita_3.setObjectName("comboBox_quantita_3")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.comboBox_quantita_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_quantita_3, 9, 3, 1, 1)
        self.label_quantita_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_quantita_2.setFont(font)
        self.label_quantita_2.setObjectName("label_quantita_2")
        self.gridLayout.addWidget(self.label_quantita_2, 7, 2, 1, 1)
        self.label_menuDolci = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_menuDolci.setFont(font)
        self.label_menuDolci.setObjectName("label_menuDolci")
        self.gridLayout.addWidget(self.label_menuDolci, 9, 0, 1, 1)
        self.comboBox_tavolo = QtWidgets.QComboBox(self.widget)
        self.comboBox_tavolo.setObjectName("comboBox_tavolo")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.comboBox_tavolo.addItem("")
        self.gridLayout.addWidget(self.comboBox_tavolo, 2, 1, 1, 1)
        self.label_quantita = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_quantita.setFont(font)
        self.label_quantita.setObjectName("label_quantita")
        self.gridLayout.addWidget(self.label_quantita, 4, 2, 1, 1)
        self.comboBox_quantita = QtWidgets.QComboBox(self.widget)
        self.comboBox_quantita.setObjectName("comboBox_quantita")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.comboBox_quantita.addItem("")
        self.gridLayout.addWidget(self.comboBox_quantita, 4, 3, 1, 1)
        self.comboBox_nomeDolci = QtWidgets.QComboBox(self.widget)
        self.comboBox_nomeDolci.setObjectName("comboBox_nomeDolci")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.comboBox_nomeDolci.addItem("")
        self.gridLayout.addWidget(self.comboBox_nomeDolci, 9, 1, 1, 1)
        self.label_menuGen = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_menuGen.setFont(font)
        self.label_menuGen.setObjectName("label_menuGen")
        self.gridLayout.addWidget(self.label_menuGen, 4, 0, 1, 1)
        self.label_menuBirre = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_menuBirre.setFont(font)
        self.label_menuBirre.setObjectName("label_menuBirre")
        self.gridLayout.addWidget(self.label_menuBirre, 7, 0, 1, 1)
        self.comboBox_quantita_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_quantita_2.setObjectName("comboBox_quantita_2")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.comboBox_quantita_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_quantita_2, 7, 3, 1, 1)
        self.comboBox_nomeBirre = QtWidgets.QComboBox(self.widget)
        self.comboBox_nomeBirre.setObjectName("comboBox_nomeBirre")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.comboBox_nomeBirre.addItem("")
        self.gridLayout.addWidget(self.comboBox_nomeBirre, 7, 1, 1, 1)
        self.label_tavolo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_tavolo.setFont(font)
        self.label_tavolo.setObjectName("label_tavolo")
        self.gridLayout.addWidget(self.label_tavolo, 2, 0, 1, 1)
        self.pushButton_invia = QtWidgets.QPushButton(Form)
        self.pushButton_invia.setGeometry(QtCore.QRect(500, 540, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_invia.setFont(font)
        self.pushButton_invia.setObjectName("pushButton_invia")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ordinazioni"))
        self.label_quantita_3.setText(_translate("Form", "quantità"))
        self.comboBox_nomeMenuGen.setItemText(0, _translate("Form", "New Item"))
        self.comboBox_nomeMenuGen.setItemText(1, _translate("Form", "[RT] Reti - 12.50 EURO"))
        self.comboBox_nomeMenuGen.setItemText(2, _translate("Form", "[IDS] Ingegneria del software - 8.00 EURO"))
        self.comboBox_nomeMenuGen.setItemText(3, _translate("Form", "[ADC] Architettura dei calcolatori - 10.00 EURO"))
        self.comboBox_nomeMenuGen.setItemText(4, _translate("Form", "[ASD] ASD - 14.00"))
        self.comboBox_nomeMenuGen.setItemText(5, _translate("Form", "[MT1] Mate1 - 7.50"))
        self.comboBox_nomeMenuGen.setItemText(6, _translate("Form", "[BDD] Basi di dati - 9.00"))
        self.comboBox_nomeMenuGen.setItemText(7, _translate("Form", "[SO] Sistemi operativi -11.00"))
        self.comboBox_quantita_3.setItemText(0, _translate("Form", "0"))
        self.comboBox_quantita_3.setItemText(1, _translate("Form", "1"))
        self.comboBox_quantita_3.setItemText(2, _translate("Form", "2"))
        self.comboBox_quantita_3.setItemText(3, _translate("Form", "3"))
        self.comboBox_quantita_3.setItemText(4, _translate("Form", "4"))
        self.comboBox_quantita_3.setItemText(5, _translate("Form", "5"))
        self.comboBox_quantita_3.setItemText(6, _translate("Form", "6"))
        self.comboBox_quantita_3.setItemText(7, _translate("Form", "7"))
        self.comboBox_quantita_3.setItemText(8, _translate("Form", "8"))
        self.comboBox_quantita_3.setItemText(9, _translate("Form", "9"))
        self.comboBox_quantita_3.setItemText(10, _translate("Form", "10"))
        self.label_quantita_2.setText(_translate("Form", "quantità"))
        self.label_menuDolci.setText(_translate("Form", "menu dolci"))
        self.comboBox_tavolo.setItemText(0, _translate("Form", "0"))
        self.comboBox_tavolo.setItemText(1, _translate("Form", "1"))
        self.comboBox_tavolo.setItemText(2, _translate("Form", "2"))
        self.comboBox_tavolo.setItemText(3, _translate("Form", "3"))
        self.comboBox_tavolo.setItemText(4, _translate("Form", "4"))
        self.comboBox_tavolo.setItemText(5, _translate("Form", "5"))
        self.comboBox_tavolo.setItemText(6, _translate("Form", "6"))
        self.comboBox_tavolo.setItemText(7, _translate("Form", "7"))
        self.comboBox_tavolo.setItemText(8, _translate("Form", "8"))
        self.comboBox_tavolo.setItemText(9, _translate("Form", "9"))
        self.comboBox_tavolo.setItemText(10, _translate("Form", "10"))
        self.comboBox_tavolo.setItemText(11, _translate("Form", "11"))
        self.comboBox_tavolo.setItemText(12, _translate("Form", "12"))
        self.comboBox_tavolo.setItemText(13, _translate("Form", "13"))
        self.comboBox_tavolo.setItemText(14, _translate("Form", "14"))
        self.comboBox_tavolo.setItemText(15, _translate("Form", "15"))
        self.comboBox_tavolo.setItemText(16, _translate("Form", "16"))
        self.comboBox_tavolo.setItemText(17, _translate("Form", "17"))
        self.comboBox_tavolo.setItemText(18, _translate("Form", "18"))
        self.comboBox_tavolo.setItemText(19, _translate("Form", "19"))
        self.comboBox_tavolo.setItemText(20, _translate("Form", "20"))
        self.label_quantita.setText(_translate("Form", "quantità"))
        self.comboBox_quantita.setItemText(0, _translate("Form", "0"))
        self.comboBox_quantita.setItemText(1, _translate("Form", "1"))
        self.comboBox_quantita.setItemText(2, _translate("Form", "2"))
        self.comboBox_quantita.setItemText(3, _translate("Form", "3"))
        self.comboBox_quantita.setItemText(4, _translate("Form", "4"))
        self.comboBox_quantita.setItemText(5, _translate("Form", "5"))
        self.comboBox_quantita.setItemText(6, _translate("Form", "6"))
        self.comboBox_quantita.setItemText(7, _translate("Form", "7"))
        self.comboBox_quantita.setItemText(8, _translate("Form", "8"))
        self.comboBox_quantita.setItemText(9, _translate("Form", "9"))
        self.comboBox_quantita.setItemText(10, _translate("Form", "10"))
        self.comboBox_nomeDolci.setItemText(0, _translate("Form", "New Item"))
        self.comboBox_nomeDolci.setItemText(1, _translate("Form", "[TRMS] Tiramisù - 6.00 EURO"))
        self.comboBox_nomeDolci.setItemText(2, _translate("Form", "[CSCK] Cheesecake -5.50 EURO"))
        self.comboBox_nomeDolci.setItemText(3, _translate("Form", "[PRFTRLS] Profiteroles - 5.50 EURO"))
        self.comboBox_nomeDolci.setItemText(4, _translate("Form", "[CDF] Crostata di frutta - 4.50 EURO"))
        self.comboBox_nomeDolci.setItemText(5, _translate("Form", "[SMFRD] Semifreddo - 4.00 EURO"))
        self.comboBox_nomeDolci.setItemText(6, _translate("Form", "[CPRS] Caprese - 5.00 EURO"))
        self.label_menuGen.setText(_translate("Form", "menu generale"))
        self.label_menuBirre.setText(_translate("Form", "menu birre"))
        self.comboBox_quantita_2.setItemText(0, _translate("Form", "0"))
        self.comboBox_quantita_2.setItemText(1, _translate("Form", "1"))
        self.comboBox_quantita_2.setItemText(2, _translate("Form", "2"))
        self.comboBox_quantita_2.setItemText(3, _translate("Form", "3"))
        self.comboBox_quantita_2.setItemText(4, _translate("Form", "4"))
        self.comboBox_quantita_2.setItemText(5, _translate("Form", "5"))
        self.comboBox_quantita_2.setItemText(6, _translate("Form", "6"))
        self.comboBox_quantita_2.setItemText(7, _translate("Form", "7"))
        self.comboBox_quantita_2.setItemText(8, _translate("Form", "8"))
        self.comboBox_quantita_2.setItemText(9, _translate("Form", "9"))
        self.comboBox_quantita_2.setItemText(10, _translate("Form", "10"))
        self.comboBox_nomeBirre.setItemText(0, _translate("Form", "New Item"))
        self.comboBox_nomeBirre.setItemText(1, _translate("Form", "[BC] Birra chiara - 4.50 EURO"))
        self.comboBox_nomeBirre.setItemText(2, _translate("Form", "[BS] Birra scura - 5.00 EURO"))
        self.comboBox_nomeBirre.setItemText(3, _translate("Form", "[BR] Birra rossa - 5.50 EURO"))
        self.comboBox_nomeBirre.setItemText(4, _translate("Form", "[BI] Birra IPA - 6.00 EURO"))
        self.comboBox_nomeBirre.setItemText(5, _translate("Form", "[BW] Birra Weiss - 5.50 EURO"))
        self.comboBox_nomeBirre.setItemText(6, _translate("Form", "[S] Stout - 6.00 EURO"))
        self.label_tavolo.setText(_translate("Form", "tavolo"))
        self.pushButton_invia.setText(_translate("Form", "Invia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
