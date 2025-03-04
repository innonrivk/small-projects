from scapy.all import *
from scapy.layers.inet import *
import time

MAX_TTL = 255
def build_packet(destination_ip, ttl):
    return IP(dst=destination_ip, ttl=ttl) / ICMP(type=8) / Raw(b"baabafadbdf")



def get_hop_ip(stability_score, destination_ip, ttl_counter):
    time_lst = []
    responses = sr1(build_packet(destination_ip, ttl_counter), verbose=0,timeout= 5)
    if responses != None:
        current_hop_ip = responses[IP].src
    else:
        time_lst = ["x","x","x"]
        return "Request timed out", time_lst
    second_hop_ip = ""
    hop_stability_counter = 0
    while hop_stability_counter < stability_score:
        t1 = time.time()
        responses = sr1(build_packet(destination_ip, ttl_counter), verbose=0,timeout= 5)
        second_hop_ip = responses[IP].src

        if second_hop_ip == current_hop_ip:
            hop_stability_counter += 1
        else:
            hop_stability_counter = 0
            current_hop_ip = second_hop_ip
        t2 = time.time()
        time_lst.append( "{:.2f} ms".format(t2 - t1))
    return current_hop_ip, time_lst


def traceroute(destination_ip):
    ttl_counter = 1
    current_hop_ip = ""
    while (current_hop_ip != destination_ip) and (ttl_counter !=  MAX_TTL):
        current_hop_ip , time =  get_hop_ip(3,destination_ip,ttl_counter)
        print(ttl_counter , *time  , current_hop_ip)
        ttl_counter += 1
    if ttl_counter ==  MAX_TTL:
        print("time to live exceeded")

def main():
    traceroute("8.8.8.8")

if __name__ == '__main__':
    main()


