from scapy.all import *
from scapy.layers.inet import *
import random
DEST_IP = 'www.google.com'
ip_layer = IP(dst= DEST_IP, src= "10.0.0.15")
icmp_layer = ICMP()
request_packet = ip_layer / icmp_layer



a = sr1(request_packet)
a.show()
