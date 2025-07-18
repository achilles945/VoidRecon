# /voidrecon/core/base.py

# Core logic of VoidRecon

import importlib
from voidrecon.core import shell
import voidrecon.core.modrunner as modrunner
import voidrecon.modules as modules
import voidrecon.core.banner as banner


class Recon():
    def __init__(self):
        super().__init__()
        self.options = {}
        self.current_module = None
        self.target = None
        self.port = None


    #==================================================
    # System & Utility Functions
    #==================================================


    def start(self):  
        banner.print_banner()

    def help(self):
        # logic to show help page
        return 0

    def create_module(self):
        # logic to create custom module by user
        return 0

    def custom_module_template(self):
        # logic to show custom module template to user
        return 0

    def validate_module(self):
        # logic to check whether module is valid
        return 0


    #==================================================
    # Module Management Methods
    #==================================================

    def list_modules(self):
        # logic to list modules
        return 0

    def search_modules(self, keyword):
        # logic to search modules
        a = 0
        dirs = ['network', 'webrecon', 'credentials', 'vulns', 'whois' ]
        for i in dirs :
            full_path = f'voidrecon.modules.{i}.{keyword}'
            try:
                full_path = f'voidrecon.modules.{i}.{keyword}'
                module = importlib.import_module(full_path)
                #print (f'[+] Module found: {full_path}' )
                short_path = f'modules.{i}.{keyword}'
                a = 1
                break
            except ModuleNotFoundError as e:
                pass
        if a == 1:
            #print (f'[+] Module found: {full_path}' )
            print (f'[+] Module found: {short_path}' )
        else: 
            print(f'[!] Module not found: {keyword}')

        return short_path


    def load_module(self, arg):
        # logic to load module
        try:
            self.current_module = modrunner.module_loader(arg)
            print(f"[+] Module selected: {arg}")
            print(f"[DEBUG] Loaded module object: {self.current_module}")
        except Exception as e:
            print(e)

    def module_info(self):
        # logic to show modules information 
        return 0


    #==================================================
    # Options & Configuration Handling 
    #==================================================


    def show_options(self, options):
        # logic to show options
        return 0

    def set_option(self, key, value):
        self.options[key] = value

    def unset_options(self, key):
        # logic to unset options 
        return 0 


    #==================================================
    # Module Execution Methods
    #==================================================


    def run_module(self):
        # logic to run the selected module with options
        if not self.current_module:
            print("[!] No Module selected. Use 'use' command first.")
            return
        options = {
            'TARGET': self.target,
            'PORT': self.port
        }
        try:
            print("[*] Running module...")
            modrunner.run_module(self.current_module, options)
        except Exception as e:
            print(e)
        return "Module executed"

    def stop_module(self):
        # logic to stop execution of module
        return 0 


    

