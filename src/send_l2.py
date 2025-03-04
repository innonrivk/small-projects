
def sr_l2_packet(pkt):
    resp = srp1(pkt, verbose=0, timeout=2)
    if resp is not None:
        print(f'MAC Src: {resp[Ether].src} MAC Dst: {resp[Ether].dst}')
        print(f'IP Src: {resp[IP].src}   IP Dst: {resp[IP].dst}')
        print(f'ICMP Response Data: {resp[Raw].load}')
    else:
        print("No answer")
