import json
import os

from common.communication import find_row, find_rows, insert_row, update_row, find_rows_v2, filter_dates_after_current

ROOT_DIR = os.path.abspath(os.curdir)

DB = {
    "CLIENTI": os.path.join(ROOT_DIR, 'db', 'clienti.csv'),
    "ORDINI": os.path.join(ROOT_DIR, 'db', 'ordini.csv'),
    "PIATTI": os.path.join(ROOT_DIR, 'db', 'piatti.csv'),
    "MENU": os.path.join(ROOT_DIR, 'db', 'menu.csv'),
    "STAF": os.path.join(ROOT_DIR, 'db', 'staff.csv'),
}

def default_case():
    return "Method not implemented"


def GetCliente(payload):
    """
    Restituisce i dettagli di un cliente dato il suo ID.
    """
    result_row = find_row(DB["CLIENTI"], {"ID": payload["ID"]})
    if result_row:
        return {"result": result_row}
    else:
        return {"result": "false"}


def GetPanino(payload):
    """
    Restituisce i dettagli di un panino dato il suo ID.
    """
    result_row = find_row(DB["PANINI"], {"ID": payload["ID"]})
    if result_row:
        return {"result": result_row}
    else:
        return {"result": "false"}


def InsertOrdine(payload):
    """
    Inserisce un nuovo ordine per un tavolo specifico.
    L'ordine include i dettagli del cliente, i panini ordinati e il totale.
    """
    order_id = payload["ID"]
    result_row = find_row(DB["ORDINI"], {"ID": order_id})
    if result_row:
        return {"result": "Ordine già esistente"}
    else:
        insert_row(DB["ORDINI"], [
            payload["ID"],  # ID ordine
            payload["Tavolo"],  # Numero del tavolo
            payload["ClienteID"],  # ID del cliente
            payload["Panini"],  # Panini ordinati
            payload["Totale"]  # Totale ordine
        ])
        return {"result": "Ordine inserito con successo"}


def GetOrdiniByTavolo(payload):
    """
    Restituisce tutti gli ordini associati a un tavolo specifico.
    """
    result_rows = find_rows(DB["ORDINI"], {"Tavolo": payload["Tavolo"]})
    if result_rows:
        return {"result": result_rows}
    else:
        return {"result": "false"}


def DeleteOrdiniByTavolo(payload):
    """
    Elimina tutti gli ordini associati a un tavolo specifico.
    """
    result_rows = find_rows(DB["ORDINI"], {"Tavolo": payload["Tavolo"]})
    if result_rows:
        for row in result_rows:
            update_row(DB["ORDINI"], row, delete=True)  # Rimuove le righe corrispondenti
        return {"result": "Ordini eliminati con successo"}
    else:
        return {"result": "false"}




def method_switch(method, payload):
    match method:

        # Cliente
        case "GetCliente":
            return GetCliente(payload)

        # Panino
        case "GetPanino":
            return GetPanino(payload)

        # Ordini
        case "InsertOrdine":
            return InsertOrdine(payload)
        case "GetOrdiniByTavolo":
            return GetOrdiniByTavolo(payload)
        case "DeleteOrdiniByTavolo":
            return DeleteOrdiniByTavolo(payload)

        # Caso predefinito per metodi non implementati
        case _:
            return default_case()