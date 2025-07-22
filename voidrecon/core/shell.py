# voidrecon/shell.py

# search

import cmd
import os
import importlib
from platform import system
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
        if system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')


    def do_exit(self, arg):
        print("[+] Exiting VoidRecon Shell...")
        exit()

    def do_help(self, arg):
        help_val = '''

VoidRecon Commands:
-----------------------------------------------------------------------------
exit                                      Exits the framework
help                                      Displays this menu
search <module-name>                      Search a module 
list                                      List all modules
info <module-name>                        Information about module
use <module-name>                         Select module to run
run                                       Execute selected module
show options                              Shows module options
set <option> <value>                      Configure current module options
unset <option>                            Unset the configured module options
module ADD <script-path> <name>           Add custom module
module DELETE <module-name>               Delete custom module  
-----------------------------------------------------------------------------
        '''
        print(help_val)


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
            search_list = self.recon.search_modules(arg)
            if search_list :
                for i in search_list:
                    print (f'[+] Module found: {i}' )
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
                print()
                print(f"[+] Information related to module {arg}:")
                print(" {:<15} {:<90}".format('-----------', '---------------------------------------------------------',))
                for key, value in info.items():
                    print(" {:<15} {:<90}".format(key or "None", value or "None"))
                print(" {:<15} {:<90}".format('-----------', '---------------------------------------------------------',))
                
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
            parts = arg.split()
            option, value1, value2 = parts

        if len(parts) != 2 | len(parts) != 3:
            print("[!] Invalid command")
            return

        if option == 'ADD':
            try:
                a = self.recon.module_add(value1, value2)
                print(a) 
            except Exception as e:
                print(f"[!] Path not found")
                print(e) 
        elif option == 'DELETE':
            try:
                a = self.recon.module_delete(value)
                print(a) 
            except Exception as e:
                print(f"[!] Module not found")
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
                    print()
                    print(" {:<10} {:<15}".format('OPTION', 'CURRENT_VALUE',))
                    print(" {:<10} {:<15}".format('------', '-------------',))
                    for key, value in option_template.items():
                        #print(f"{key} : {option_template[key]}")
                        print(" {:<10} {:<15}".format(key, value or "None"))
                    print(" {:<10} {:<15}".format('------', '-------------',))
                    print()
                    
                else :
                    print(f"[!] No module selected")
            except Exception as e:
                print(e)
        elif arg == 'template':
            try:
                self.recon.module_template()
                print("[+] module_template.py stored in home directory")
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






























































































































