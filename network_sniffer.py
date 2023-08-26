from scapy.all import *
from scapy.layers.inet import IP, TCP  # for taking ip address from ethe0 interface
from scapy.layers.http import HTTPRequest
from colorama import init
import colorama

init()
red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
yellow = colorama.Fore.YELLOW


# iface -> it is the interface which use for sniffing.

def sniff_packets(iface):
    if iface:
        sniff(prn=process_packet, iface=iface)

        # it is for specefic porn 80.
        # sniff(filter="port 80",prn=process_packet,iface=iface)

    else:
        sniff(prn=process_packet)


def process_packet(packet):
    # for TCP packet sniffing
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"{blue} [+] {src_ip} is using port {src_port} to connect {dst_ip} at port {dst_port}")

    if packet.haslayer(HTTPRequest):
        # host is self address aand the path means the other source to request.
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        method = packet[HTTPRequest].Method.decode()

        print(f"{green}[+] {src_ip} is making a HTTP request to {url} with method {method} ") #it is for which methode given like GET or POST

        print(f"{yellow}[+] {packet[HTTPRequest].show()}") #it show all about in the packet header

        print(f"{yellow} {packet.show()}")

    if packet.haslayer(Raw):
        print(f"{red}[+] Usefully raw data: {packet.getlayer(Raw).load}")


sniff_packets("eth0") # in this perameter we will given the interface which we want sniff
