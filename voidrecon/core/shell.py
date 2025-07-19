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
            print(f"[!] Cannot load module {e}")


    def do_set(self, arg):
        parts = arg.split()
        setkey, setvalue = parts
        if len(parts) != 2:
            print("[!] Usage: set <OPTIONS> <VALUE>")
            return
        try :
            a = self.recon.set_option(arg)
            print(f"[+] {setkey} set to: {a}")
        except Exception as e:
            print(f"[!] Cannot set option {e}")

    def do_show(self, arg):
        try:
            print("[*] Current Settings:")
            print(f"    Module: {self.current_module.__name__ if self.current_module else 'None'}")
            print(f"    TARGET: {self.target}")
            print(f"    PORT: {self.port}")
        except Exception as e:
            print(e)


    def do_run(self, arg):
        try:
            print("[*] Running module...")
            self.recon.run_module()
        except Exception as e:
            print(e)


    def do_clear(self, arg):
        os.system('clear')


    def do_search(self, arg):
        try:
            module_path = self.recon.search_modules(arg)
            print (f'[+] Module found: {short_path}' )
        except Exception as e:
            print(e)


    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()





























































































































