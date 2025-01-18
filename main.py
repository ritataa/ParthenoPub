import sys
from PyQt5.QtWidgets import QApplication
from Logic.schermata_iniziale_logic import MainWindow
from Logic.Pub.pub_home_login_logic import PubHomeLoginLogic
#from Logic.Pub.pub_home_logic import PubHomeLogic
from Logic.Clienti.cliente_home_logic import ClienteHomeLogic

from multiprocessing import Process
from combined_multiplex_concurrent_server import server_main



def main():
    app = QApplication(sys.argv)

    login_window = MainWindow()
    clienti_window = ClienteHomeLogic(login_window.user)
    pub_window = PubHomeLoginLogic(login_window.user)

    login_window.show_clienti_home.connect(lambda:clienti_window.showWindow(login_window.user))
    login_window.show_pub_home.connect(lambda: pub_window.showWindow(login_window.user))

    login_window.show()

    app.exec_()





if __name__ == "__main__":
    onlymain = True
    if onlymain:
        main()
    else:
        server = Process(target=server_main, args=('127.0.0.1', 5000))
        server.start()
        main()
        server.kill()