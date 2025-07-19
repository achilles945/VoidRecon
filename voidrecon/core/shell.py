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


    def do_use(self, arg):
        try:
            module_name = self.recon.load_module(arg)
            print(f"[+] Module selected: {module_name}")
        except Exception as e:
            print(f"[!] Module not selected: {e}")


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


    def do_run(self, arg):
        try:
            print("[*] Running module...")
            self.recon.run_module()
        except Exception as e:
            print(f"[!] No module selected: {e}")


    def do_clear(self, arg):
        os.system('clear')


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
        try :
            info = self.recon.module_info(arg)
            for key in info:
                print(f"{key} : {info[key]}")
        except Exception as e:
            print(e)



    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()





























































































































