import socket
from scapy.all import *
from scapy.layers.inet import *

PROTOCOL = "UDP"
PORT = 5033

def recv_until(connetion,delim):
    data =b""
    while not data.endswith(delim):
        data += connetion.recv(1024)
    return data

def recv_from(server,delim):
    data =b""
    while not data.endswith(delim):
        data += server.revfrom(1024)
    return data


def tcp_server():
    try:
        server_socket = socket.socket()
        server_socket.bind(('127.0.0.1', PORT))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()
    except socket.error:
        print("problem with setting")

    try:
        massege = recv_until(client_socket, "\n")
        client_socket.sendall(massege)
    except socket.error :
        print("problem with setting")

    finally:
        client_socket.close()
        server_socket.close()
        return

def udp_server():
    try:
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server_socket.bind(('127.0.0.1', PORT))

    except socket.error:
        print("problem with setting")

    try:
        massege =  recv_from(server_socket, "\n")
        server_socket.sendall(massege)

    except socket.error:
        print("problem with setting")

    finally:
        server_socket.close()
        return


def main():
    if PROTOCOL == "UDP":
        udp_server()
    elif PROTOCOL == "TCP":
        tcp_server()


if __name__ == '__main__':
    main()
