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
            self.recon.load_module(arg)
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
        try:
            print("[*] Current Settings:")
            print(f"    Module: {self.current_module.__name__ if self.current_module else 'None'}")
            print(f"    TARGET: {self.target}")
            print(f"    PORT: {self.port}")
        except Exception as e:
            print(e)


    def do_run(self, arg):
        try:
            self.recon.run_module()
        except Exception as e:
            print(e)


    def do_clear(self, arg):
        os.system('clear')


    def do_search(self, arg):
        try:
            self.recon.search_modules(arg)
        except Exception as e:
            print(e)


    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()





























































































































