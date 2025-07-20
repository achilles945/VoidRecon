# /voidrecon/core/base.py

# Core logic of VoidRecon

import os
import importlib
from voidrecon.core import shell
import voidrecon.modules as modules
import voidrecon.core.banner as banner


class Recon():
    def __init__(self):
        super().__init__()
        self.options = {}
        self.current_module = None


    #==================================================
    # System & Utility Functions
    #==================================================


    def help(self):
        # logic to show help page
        return 0


    #==================================================
    # Module Management Methods
    #==================================================

    def list_modules(self):
        # logic to list modules
        modlist = []
        file = "/voidrecon/modules/module_list.txt"
        file_path = os.getcwd() +file
        with open(file_path, 'r') as f:
            for index, line in enumerate(f):
                modlist.append(line)
        return modlist


    def search_modules(self, keyword):
        # logic to search modules
        file = "/voidrecon/modules/module_list.txt"
        file_path = os.getcwd() +file
        with open(file_path, 'r') as f:
            for index, line in enumerate(f):
                if keyword in line:
                    return line
                    break
            else:
                return False


    def load_module(self, arg):
        # logic to load module
        module_name = arg 
        full_path = f'voidrecon.modules.{module_name}'
        self.current_module = importlib.import_module(full_path)
        self.options = getattr(self.current_module, 'option_template')

        return module_name

    def module_info(self, arg):
        # logic to show modules information 
        module_name = arg 
        full_path = f'voidrecon.modules.{module_name}'
        info_module = importlib.import_module(full_path)
        info = getattr(info_module, 'info')
        return info



    def module_add(self, value):
        # logic to create custom module by user
        print(f"Module added {value}")


    def module_check(self, value):
        # logic to check whether module is valid
        print(f"Module Checked {value}")
    

    def module_delete(self, value):
        # logic to delete module
        print(f"Module deleted {value}")

    def module_template(self):
        # logic to show custom module template to user
        print(f"Module template ")


    #==================================================
    # Options & Configuration Handling 
    #==================================================


    def show_options(self):
        # logic to show options
        if self.current_module == None:
            return False
        return self.options



    def set_option(self, arg):

        #option_template = getattr(self.current_module, 'option_template')
        parts = arg.split()
        setkey, setvalue = parts
        for key in self.options:
            if setkey == key :
                self.options[key] = setvalue
                return f"[+] {setkey} set to: {setvalue}"
                break
            else:
                pass
        else :
            return f"Invalid Option!"



    def unset_option(self, key):
        # logic to unset options 
        try:
            self.options[key] = None
            return True
        except Exception as e:
            return False


    #==================================================
    # Module Execution Methods
    #==================================================


    def run_module(self):
        # logic to run the selected module with options
        try:
            mod_class = getattr(self.current_module, 'Recon')
            instance = mod_class(self.options)
            instance.run()
            return True
        except KeyboardInterrupt:
            print("Interrupted!...")
            return



    

