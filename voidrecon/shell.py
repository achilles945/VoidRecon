# voidrecon/shell.py

# search, use, set TARGET, set PORT, run

import cmd
from core import module_loader, scanner_runner

def print_banner():
    banner = r"""
 888     888          d8b      888 8888888b.                                    
 888     888          Y8P      888 888   Y88b                                   
 888     888                   888 888    888                                   
 Y88b   d88P  .d88b.  888  .d88888 888   d88P .d88b.   .d8888b .d88b.  88888b.  
  Y88b d88P  d88""88b 888 d88" 888 8888888P" d8P  Y8b d88P"   d88""88b 888 "88b 
   Y88o88P   888  888 888 888  888 888 T88b  88888888 888     888  888 888  888 
    Y888P    Y88..88P 888 Y88b 888 888  T88b Y8b.     Y88b.   Y88..88P 888  888 
     Y8P      "Y88P"  888  "Y88888 888   T88b "Y8888   "Y8888P "Y88P"  888  888 

                    [*] VoidRecon - Modular Recon Toolkit
    """
    print(banner)


class VoidReconShell(cmd.Cmd):
    prompt = "VoidRecon > "

    def __init__(self):
        super().__init__()
        self.current_module = None
        self.target = None
        self.port = None

    def do_use(self, arg):
        try:
            self.current_module = module_loader.load_module(arg)
            print(f"[+] Module selected: {self.current_module}")
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
            scanner_runner.run_module(self.current_module, options)
        except Exception as e:
            print(e)

    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        return True


class Main:
    print_banner()
    VoidReconShell().cmdloop()





























































































































