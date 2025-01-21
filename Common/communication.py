import json
import datetime
import socket
import os
import csv
import multiprocessing
import hashlib

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
    
    # Parse header into an associative array
    header_array = {}
    header_segments = header.split(';')

    payload_array = {}
    payload_segments = payload.split(';')
    
    return {"Header": header_array, "Payload": payload}


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

def request_constructor_obj(input_object, header):
    return {
        "header": header,
        "payload": input_object
    }


def request_constructor_str(input_object, header):
    return json.dumps(request_constructor_obj(input_object, header))



def customHash(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funzione per caricare l'indirizzo e la porta del server dal file JSON
def loadJSONFromFile(json_file):
    f = open(json_file)
    data = json.load(f)
    f.close()
    return data

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

def find_rows_v2(csv_file, search_criteria_list=None):
    matching_rows = []

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            # If no search criteria are provided, return all rows
            if search_criteria_list is None:
                matching_rows.append(row)
            else:
                # Check if the row matches any of the criteria in the list
                row_matches = False
                for search_criteria in search_criteria_list:
                    # Check if all criteria in the dictionary match
                    matches = all(row[header.index(column)] == str(value) for column, value in search_criteria.items())
                    if matches:
                        row_matches = True
                        break
                if row_matches:
                    matching_rows.append(row)

    return matching_rows

def formato_data():
    # Definisci i nomi dei giorni della settimana e dei mesi
    nomi_giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre",
                "Ottobre", "Novembre", "Dicembre"]

    # Ottieni la data e l'ora attuali
    oggi = datetime.datetime.now()

    # Ottieni il giorno della settimana, il giorno del mese e il mese attuali
    giorno_settimana = nomi_giorni[oggi.weekday()]
    giorno_mese = oggi.day
    mese = nomi_mesi[oggi.month - 1]
    anno = oggi.year

    # Costruisci la stringa con il formato richiesto
    data_formattata = f"{giorno_settimana} {giorno_mese} {mese} {anno}"
    return data_formattata

def insert_row(csv_file, data_row, custom_id=None):

    if custom_id is not None:
        new_id = custom_id
    else:
        # Determine the last ID in the CSV file and increment it
        # Critical Section Start
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is None or is_number(last_row[0]) == False:
                new_id = 1
            else:
                new_id = int(last_row[0]) + 1
    Lock = multiprocessing.Lock()
    # Insert the new row into the CSV file
    Lock.acquire() #Critical section for write in files
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id] + data_row)
    Lock.release()  # Critical Section END

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

    Lock = multiprocessing.Lock()
    # Write the updated contents back to the CSV file
    Lock.acquire()  # Critical section for write in files
    with open(csv_file, 'w', newline='') as file:
        fieldnames = csv_reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    Lock.release()

    print(f"Value in row {row_id}, column {column_name} updated to {new_value}.")



def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#DATE

def formato_data():
    # Definisci i nomi dei giorni della settimana e dei mesi
    nomi_giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre",
                "Ottobre", "Novembre", "Dicembre"]

    # Ottieni la data e l'ora attuali
    oggi = datetime.datetime.now()

    # Ottieni il giorno della settimana, il giorno del mese e il mese attuali
    giorno_settimana = nomi_giorni[oggi.weekday()]
    giorno_mese = oggi.day
    mese = nomi_mesi[oggi.month - 1]
    anno = oggi.year

    # Costruisci la stringa con il formato richiesto
    data_formattata = f"{giorno_settimana} {giorno_mese} {mese} {anno}"
    return data_formattata


def get_current_date():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")


def filter_dates_after_current(dates):
    current_date = datetime.datetime.now()
    matching_rows = []

    for row in dates:
        row_date = datetime.datetime.strptime(row[1], "%d-%m-%Y %H:%M:%S")
        if row_date > current_date:
            matching_rows.append(row)

    return matching_rows