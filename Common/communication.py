import json
import datetime
import socket
import os
import csv


# Funzione per costruire il protocollo di comunicazione (header + payload)
def build_communication_protocol(header_data, payload_data):
    """
    Costruisce il protocollo di comunicazione con un header e un payload.
    """
    # Converte i dati dell'header in formato stringa
    header = build_header(header_data)
    
    # Converte i dati del payload in formato stringa
    payload = build_payload(payload_data)
    
    # Crea il messaggio completo
    communication_protocol = f"--Header:{header}--EndH--Payload:{payload}--EndP"
    
    return communication_protocol


def build_header(header_data):
    """
    Costruisce l'header del protocollo.
    L'header è una stringa in cui i dati sono separati da un punto e virgola.
    """
    header_list = [f"{key}={value}" for key, value in header_data.items()]
    header = ";".join(header_list)
    
    return header


def build_payload(payload_data):
    """
    Costruisce il payload del protocollo.
    Il payload può essere un oggetto JSON o una stringa.
    """
    # Se il payload è un oggetto, lo converte in formato JSON
    if isinstance(payload_data, dict):
        payload = json.dumps(payload_data)
    else:
        payload = str(payload_data)
    
    return payload


def parse_communication_protocol(communication_string):
    """
    Estrae e restituisce l'header e il payload da un protocollo di comunicazione.
    """
    # Trova la posizione di inizio e fine dell'header
    header_start = communication_string.find("--Header:") + len("--Header:")
    header_end = communication_string.find("--EndH")
    
    # Estrae l'header
    header = communication_string[header_start:header_end].strip()
    
    # Trova la posizione di inizio e fine del payload
    payload_start = communication_string.find("--Payload:") + len("--Payload:")
    payload_end = communication_string.find("--EndP", payload_start)
    
    # Estrae il payload
    payload = communication_string[payload_start:payload_end].strip()
    
    # Parso l'header come dizionario (associative array)
    header_array = parse_header(header)
    
    # Parso il payload come dizionario (se è JSON)
    payload_data = parse_payload(payload)
    
    return {"Header": header_array, "Payload": payload_data}


def parse_header(header):
    """
    Parso l'header e lo converto in un dizionario.
    L'header è una stringa separata da punto e virgola, quindi dividiamo la stringa
    e creiamo un dizionario.
    """
    header_array = {}
    header_segments = header.split(";")
    
    for segment in header_segments:
        key, value = segment.split("=")
        header_array[key.strip()] = value.strip()
    
    return header_array


def parse_payload(payload):
    """
    Parso il payload. Se è un JSON, lo converto in un oggetto Python.
    """
    try:
        payload_data = json.loads(payload)
    except json.JSONDecodeError:
        # Se il payload non è un JSON valido, lo restituisco come stringa
        payload_data = payload
    
    return payload_data


def get_current_date():
    """
    Restituisce la data corrente nel formato "gg-mm-aaaa".
    """
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")


def custom_hash(text: str):
    """
    Funzione di hashing personalizzata per generare un hash per il testo fornito.
    """
    hash_value = 0
    for ch in text:
        hash_value = (hash_value * 281 ^ ord(ch) * 997) & 0xFFFFFFFF
    return hash_value

# Funzione per caricare l'indirizzo e la porta del server dal file JSON
def load_server_address_from_json(json_file="server_address.json"):
    """
    Carica l'indirizzo e la porta del server dal file JSON.
    """
    with open(json_file, 'r') as f:
        server_data = json.load(f)
    return server_data['address'], server_data['port']

# Funzione per avviare la comunicazione con il server
def launchMethod(request_str):
    """
    Crea una connessione al server usando i socket e invia una richiesta.
    """
    # Carica le coordinate del server dal file JSON
    address, port = load_server_address_from_json()
    
    # Crea una connessione al server usando i socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((address, port))
        s.sendall(request_str.encode('utf-8'))
        
        # Ricevi la risposta dal server
        data = s.recv(1024)
    
    return data.decode('utf-8')

# Funzioni per gestire i CSV
def find_row(csv_file, search_criteria):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            if all(row[header.index(column)] == str(value) for column, value in search_criteria.items()):
                return row

    return None  # Return None if the row is not found


def find_rows(csv_file, search_criteria=None):
    matching_rows = []

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            if search_criteria is None:
                matching_rows.append(row)
            else:
                if all(row[header.index(column)] == str(value) for column, value in search_criteria.items()):
                    matching_rows.append(row)

    return matching_rows


def insert_row(csv_file, data_row, custom_id=None):
    if custom_id is not None:
        new_id = custom_id
    else:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is None or not last_row[0].isdigit():
                new_id = 1
            else:
                new_id = int(last_row[0]) + 1

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id] + data_row)

    return new_id


def update_row(csv_file: str, row_id: str, column_name: str, new_value: str):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

    for row in rows:
        if row['ID'] == row_id:
            row[column_name] = new_value
            break
    else:
        print(f"Row with ID {row_id} not found.")
        return

    with open(csv_file, 'w', newline='') as file:
        fieldnames = csv_reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Value in row {row_id}, column {column_name} updated to {new_value}.")