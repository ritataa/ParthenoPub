import socket
import sys
import asyncio
import json

from Common.full_write import full_write

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


def launchMethod(input: str, server_address: str, server_port: int):
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
    # Example input data without user and password
    input_data = {"header": "SomeHeader", "payload": {"SomeKey": "SomeValue"}}
    result = launchMethod(json.dumps(input_data), "127.0.0.1", 1024)
    print(result)
