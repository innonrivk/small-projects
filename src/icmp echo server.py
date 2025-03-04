from scapy.all import *
from scapy.layers.inet import *

def filer_icmp(pack):
    return  ICMP in pack and pack[ICMP].type == 8

def build_pac(ip):
   icmp_pack  = IP(dst = ip) / ICMP(type = 0)
   return icmp_pack

def prn_act(pack):
    print("hi")
    #sr(build_pac(pack[ICMP].src))


sniff(lfilter= filer_icmp, prn = prn_act)



