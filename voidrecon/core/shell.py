# voidrecon/shell.py

# search

import cmd
import os
import importlib
import voidrecon.core.base as base

class Shell(cmd.Cmd):
    prompt = "# VoidRecon > "


    def __init__(self):
        super().__init__()
        self.recon = base.Recon()


    #==================================================
    # System & Utility Functions
    #==================================================

    def do_clear(self, arg):
        os.system('clear')


    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()

    
    def do_help(self):
        return 0



    #==================================================
    # Module Management Methods
    #==================================================


    def do_use(self, arg):
        try:
            module_name = self.recon.load_module(arg)
            print(f"[+] Module selected: {module_name}")
        except Exception as e:
            print(f"[!] Module not selected: {e}")


    def do_search(self, arg):
        try:
            module_path = self.recon.search_modules(arg)
            if module_path != False:
                print (f'[+] Module found: {module_path}' )
            else:
                print(f'[+] Module not found: {arg}')
        except Exception as e:
            print(f"Error while searching module: {e}")


    def do_list(self,arg):
        try :
            modlist = self.recon.list_modules()
            for mod in modlist:
                print(mod)
        except Exception as e:
            print(f"[!] Error while setting: {e}")
    

    def do_info(self, arg):     # Info formatting to do
        if arg :
            try :
                info = self.recon.module_info(arg)
                for key in info:
                    print(f"{key} : {info[key]}")
            except Exception as e:
                print(e)
        else:
            print("[!] Usage: set <MODULE_NAME>")            



    def do_module(self, arg):
        # ADD, DELETE, CHECK
        try:
            parts = arg.split()
            option, value = parts
        except Exception as e:
            print(e)

        if len(parts) != 2:
            print("[!] Usage: set <OPTIONS> <VALUE>")
            return

        if option == 'ADD':
            try:
                self.recon.module_add(value)
            except Exception as e:
                print(f"[!] Path not found")
                print(e) 
        elif option == 'DELETE':
            try:
                self.recon.module_delete(value)
            except Exception as e:
                print(f"[!] Module not found")
                print(e) 

        elif option == 'CHECK':
            try:
                self.recon.module_check(value)
            except Exception as e:
                print(f"[!] module not found")
                print(e) 
        else:
            print("[!] Invalid option")
        return 0


    

    #==================================================
    # Options & Configuration Handling 
    #==================================================


    def do_set(self, arg):
        parts = arg.split()
        setkey, setvalue = parts
        if len(parts) != 2:
            print("[!] Usage: set <OPTIONS> <VALUE>")
            return
        try :
            a = self.recon.set_option(arg)
            print(a)
        except Exception as e:
            print(f"[!] Error while setting option: {e}")

    
    def do_unset(self, arg):
        try:
            a = self.recon.unset_option(arg)
            if a == True:
                print(f"{arg}: None")
        except Exception as e:
            print(f"[!] Error while unsetting option: {e}")


    def do_show(self, arg):
        if arg == 'options':
            try:
                option_template = self.recon.show_options()
                if option_template != False:
                    for key in option_template:
                        print(f"{key} : {option_template[key]}")
                else :
                    print(f"[!] No module selected")
            except Exception as e:
                print(e)
        else:
            print("[!] Invalid option")


    #==================================================
    # Module Execution Methods
    #==================================================


    def do_run(self, arg):
        try:
            print("[*] Running module...")
            self.recon.run_module()
        except Exception as e:
            print(f"[!] No module selected: {e}")































































































































