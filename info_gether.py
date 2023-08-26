import whois
import dns.resolver
import shodan
import requests
import socket
import sys
import argparse  # take arguments from command line

argparse = argparse.ArgumentParser(description="This is basic information gathering tool",
                                   usage="Fetching the information")
argparse.add_argument("-d", "--domain", help="Enter the domain name")
argparse.add_argument("-s", "--shodan", help="Enter the ip address")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan

# Whois module block

print("[+] Fetching whois information")

# Creating instances using whois library

try:
    py = whois.query(domain)  # query is the methode of whois. in this query method we pass the domain

    print("[+] whois information found!")
    print()

    print("[+] Name: {}".format(py.name))
    print("[+] Registrar: {}".format(py.registrar))
    print("[+] Registered on: {}".format(py.registrant))
    print("[+] Creation On: {}".format(py.creation_date))
    print("[+] Expire On: {}".format(py.expiration_date))
    print("[+] Status: {}".format(py.status))
    print("[+] Name Server: {}".format(py.name_servers))
    print("[+] country: {}".format(py.registrant_country))
    print("[+] Emails: {}".format(py.emails))

except:
    pass

print()

# DNS module

print("[+] fetching DNS Records......")

try:
    for a in dns.resolver.resolve(domain, "A"):  # resolve is the methode of dns record resolver.
        print("[+] A Record {}".format(a.to_text()))

    for ns in dns.resolver.resolve(domain, "NS"):
        print("[+] NS Record {}".format(ns.to_text()))

    for mx in dns.resolver.resolve(domain, "MX"):
        print("[+] MX Record {}".format(mx.to_text()))

except:
    pass

print()

# geolocation module

print("[+] fetching geolocation information")

try:
    response = requests.Request('GET', "http://geolocation-db.com/json/" + socket.gethostbyname(domain)).json
    print("[+] IP: {}".format(response['ipv4']))
    print("[+] Country code: {}".format(response['country_code']))
    print("[+] Country: {}".format(response['country_name']))
    print("[+] Latitude: {}".format(response['latitude']))
    print("[+] Longitude: {}".format(response['longitude']))
    print("[+] City: {}".format(response['city']))
    print("[+] State: {}".format(response['state']))

except:
    pass

print()

# shodan module use

print("[+] fetching shodan information")

if ip:
    print("[+] fetching information from shodan for IP {}".format(ip))
    # shodan api
    # api = shodan.Shodan("2oPwZiVpVS30xGpjpzS55jJfkIQBV4a8")
    api = shodan.Shodan("PSKINdQe1GyxGgecYz2191H2JoS9qvgD")
    try:
        print("[+] Result found: {}".format(result['total']))
        print("[+] Data \n{}".format(result['data']))
        print()

    except:
        print("[-] Search error occur")
