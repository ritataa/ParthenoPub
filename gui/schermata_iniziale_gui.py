# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schermata_iniziale.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 140, 501, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.clienteButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        self.clienteButton.setFont(font)
        self.clienteButton.setObjectName("clienteButton")
        self.gridLayout.addWidget(self.clienteButton, 0, 0, 1, 1)
        self.serverButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        self.serverButton.setFont(font)
        self.serverButton.setObjectName("serverButton")
        self.gridLayout.addWidget(self.serverButton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 371, 141))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clienteButton.setText(_translate("MainWindow", "Cliente"))
        self.serverButton.setText(_translate("MainWindow", "Server"))
        self.label.setText(_translate("MainWindow", "Seleziona un\'opzione per continuare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())