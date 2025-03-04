from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP
import timeit

DEFULT_GATEWAY= "10.0.0.25"


def create_arp_packet(ip_to_find):
    arp_pack = ARP(pdst=ip_to_find)
    return arp_pack

def sr_arp_frame(frame):
    try:
        resp = srp(frame, timeout = 2, verbose = 0)
        return resp
    except TimeoutError as ex:
        print(ex)
        return None



def main():
    frame = create_arp_packet(DEFULT_GATEWAY)
    resp = sr_arp_frame(frame)
    arp_result = scapy.arpin
    if resp is not None:
        print(f"op code = {resp[ARP].op} , HW addr = {resp[ARP].hwsrc} , IP addr = {resp[ARP].psrc}")


if __name__ == '__main__':
    main()
