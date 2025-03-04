from  scapy.all import *

def filter_dns(okt):
    return DNS in okt and okt[IP].src == "8.8.8.8"

def print_dns_address(pkt):
    print(pkt[DNS].qd.qname)
    
result = sniff(lfilter = filter_dns, prn = print_dns_address)

