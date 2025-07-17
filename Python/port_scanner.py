import socket
import threading

target_ip = input("[*]Enter the target IP address: ")
open_ports = []

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

start_port = int(input("[*]Enter the starting port number: "))
end_port = int(input("[*]Enter the ending port number: "))  

print("[*]Starting port scan...")
threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()  

for thread in threads:
    thread.join()   

print("[*]Port scan completed.")
if open_ports:
    print("[*]Open ports found:")
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print("[*]No open ports found.")
print("[*]Exiting port scanner.")