# /voidrecon/core/base.py

# Core logic of VoidRecon

import sys
import os
import importlib
import sqlite3
from shutil import rmtree
from shutil import copyfile
import datetime

from pathlib import Path
from voidrecon.core import shell
import voidrecon.modules as modules
import voidrecon.core.banner as banner


class Recon():
    def __init__(self):
        super().__init__()
        self.options = {}
        self.current_module = None
        self.module_name = None
        base_path = Path.cwd() / "voidrecon"
        self.module_list_path = base_path / "modules" / "module_list.txt"
        self.module_path_list_path = base_path / "modules" / "module_path_list.txt"
        self.workspace = None

        # database management
        self.data_con = None
        self.data_cur = None
        self.tasks_con = None
        self.tasks_cur = None



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
        self.module_name = arg 
        full_path = f'voidrecon.modules.{arg}'
        self.current_module = importlib.import_module(full_path)
        self.options = getattr(self.current_module, 'option_template')

        return self.module_name

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
    # Database Management
    #==================================================



    def activate_db(self, data_file_path, tasks_file_path):
        try:
            # --- Close existing connections before opening new ones ---
            if self.data_con:
                self.data_con.close()
            if self.tasks_con:
                self.tasks_con.close()

            # --- Create new database connections and cursors ---
            self.data_con = sqlite3.connect(data_file_path, check_same_thread=False)
            self.data_cur = self.data_con.cursor()

            self.tasks_con = sqlite3.connect(tasks_file_path, check_same_thread=False)
            self.tasks_cur = self.tasks_con.cursor()


        except Exception as e:
            print(f"Failed to activate the databases: {e}")



    def create_tasks_db(self):
        self.tasks_cur.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT,module TEXT,arguments TEXT,status TEXT,start_time TEXT,end_time TEXT);')
        self.tasks_con.commit()

    def create_data_db(self):
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS domains (domain TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS companies (company TEXT, description TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS netblocks (netblock TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS locations (latitude TEXT, longitude TEXT, street_address TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS vulnerabilities (host TEXT, reference TEXT, example TEXT, publish_date TEXT, category TEXT, status TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS ports (ip_address TEXT, host TEXT, port TEXT, protocol TEXT, banner TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS hosts (host TEXT, ip_address TEXT, region TEXT, country TEXT, latitude TEXT, longitude TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, middle_name TEXT, last_name TEXT, email TEXT, title TEXT, region TEXT, country TEXT, phone TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS credentials (username TEXT, password TEXT, hash TEXT, type TEXT, leak TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS leaks (leak_id TEXT, description TEXT, source_refs TEXT, leak_type TEXT, title TEXT, import_date TEXT, leak_date TEXT, attackers TEXT, num_entries TEXT, score TEXT, num_domains_affected TEXT, attack_method TEXT, target_industries TEXT, password_hash TEXT, password_type TEXT, targets TEXT, media_refs TEXT, notes TEXT, module TEXT)')
        #self.data_con.execute('CREATE TABLE IF NOT EXISTS pushpins (source TEXT, screen_name TEXT, profile_name TEXT, profile_url TEXT, media_url TEXT, thumb_url TEXT, message TEXT, latitude TEXT, longitude TEXT, time TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS profiles (username TEXT, resource TEXT, url TEXT, category TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS repositories (name TEXT, owner TEXT, description TEXT, resource TEXT, category TEXT, url TEXT, notes TEXT, module TEXT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS dashboard (module TEXT PRIMARY KEY, runs INT)')
        self.data_cur.execute('CREATE TABLE IF NOT EXISTS whois (domain_name TEXT, registrar TEXT, creation_date TEXT, expiration_date TEXT, name_servers TEXT, emails TEXT, status TEXT, module TEXT)')
        self.data_cur.execute('PRAGMA user_version = 10')
        self.data_con.commit()



    def insert_into_table(self, table_name: str, data: dict ):
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?'] * len(data))
            values = tuple(data.values())
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.data_cur.execute(query, values)
            self.data_con.commit()
            print("[+] Collected Data stored successfully")
            
        except Exception as e:
            print(f"[!] Failed to insert into table {table_name}: {e}")  



    def get_data(self, table_name): 
        try:
            query = f"SELECT * FROM {table_name}"
            self.data_cur.execute(query)
            rows = self.data_cur.fetchall()
            return rows
        except Exception as e:
            print(f"[!] Failed to select from table {table_name}: {e}")


    def log_tasks(self, data: dict):
        try:
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?'] * len(data))
            values = tuple(data.values())
            query = f"INSERT INTO tasks ({columns}) VALUES ({placeholders})"
            self.tasks_cur.execute(query, values)
            self.tasks_con.commit()
            print("[+] Task logged successfully.")
            
        except Exception as e:
            print(f"[!] Failed to insert into table tasks: {e}") 



    def get_tasks(self):
        try:
            query = f"SELECT * FROM tasks"
            self.tasks_cur.execute(query)
            rows = self.tasks_cur.fetchall()
            return rows
        except Exception as e:
            print(f"[!] Failed to select from table tasks: {e}")



#    def update_table(self):



#    def delete_from_table(self):


    
    #==================================================
    # Workspace & Project Management
    #==================================================


    def create_workspace(self, workspace_name):
        workspace_path = Path.home() / ".voidrecon" / "workspaces" / f"{workspace_name}"
        data_file_path = workspace_path / "data.db"
        tasks_file_path = workspace_path / "tasks.db"
        a = 0
        try:
            os.makedirs(workspace_path, exist_ok=False)
            self.activate_db(data_file_path, tasks_file_path)
            self.create_data_db()
            self.create_tasks_db() 
            self.data_con.close()
            self.tasks_con.close()         
            return f"[+] Workspace {workspace_name} created successfully"
        except Exception as e:
            #return f"[!] Workspace {workspace_name} already exists: {e}"
            return e 


    def switch_workspace(self, workspace_name):
        workspace_path = Path.home() / ".voidrecon" / "workspaces" / f"{workspace_name}"
        data_file_path = workspace_path / "data.db"
        tasks_file_path = workspace_path / "tasks.db"

        if not workspace_path.exists():
            return f"[!] No workspace {workspace_name} found"

        try:
            # --- Ensure previous connections are closed ---
            if self.data_con:
                self.data_con.close()
            if self.tasks_con:
                self.tasks_con.close()

            # --- Activate the new workspace databases ---
            self.activate_db(data_file_path, tasks_file_path)

            # --- Update workspace name and confirm ---
            self.workspace = workspace_name
            return f"[+] Workspace changed to {self.workspace} successfully"

        except Exception as e:
            return f"[!] Cannot switch workspace: {e}"

        


    def list_workspaces(self):
        workspace_dir = Path.home() / ".voidrecon" / "workspaces"
        
        if not workspace_dir.exists():
            return "[!] No workspace directory found"
        
        workspace_list = []
        workspace_list = os.listdir(workspace_dir)
        return sorted(workspace_list)



    def delete_workspace(self, workspace_name):
        workspace_path = Path.home() / ".voidrecon" / "workspaces" / workspace_name
        
        if not workspace_path.exists():
            return f"[!] No workspace {workspace_name} found"

        try:
            rmtree(workspace_path)
            return f"[+] Workspace {workspace_name} deleted successfully"
        except Exception as e:
            return f"[!] Cannot delete workspace: {e}"
    
    def rename_workspace(self, current_name, new_name):
        current_workspace_path = Path.home() / ".voidrecon" / "workspaces" / current_name
        new_workspace_path = Path.home() / ".voidrecon" / "workspaces" / new_name

        if new_workspace_path.exists():
            return f"[!] A workspace named {new_name} already exists"

        if not current_workspace_path.exists():
            return "[!] No workspace directory found"

        try:
            os.rename(current_workspace_path, new_workspace_path)
            return f"[+] Workspace {current_name} name changed to {new_name}"
        except Exception as e:
            return f"[!] Cannot change workspace name: {e}"


    #==================================================
    # Startup Function
    #==================================================

    def start(self):
        workspace = "default"
        self.workspace = workspace
        workspace_path = Path.home() / ".voidrecon" / "workspaces" / f"{workspace}"

        try:
            if not workspace_path.exists():
                self.create_workspace(workspace)
            self.switch_workspace(workspace)
        except Exception as e:
            print(f"[!] Failed to initialize workspace: {e}")


        

    #==================================================
    # Module Execution Methods
    #==================================================


    def run_module(self):
        # logic to run the selected module with options

        module = self.module_name
        args = self.options
        status = "completed"
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()

        data = {
            "module": str(module),
            "arguments": str(args),
            "status": status,
            "start_time": str(start_time),
            "end_time": str(end_time)
        }     

        try:
            mod_class = getattr(self.current_module, 'Recon')
            instance = mod_class(self.options)
            collected_data = instance.run()
            data["end_time"] = datetime.datetime.now()
            self.log_tasks(data) 
            self.insert_into_table(collected_data["module_name"], collected_data["data"]) 
            return True
        except KeyboardInterrupt:
                print("[!] Interrupted by user.")
                data["status"] = "interrupted"
                data["end_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.log_tasks(data)
                return False




        
































