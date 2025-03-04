import socket

PROTOCOL = "UDP"
BUF_SIZE = 4096
# LOCAL_SERVER_IP = 'localhost'
LOCAL_SERVER_IP = '127.0.0.1'
UDP_PORT = 5650


def udp_server():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = (LOCAL_SERVER_IP, UDP_PORT)
    print(f"starting up on port {UDP_PORT}")
    sock.bind(server_address)

    while True:
        print("\nwaiting to receive message")
        try:
            # Receive and echo
            data, address = sock.recvfrom(BUF_SIZE)
            if data:
                decoded_data = data.decode()
                print(f'received {len(data)} bytes from {address}')
                print("Data: " + decoded_data)
                sent = sock.sendto(data, address)
                print(f"sent {sent} bytes back to {address}")
                if decoded_data.strip() == "EXIT":
                    break
        except ConnectionResetError as ex:
            print(f"Connection reset. ex= {ex}")

    print("\nUDP server exiting")
    sock.close()


def run_server():
    udp_server()


if __name__ == '__main__':
    run_server()
