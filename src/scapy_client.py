from scapy.all import *
from scapy.layers.inet import *
LOCAL_SERVER_IP = '127.0.0.1'
UDP_PORT = 5650

def sr1_udp(data):
        udp_packet = IP(dst=LOCAL_SERVER_IP) / UDP(sport= 4325 ,dport = UDP_PORT) / data
        recv_pkt = sr1(udp_packet, timeout = 2)
        return recv_pkt

def main():
    try:
        message = ""
        while message != "EXIT":
            client_input = input("Enter your message:\n")
            recv_pkt = sr1_udp(client_input)
            message = recv_pkt[Raw].load.decode()
            print(message)
    except TypeError as ex:
        print(f"error,{ex}")
    except UDPerror as ex1:
        print(f"udp error, {ex1}")
    finally:
        print("client close")

if __name__ == '__main__':
    main()





