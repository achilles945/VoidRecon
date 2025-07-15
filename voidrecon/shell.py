# voidrecon/shell.py

# search, use, set TARGET, set PORT, run

import cmd


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

    def do_use(self, arg):
        print(f"[+] Module selected: {arg}")

    def do_set(self, arg):
        print(f"[+] Set argument: {arg}")

    def do_run(self, arg):
        print("[+] Running module...")

    def do_exit(self, arg):
        print("[+] Exiting...")

    def do_akh(self, arg):
        print("aksdjfkdjsf")


class Main:
    print_banner()
    VoidReconShell().cmdloop()





























































































































