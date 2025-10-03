# No Database table for this module is created yet

from ipwhois import IPWhois 
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

        
    def run(self):
        print(f"[*] Performing IPWHOIS Lookup on: {self.target}")
        data = self.ipwhois_lookup()
        if data:
            print(json.dumps(data, indent=4))
            collected_data = {
                "module_name" : "ipwhois",
                "data" : data
            }
            return collected_data

    def ipwhois_lookup(self):
        try:
            w = IPWhois(self.target)
            res = w.lookup_rdap(asn_methods=["whois","dns","http"])
            network = res.get("network",{}) 
            result = {
                "IP": res.get("query"),
                "ASN": res.get("asn"),
                "ASN_Description": res.get("asn_description"),
                "Country": res.get("asn_country_code"),
                "Network_CIDR": network.get("cidr"),
                "Registry": res.get("asn_registry"),
                "module": "ipwhois"
            }
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None



