
import whois
import json

info = {
    "name": "WHOIS Lookup",
    "description": "Retrieve historical/current DNS records (A, AAAA, CNAME, MX, NS).",
    "author": "Achilles",
    "options": "TARGET"
}

option_template = {
    'TARGET': None,            # IP or domain 
    #'PORT': None,              # Optional port or range
    #'URL' : None,             # Full URL (https://example.com)
    #'WORDLIST' : None         # Path to a wordlist
    #'EMAIL' : None            # Target email address        
    #'USERNAME' : None         # Target username    
    #'FILE' : None             # Path to file for metadata/hash
    #'API-KEY' : None          # API key for services (Shodan, VirusTotal, etc.)

}
    


class Recon():
    def __init__(self, options):
        super().__init__()
        self.target = options.get('TARGET')



    def format_datetime(self,dt):
        if not dt:
            return None
        if isinstance(dt, list):
            # Convert each datetime in the list to ISO format
            return [d.isoformat() if hasattr(d, 'isoformat') else str(d) for d in dt]
        else:
            return dt.isoformat() if hasattr(dt, 'isoformat') else str(dt)


        
    def run(self):
        print(f"[*] Performing WHOIS Lookup on: {self.target}")
        data = self.whois_lookup()
        if data:
            print(json.dumps(data, indent=4))
            collected_data = {
                "module_name" : "whois",
                "data" : data
            }
            return collected_data

    def whois_lookup(self):
        try:
            w = whois.whois(self.target)
            result = {
                "domain_name": json.dumps(w.domain_name) if w.domain_name else None,
                "registrar": json.dumps(w.registrar) if w.registrar else None,
                "creation_date": json.dumps(self.format_datetime(w.creation_date)) if isinstance(w.creation_date, list) else self.format_datetime(w.creation_date),
                "expiration_date": json.dumps(self.format_datetime(w.expiration_date)) if isinstance(w.expiration_date, list) else self.format_datetime(w.expiration_date),
                "name_servers": json.dumps(w.name_servers) if w.name_servers else None,
                "emails": json.dumps(w.emails) if w.emails else None,
                "status": json.dumps(w.status) if w.status else None,
                "module": "whois"
            }


            return result
        except Exception as e:
            print(f"Error: {e}")
            return None



