# voidrecon/shell.py

# search

import cmd
import os
import importlib
from platform import system
import voidrecon.core.base as base


class Shell(cmd.Cmd):

    prompt = "# VoidRecon >"

    def __init__(self):
        super().__init__()
        self.recon = base.Recon()
        self.current_workspace = None
        self.begin()
        self.update_prompt()

        
    def begin(self):
        self.recon.start()



    def update_prompt(self):
        self.current_workspace = self.recon.workspace
        if self.current_workspace:
            self.prompt = f"[VoidRecon: {self.current_workspace}] > "
        else:
            self.prompt = f"[VoidRecon: No Workspace] > "
        


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
exit                                         Exits the framework
help                                         Displays this menu
search <module-name>                         Search a module 
list <modules or workspace>                  List all modules/workspaces
info <module-name>                           Information about module
use <module-name>                            Select module to run
run                                          Execute selected module
show options                                 Shows module options
show template                                Show module template to create custom module
set <option> <value>                         Configure current module options
unset <option>                               Unset the configured module options 
create module <file-path> <module-name>      Create a custom module
delete module <module-name>                  Delete custom module
create workspace <workspace-name>            Create new workspace
delete workspace <workspace-name>            Delete a workspace
rename workspace <current-name> <new-name>   Change name of existing workspace
switch workspace <workspace name>            Change the workspace
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


    #==================================================
    # Module Execution Methods
    #==================================================


    def do_run(self, arg):
        try:
            print("[*] Running module...")
            self.recon.run_module()
        except Exception as e:
            print(f"[!] No module selected: {e}")




    

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
    # Workspace & Project Management / Module Management
    #==================================================



    def do_list(self,arg):


        if arg == "workspaces":
            try :
                out = self.recon.list_workspaces()
                for work in out:
                    print(work)
            except Exception as e :
                print(e)
        elif arg == "modules":
            try :
                modlist = self.recon.list_modules()
                for mod in modlist:
                    print(mod)
            except Exception as e:
                print(f"[!] Error while setting: {e}")


    def do_create(self, arg):
        try:
            parts = arg.split()
            option, value = parts
        except Exception as e:
            parts = arg.split()
            option, value1, value2 = parts

        if option == "workspace":
            try:
                a = self.recon.create_workspace(value)
                print(a)
            except Exception as e:
                print(e)
                return
        elif option == "module":
            try:
                a = self.recon.module_add(value1, value2)
                print(a) 
            except Exception as e:
                print(f"[!] Path not found")
                print(e)
        else :
            print("[!] Invalid option")

    
    def do_delete(self, arg):
        try:
            parts = arg.split()
            option, value = parts
        except:
            print(f"[!] Invalid option")

        if option == "workspace":
            try:
                output = self.recon.delete_workspace(value)
                print(output)
            except Exception as e:
                print(e)

        elif option == 'module':
            try:
                a = self.recon.module_delete(value)
                print(a) 
            except Exception as e:
                print(f"[!] Module not found")
                print(e) 
        else:
            print("[!] Invalid option")

    def do_rename(self, arg):
        try:
            parts = arg.split()
            option, value1, value2 = parts
        except Exception as e:
            print(e)

        if option == "workspace":
            try:
                output = self.recon.rename_workspace(value1, value2)
                print(output)
            except Exception as e:
                print(e)

    def do_switch(self, arg):
        parts = arg.split()
        option, value = parts
        if option == "workspace":
            try:
                a = self.recon.switch_workspace(value)
                self.update_prompt()
                print(a)

            except Exception as e:
                print(e)
                


    def do_tasks(self, arg):

        try:
            rows = self.recon.get_tasks()
            for row in rows:
                for i in row:
                    print(i)
        except Exception as e:
            print(e)
            return

    def do_data(self, arg):

        try: 
            rows = self.recon.get_data(arg)
            for row in rows:
                for i in row:
                    print(i)
        except Exception as e:
            print(e)
            return























































































































