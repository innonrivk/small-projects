from scapy.all import *
from scapy.layers.inet import *

MY_MAC =  "AA:AA:AA:AA:AA".lower()

def filter_mac(frame):
    return  (Ether in frame) and (frame[Ether].dst == MY_MAC)

def print_source_adress(frame):
    print(frame[Ether].src)

def sniff_mac():
    sniff(timeout=10, lfilter = filter_mac, prn = print_source_adress )


if __name__ == '__main__':
    sniff_mac()
