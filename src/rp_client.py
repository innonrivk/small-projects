from scapy.all import *
from scapy.layers.l2 import ARP, Ether

SERVER_IP = "4.4.4.4"

def client_arp():
    arp_req= Ether(dst= "ff:ff:ff:ff:ff:ff") / ARP(pdst=SERVER_IP)
    resp = srp1(arp_req, timeout = 5, verbose = 0)
    resp.show()
if __name__ == '__main__':
    client_arp()