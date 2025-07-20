# voidrecon/modules/network/portscan.py

import socket


info = {
    "name": "Port Scanner",
    "description": "Scans a range of TCP ports on the target",
    "author": "YourName",
    "options": {
        "TARGET": "Target IP or hostname",
        "PORT": "Comma-separated port list or single port (e.g., 22,80,443)"
    }
}

option_template = {
    'TARGET': None,            # IP or domain 
    'PORT': None,              # Optional port or range
    #'URL' : None,             # Full URL (https://example.com)
    #'WORDLIST' : None         # Path to a wordlist
    #'EMAIL' : None            # Target email address        
    #'USERNAME' : None         # Target username    
    #'FILE' : None             # Path to file for metadata/hash
    #'API-KEY' : None          # API key for services (Shodan, VirusTotal, etc.)

}
    


class Recon:
    def __init__(self, options):
        self.target = options.get('TARGET')
        ports = options.get('PORT')
        if ports:
            self.ports = [int(p.strip()) for p in ports.split(',')]
        else:
            self.ports = list(range(1, 1025))  # Default to top 1024 ports

    def run(self):
        print(f"[*] Scanning {self.target} on ports: {self.ports}")
        for port in self.ports:
            self.scan_port(port)

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")
