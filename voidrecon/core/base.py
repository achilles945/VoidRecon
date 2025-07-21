# /voidrecon/core/base.py

# Core logic of VoidRecon

import sys
import os
import importlib
from shutil import copyfile
from pathlib import Path
from voidrecon.core import shell
import voidrecon.modules as modules
import voidrecon.core.banner as banner


class Recon():
    def __init__(self):
        super().__init__()
        self.options = {}
        self.current_module = None
        base_path = Path.cwd() / "voidrecon"
        self.module_list_path = base_path / "modules" / "module_list.txt"
        self.module_path_list_path = base_path / "modules" / "module_path_list.txt"


    #==================================================
    # System & Utility Functions
    #==================================================



    #==================================================
    # Module Management Methods
    #==================================================

    def list_modules(self):
        # logic to list modules
        modlist = []
        file_path = self.module_list_path
        with open(file_path, 'r') as f:
            modlist = [line.strip() for line in f if line.strip()]
        return modlist


    def search_modules(self, keyword):
        # logic to search modules
        search_list = []
        a = 0
        file_path = self.module_list_path
        
        with open(file_path, 'r') as f:
            search_list = [line.strip() for line in f if keyword in line ]
        return search_list


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
        self.current_module = importlib.import_module(full_path)
        info = getattr(self.current_module, 'info')
        return info



    def module_add(self, current_path, mod_name):
        # logic to create custom module by user

        final_path = Path.cwd() / "voidrecon" / "modules" / "custom" / f"{mod_name}.py"
        copyfile(current_path, final_path)

        file_path = self.module_list_path
        with open(file_path, 'a') as f:
            f.write(f"\ncustom.{mod_name}")


        file_path = self.module_path_list_path
        with open(file_path, 'a') as f:
            f.write(f"\ncustom.{mod_name}:{final_path}")


        return f"Module added {mod_name}"
    

    def module_delete(self, value):
        # logic to delete module
        module_name = value
        mod_to_delete = None
        modpath_path_list = None
        modname_path_list = None
        

        file_path = self.module_path_list_path
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ':' not in line:
                    continue
                modname, modpath = line.split(":", 1)
                modpath_path_list = modpath.strip()
                modname_path_list = modname.strip()

                if modname.strip() == module_name:
                    mod_to_delete = modpath.strip()
                    print(modpath.strip())
                    break

        if mod_to_delete:
            mod_path = Path(mod_to_delete)
            if mod_path.is_file():
                os.remove(mod_path)

                with open(file_path, 'r') as f:
                    lines = f.readlines()

                with open(file_path, 'w') as f:
                    for line in lines:
                        if line.strip() != f"{modname_path_list}:{modpath_path_list}":
                            f.write(line)



                file_path = self.module_list_path

                with open(file_path, 'r') as f:
                    lines = f.readlines()
            
                with open(file_path, 'w') as f:
                    for line in lines:
                        if line.strip() != value:
                            f.write(line)

                return f"[INFO] Module deleted: {module_name}"

        else:
            return f"[WARN] Module '{module_name}' not found or file does not exist."

        


    def module_template(self):
        # logic to show custom module template to user

        module_template_path_full = Path.cwd() / "voidrecon" / "core" / "module_template.py"
        
        dst_path = Path.home() / "module_template.py"

        copyfile(module_template_path_full, dst_path)

        


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



    

