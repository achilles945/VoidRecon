# voidrecon/shell.py

# search

import cmd
import os
import importlib
import voidrecon.core.module as module
import voidrecon.modules as modules
import voidrecon.core.banner as banner

class VoidReconShell(cmd.Cmd):
    prompt = "# VoidRecon > "

    def __init__(self):
        super().__init__()
        self.current_module = None
        self.target = None
        self.port = None

    def do_use(self, arg):
        try:
            self.current_module = module.load_module(arg)
            print(f"[+] Module selected: {arg}")
        except Exception as e:
            print(e)
    def do_set(self, arg):
        parts = arg.split()
        if len(parts) != 2:
            print("[!] Usage: set <OPTIONS> <VALUE>")
            return
        key, value = parts
        if key.upper() == "TARGET":
            self.target = value
        elif key.upper() == "PORT":
            self.port = value
        else:
            print(f"[!] Unknown option: {key}")
            return
        print(f"[+] {key.upper()} set to {value}")

    def do_show(self, arg):
        print("[*] Current Settings:")
        print(f"    Module: {self.current_module.__name__ if self.current_module else 'None'}")
        print(f"    TARGET: {self.target}")
        print(f"    PORT: {self.port}")

    def do_run(self, arg):
        if not self.current_module:
            print("[!] No Module selected. Use 'use' command first.")
            return
        options = {
            'TARGET': self.target,
            'PORT': self.port
        }
        try:
            print("[*] Running module...")
            module.run_module(self.current_module, options)
        except Exception as e:
            print(e)
    
    def do_clear(self, arg):
        os.system('clear')

    def do_search(self, arg):
        a = 0
        dirs = ['network', 'webrecon', 'credentials', 'vulns', 'whois' ]
        for i in dirs :
            full_path = f'modules.{i}.{arg}'
            try:
                full_path = f'modules.{i}.{arg}'
                module = importlib.import_module(full_path)
                #print (f'[+] Module found: {full_path}' )
                a = 1
                break
            except ModuleNotFoundError as e:
                pass
        if a == 1:
            print (f'[+] Module found: {full_path}' )
        else: 
            print(f'[!] Module not found: {arg}')


    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()

def run():
    banner.print_banner()
    VoidReconShell().cmdloop()



























































































































