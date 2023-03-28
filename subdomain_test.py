import socket

def subdomain_enum(tld):
    # Enumerate subdomains
    subdomains = []
    with open("subdomains.txt", "r") as sublist:
        for line in sublist:
            sub = line.strip() + "." + tld
            try:
                ip = socket.gethostbyname(sub)
                subdomains.append(sub)
                print(f"{sub} has IP address: {ip}")
            except socket.gaierror:
                pass
    return subdomains

if __name__ == "__main__":
    tld = input("Enter the top-level domain: ")
    subdomains = subdomain_enum(tld)
    print(f"Found {len(subdomains)} subdomains for {tld}.")
