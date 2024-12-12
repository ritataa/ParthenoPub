import csv
import json
import os

from Common.communication import find_rows_v2

ROOT_DIR = os.path.abspath(os.curdir)

DB = {
    "TAVOLI": os.path.join(ROOT_DIR, 'db', 'tavoli', 'tavoli.csv'),

    "RICHIESTA_CAMERIERE": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesta_cameriere.csv'),
    "INVIA_ORDINE": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'invia_ordine.csv'),
    "PRENOTA_TAVOLO": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'prenota_tavolo.csv'),
    "RICHIESTA_ENTRATA": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesta_entrata.csv'),
    "RICHIESTA_MENU": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesta_menu.csv'),

    "PAGAMENTI": os.path.join(ROOT_DIR, 'db', 'pagamenti', 'pagamenti.csv'),

    "MENU": os.path.join(ROOT_DIR, 'db', 'menu', 'menu.csv'),

    "LOGIN": os.path.join(ROOT_DIR, 'db', 'login', 'login.csv'),
}

if __name__ == '__main__':
    result_row = find_rows_v2(DB["RICHIESTA_ENTRATA"],[{"id": "1"}, {"Stato": "1"}])
    print(result_row)