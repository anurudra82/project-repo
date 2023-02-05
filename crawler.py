import requests

# url = "mail.google.com"
# try:
#     response = requests.get("http://" + url)
#     print(response)
# except requests.exceptions.ConnectionError:
#     pass

# {until this it is used to check website give response or not.}

# ..........................................................


def request(url):
    try:
      return requests.get("http://" + url)
    
    except requests.exceptions.ConnectionError:
       pass
# target_url = input("Enter the target url: ")
target_url = "google.com"
with open("A:\subdomains-wodlist","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        result = word + "." + target_url
        response = print(result)

        if response:
            print("[+] Discovered subdomain -->" + result)

#  {untill that position this fatch the subdomains.}

# ........................................................................


# def request(url):
#     try:
#       return requests.get("http://" + url)
    
#     except requests.exceptions.ConnectionError:
#        pass
# target_url = input("Enter the target url: ")
# with open("D:\directory_files.txt","r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         result = target_url + "/" + word
#         response = print(result)

#         if response:
#             print("[+] Discovered subdomain -->" + result)

# {this is find all files and directories.}

# .........................................................