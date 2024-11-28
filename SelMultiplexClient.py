import socket
import sys
import asyncio
import json

from common.full_write import full_write
from common.communication import loadJSONFromFile  # Importa la funzione dal tuo file communication

MAXLINE = 256

async def read_socket(sock):
    received_data = ""
    while True:
        recvbuff = await asyncio.to_thread(sock.recv, MAXLINE)
        if not recvbuff:
            print("EOF on the socket")
            break
        if not recvbuff.strip():
            print("Empty data received. Closing the socket.")
            break
        received_data += recvbuff.decode()
    return received_data


async def client_echo(data, sock):
    # Write the data using full_write
    await asyncio.to_thread(full_write, sock, data.encode())
    # Wait for the socket to be flushed (optional)
    await asyncio.to_thread(sock.shutdown, socket.SHUT_WR)
    return await read_socket(sock)


def launchMethod(input: str, config_file: str = "server_address.json"):
    # Usa loadJSONFromFile per leggere il file di configurazione
    server_config = loadJSONFromFile(config_file)
    server_address = server_config["address"]
    server_port = server_config["port"]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_add = (server_address, server_port)

    try:
        sock.connect(serv_add)
        print(f"Connection to {serv_add} established!")
    except Exception as e:
        print(f"Connection error: {e}")
        sys.exit(1)

    result = asyncio.run(client_echo(input, sock))

    # Close the socket after finishing the data stream
    sock.close()

    return result


if __name__ == "__main__":
    # Esempio di dati di input
    input_data = {
        "header": {"Action": "ExampleAction"},
        "payload": {"Key1": "Value1", "Key2": "Value2"}
    }
    # Converte l'input in formato JSON
    result = launchMethod(json.dumps(input_data))
    print("Response from server:", result)