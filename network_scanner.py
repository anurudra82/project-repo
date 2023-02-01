import scapy.all as scapy


def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # scapy.ls(scapy.Ether()) # list all the options which set
    # print(broadcast.summary())

    # combine both the packet.
    arp_request_broadcast = broadcast / arp_request
    # arp_request_broadcast.show()
    # print(arp_request_broadcast.summary())

    #  sending packet and receiving the response.

    # answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    answered = scapy.srp(arp_request_broadcast, timeout=1)[0]
    #  srp function sending and recieving packet of the client which have an same network.

    # print(answered.summary())
    # print(unanswered.summary())

    print("IP\t\t\tMAC ADDRESS\n---------------------------------------------------------")

    for element in answered:
        # print(element[1].show()) # 
        # print(element[1].psrc) # it provide the ip address.
        # print(element[1].hwsrc) # it provide the mac address.
        # print("---------------------------------------------------------------------------")

        print(element[1].psrc + "\t\t" + element[1].hwsrc )

# router_ip = input("Enter our router ip : ")
scan("192.168.1.1/24")
