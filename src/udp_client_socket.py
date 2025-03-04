import socket
BUF_SIZE = 4096
LOCAL_SERVER_IP = '127.0.0.1'
UDP_PORT = 5650

serverAddressPort = (LOCAL_SERVER_IP,UDP_PORT)


def UDP_client():
    clinet_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = ""
        while message != "EXIT":
            input_data = input("write message")
            clinet_sock.sendto(input_data.encode(), serverAddressPort)
            data, address = clinet_sock.recvfrom(BUF_SIZE)
            message = data.decode()
            print(message)
    except UnicodeDecodeError as ex:
        print(f"Decode error, ex={ex}")
    except socket.error as ex2:
        print(f"socket error, ex={ex2}")
    finally:
        print("socket close")
        clinet_sock.close()


def main():
    UDP_client()

if __name__ == '__main__':
    main()












