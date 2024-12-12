import sys

from PyQt5.QtWidgets import QApplication

from Logic.schermata_iniziale_logic import MainWindow

from multiprocessing import Process
from combined_multiplex_concurrent_server import server_main


def main():
    app = QApplication(sys.argv)

    initial_window = MainWindow()

    # Connect buttons to their respective functions
    


    initial_window.show()
    app.exec_()

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