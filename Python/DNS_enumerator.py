import socket
import dns.resolver

def resolve_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[+] {full_domain} resolved to {ip}")
        return full_domain, ip
    except socket.gaierror:
        print(f"[-] {full_domain} could not be resolved.")
        return None, None

def get_dns_records(domain):
    record_types = ['A', 'NS', 'MX', 'TXT']
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"[+] {record} records for {domain}:")
            for rdata in answers:
                print(f"   {rdata.to_text()}")
        except dns.resolver.NoAnswer:
                print(f"[-] No {record} records found for {domain}.")
        except dns.resolver.NXDOMAIN:
                print(f"[-] Domain {domain} does not exist.")

def enumerate_dns(domain, subdomains):
    with open(wordlist_path) as f:
         subdomains = f.read().splitlines()

    print(f"Enumerating DNS records for {domain}...")
    for sub in subdomains:
         resolve_subdomain(sub, domain)

    print(f"Getting DNS records for {domain}...")
    get_dns_records(domain)

target_domain = input("Enter the target domain: ")
wordlist_path = input("Enter the path to the subdomain wordlist: ")
enumerate_dns(target_domain, wordlist_path)