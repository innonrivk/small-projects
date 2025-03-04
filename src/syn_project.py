from scapy.all import *
import random
from scapy.layers.inet import *

DEST_IP = 'walla.co.il'
SCR_PORT =  random.randint(10000, 30000)
syn_segment = TCP(dport=80, sport=SCR_PORT,seq=1234, ack=0, flags="S")

ip_syn_segment= IP(dst=DEST_IP) / syn_segment
ip_syn_segment.show()
# print(ip_syn_segment.__repr__)
# print(ip_syn_segment.summary())
resp = sr1(ip_syn_segment)
resp.show()
if resp[TCP].flags == "SA":
    ack = resp[TCP].seq + 1
    ack_sagment = TCP(dport=80, sport=SCR_PORT,seq=resp[TCP].ack, ack=ack, flags="A")
    ip_ack_sagment = IP(dst=DEST_IP) / ack_sagment
    print(ip_ack_sagment.show())
    send(ip_ack_sagment)

