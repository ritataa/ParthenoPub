import json
import os
import datetime
from Common.communication import find_row, find_rows, insert_row, update_row, find_rows_v2, filter_dates_after_current


# Percorso principale
ROOT_DIR = os.path.abspath(os.curdir)

# Percorsi ai file CSV
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

def default_case():
    return "Method not implemented"

def GetTavolo(payload):
    """
    Restituisce i dettagli di un tavolo dato il suo numero.
    """
    result_row = find_row(DB["TAVOLI"], {"TavoloID": payload["TavoloID"]})
    if result_row:
        return {"result": result_row}
    else:
        return {"result": "false"}
    
def GetUser(payload):
    """
    Verifica le credenziali dell'utente nel file login.csv.
    """
    result_row = find_row(DB["LOGIN"], {"User": payload["User"]})
    if result_row:
        if "Password" in payload:
            if str(result_row[4]) == str(payload["Password"]):
                return result_row
            else:
                return False
        else:
            return False
    else:
        return False

def ClientsPrenotazioniTav(payload):
    """
    Verifica se un cliente ha prenotato un tavolo.
    """
    result_rows = find_rows(DB["PRENOTA_TAVOLO"], {"ClienteID": payload["ClienteID"]})
    if result_rows:
        return {"result": result_rows}
    else:
        return {"result": "false"}

def InsertCliente(payload):
    """
    Inserisce un nuovo cliente nel file delle richieste di entrata.
    """
    result_row = find_row(DB["RICHIESTA_ENTRATA"], {"ID": payload["ID"]})
    if not result_row:
        insert_row(DB["RICHIESTA_ENTRATA"], [
            payload["Nome"],
            payload["Tavolo"],
            payload["Orario"]
        ])
        return {"result": "True"}
    else:
        return {"result": "Cliente già esistente"}

def ClientsRichiesteCameriere():
    """
    Mostra i tavoli che hanno richiesto il cameriere.
    """
    result_rows = find_rows(DB["RICHIESTA_CAMERIERE"])
    if result_rows:
        return {"result": result_rows}
    else:
        return {"result": "false"}

def ClientsRichiesteMenu(payload):
    """
    Mostra i tavoli che hanno richiesto un tipo di menu specifico.
    """
    result_rows = find_rows(DB["RICHIESTA_MENU"], {"TipoMenu": payload["TipoMenu"]})
    if result_rows:
        return {"result": result_rows}
    else:
        return {"result": "false"}




def GetMenu(payload):
    """
    Handles the request to call a waiter when the menu button is pressed.
    """
    numero_tavolo = payload["numero_tavolo"]

    # Check if the table exists and is available
    tavolo_row = find_row(DB["TAVOLI"], {"NumeroTavolo": numero_tavolo})
    if tavolo_row:
        # Log the request for a waiter
        timestamp = datetime.datetime.now().isoformat()
        insert_row(DB["RICHIESTA_CAMERIERE"], [numero_tavolo, "Richiesta cameriere", timestamp])

        return {"result": "successo", "messaggio": "Cameriere chiamato"}
    else:
        return {"result": "errore", "messaggio": "Tavolo non trovato"}


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

def InsertMenuGen():
    
    mgen = find_rows(DB["MGEN"])
    if len(mgen) > 0:
        return {"result": mgen}
    else:
        return {"result": "not found"}
    
def InsertMenuBirre():
    
    mbirre = find_rows(DB["MBIRRE"])
    if len(mbirre) > 0:
        return {"result": mbirre}
    else:
        return {"result": "not found"}
    
def InsertMenuDolci():
    
    mdolci = find_rows(DB["MDOLCI"])
    if len(mdolci) > 0:
        return {"result": mdolci}
    else:
        return {"result": "not found"}


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
    
def inviaOrdine(payload):
    try:
        insert_row(csv_file=DB["INVIA_ORDINE"],
                data_row=[payload["TavoloID"], payload["ordineG"], payload["quantG"], payload["ordineB"], payload["quantB"], payload["ordineD"], payload["quantD"]])
        return {"result": "OK"}
    except Exception as e:
        return {"result": f"Not OK error: {e}"}

# in gestione_ordinazioni
def ClientsRichiesteInvioOrdine():
    """
    Recupera l'elenco degli ordini da inviare o completare per ogni tabella.
    """
    # Find all rows in the INVIA_ORDINE table where the Status is "Richiesta" or "Completato"
    result_rows = find_rows(DB["INVIA_ORDINE"], {"Stato": ["1","0","?"]})
    
    if result_rows:
        # Return the orders found in the database
        return {"result": result_rows}
    else:
        # Return "false" if no orders are found
        return {"result": "false"}

def AggiornaStatoOrdine(payload):
    jsonToSend = {}
    
    if payload["Stato"] == "1":
        invio_ord = find_row(DB["INVIA_ORDINE"], {"ID": payload["ID"]})
        tavolo_id = invio_ord[1]
        
        # Recupera i dettagli del tavolo
        tavolo = find_row(DB["TAVOLI"], {"TavoloID": tavolo_id})
        numero_persone = tavolo[2]
        
        # Calcola il pagamento totale
        pagamento_totale = 0
        if invio_ord[2]:  # ordineG
            menu_gen = find_row(DB["MGEN"], {"ID": invio_ord[2]})
            pagamento_totale += float(menu_gen[2]) * int(invio_ord[3])
        if invio_ord[4]:  # ordineB
            menu_birre = find_row(DB["MBIRRE"], {"ID": invio_ord[4]})
            pagamento_totale += float(menu_birre[2]) * int(invio_ord[5])
        if invio_ord[6]:  # ordineD
            menu_dolci = find_row(DB["MDOLCI"], {"ID": invio_ord[6]})
            pagamento_totale += float(menu_dolci[2]) * int(invio_ord[7])
        
        # Inserisci una nuova riga nel file dei pagamenti
        insert_row(DB["PAGAMENTI"], [payload["ID"], tavolo_id, numero_persone, pagamento_totale, "0"])
        
        jsonToSend = {"pagamenti": [payload["ID"], tavolo_id, numero_persone, pagamento_totale, "0"]}

    jsonToSend = str(jsonToSend)
    update_row(csv_file=DB["INVIA_ORDINE"], row_id=payload["ID"], column_name="Stato",
            new_value=payload["Stato"])


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


        # Ordini
        case "InsertMenuGen":
            return InsertMenuGen(payload)
        case "InsertMenuBirre":
            return InsertMenuBirre(payload)
        case "InsertMenuDolci":
            return InsertMenuDolci(payload)
        case "inviaOrdine":
            return inviaOrdine(payload)
        case "GetOrdiniByTavolo":
            return GetOrdiniByTavolo(payload)
        case "DeleteOrdiniByTavolo":
            return DeleteOrdiniByTavolo(payload)
        

        case "AggiornaStatoOrdine":
            return AggiornaStatoOrdine(payload)

        case "GetUser":
            return GetUser(payload)
        case "ClientsPrenotazioniTav":
            return ClientsPrenotazioniTav(payload)
        case "InsertCliente":
            return InsertCliente(payload)
        case "ClientsRichiesteCameriere":
            return ClientsRichiesteCameriere()
        case "ClientsRichiesteMenu":
            return ClientsRichiesteMenu(payload)
        case "ClientsRichiesteInvioOrdine":
            return ClientsRichiesteInvioOrdine()

        # Caso predefinito per metodi non implementati
        case _:
            return default_case()