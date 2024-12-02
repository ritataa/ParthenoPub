import json
import os

from common.communication import find_row, find_rows, insert_row, update_row, find_rows_v2, filter_dates_after_current


# Percorso principale
ROOT_DIR = os.path.abspath(os.curdir)

# Percorsi ai file CSV
DB = {
    "TAVOLI": os.path.join(ROOT_DIR, 'db', 'tavoli', 'tavoli.csv'),

    "RICHIESTA_CAMERIERE": os.path.join(os.path.abspath(os.curdir), 'db', 'prenotazioni', 'richiesta_cameriere.csv'),
    "INVIA_ORDINE": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'invia_ordine.csv'),
    "PRENOTA_TAVOLO": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'prenota_tavolo.csv'),
    "RICHIESTA_ENTRATA": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesta_entrata.csv'),
    "RICHIESTA_MENU": os.path.join(ROOT_DIR, 'db', 'prenotazioni', 'richiesta_menu.csv'),

    "PAGAMENTI": os.path.join(ROOT_DIR, 'db', 'pagamenti', 'pagamenti.csv'),

    "MENU": os.path.join(ROOT_DIR, 'db', 'menu', 'menu.csv'),
}

def default_case():
    return "Method not implemented"

# Funzione per ottenere il menu in base al tipo richiesto
def GetMenu(menu_type):
    menu_file = DB["MENU"]  # Percorso del file CSV del menu
    menu_rows = find_rows(menu_file)  # Ottieni tutte le righe del menu
    
    if menu_rows:
        # Restituisci il menu in un formato che il client possa comprendere
        menu = []
        for row in menu_rows:
            # Supponiamo che ogni riga contenga: ID, Nome, Tipo, TipoMenu, Prezzo, Descrizione
            if row[3].lower() == menu_type.lower():
                menu.append({
                "ID": row[0],
                "Nome": row[1],
                "Tipo": row[2],
                "TipoMenu": row[3],
                "Prezzo": row[4],
                "Descrizione": row[5]
            })
        if menu:
            return {"result": menu}
        else:
            return {"result": "No items found for the requested menu type."}
    else:
        return {"result": "false"}

import datetime
def richiestaCameriere(payload):
    """
    Handles the request to call a waiter for a specific table.
    """
    numero_tavolo = payload["numero_tavolo"]

    # Check if the table exists and is available
    tavolo_row = find_row(DB["TAVOLI"], {"NumeroTavolo": numero_tavolo})
    if tavolo_row:
        # Log the request in a CSV file or update the table status
        timestamp = datetime.datetime.now().isoformat()
        insert_row(DB["RICHIESTA_CAMERIERE"], [numero_tavolo, "Richiesta cameriere", timestamp])
        
        # Optionally update the table status if needed
        # update_row(DB["TAVOLI"], tavolo_row[0], "Stato", "Cameriere chiamato")

        return {"stato": "successo"}
    else:
        return {"stato": "errore", "messaggio": "Tavolo non trovato"}

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

        # Menu
        case "GetMenu":
            return GetMenu(payload)

        # Cameriere
        case "richiestaCameriere":
            return richiestaCameriere(payload)


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