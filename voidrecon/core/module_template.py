# module_template.py



info = {
    "name": "",
    "description": "",
    "author": "YourName",
    "options": {
        "OPTION": "OPTION Description"
        "OPTION": "OPTION Description"
        "OPTION": "OPTION Description"
    }
}

option_template = {
    #'TARGET': None,            # IP or domain 
    #'PORT': None,              # Optional port or range
    #'URL' : None,             # Full URL (https://example.com)
    #'WORDLIST' : None         # Path to a wordlist
    #'EMAIL' : None            # Target email address        
    #'USERNAME' : None         # Target username    
    #'FILE' : None             # Path to file for metadata/hash
    #'API-KEY' : None          # API key for services (Shodan, VirusTotal, etc.)
    # More Options

}
    


class Recon:
    def __init__(self, options):
        # self.target = options.get('TARGET')         # global variable
        # self.port = options.get('PORT')             # global variable 

    def run(self):
        print(f"[*] Running Scanner")
        self.scanner_name()

    def scanner_name(self):
        
        # Main Script Logic
