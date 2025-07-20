# devlopment

This file contains development strategies

## Logic of VoidRecon
    - voidrecon.py - entry point (loads shell interface or web interface)
    - base.py - core logic (can be used by both framework and web interface)
        - System & Utility Functions
            - exit()                           Done
            - clear()                          Done 
            - help()                           Not Done 
            - print_banner()                   Done 
            - version()
            - check_dependencies()
            - update_tool()        
        - module management
            - list_modules()                   Done
            - search_modules()                 Done
            - load_module(path_to_module)      Done  
            - reload_module()                  
            - reload_all_modules()
            - unload_module()
            - module_info()                    Done(NOT Formatted)
            - add_module()                     Done
            - module_template()                Done 
        - Option & Configuration Handling
            - set_option(key, value)           Done
            - unset_option(key)                Done 
            - show_options()                   Done(NOT Formatted)
        - Module Execution
            - run_module()                     Done                 
            - stop_module() 
            - run_all()
        - Data Collection & Results
            - show_results()   
            - clear_results()
            - export_results(format="json/csv/txt")
            - save_results(path)
            - load_results(path)
        - Workspace & Project Management
            - create_workspace(name)
            - switch_workspace(name)
            - list_workspaces()
            - delete_workspace(name)
            - rename_workspace(old, new)
            - backup_workspace(name)
            - import_workspace(path)
        - API Key Management 
            - For modules that rely on external APIs (Shodan, VirusTotal, etc.)
            - add_api_key(service, key)
            - remove_apt_key(services)
            - list_api_keys()
            - validate_api_key(service)
            - save_api_keys(path)
            - load_api_keys(path)
        - Debugging & Development Tools
            - debug_module(name)
            - log_event(event)
            - trace_error()
            - dev_mode()
        - multi-threading support
        - interactive graph view
        

    - module.py - loads and runs module scripts
    - framework.py - shell interface
    - web - web interface (accessed through browser)


## Current Status

- **voidrecon.py**
    - argparse

- **voidrecon/core/banner.py**
    - banner 

- **base.py**
    - nothing 

- **voidreconcore/framework.py**
    - cmd library
        - do_use(): `use`
        - do_set(): `set TARGET google.com`,`set PORT 80`
        - do_show(): `show`
        - do_run(): `run`, 
            - creates 'options' (input api) & gives to module.run_module
        - do_search(): `search <module>`
        - do_exit(): `exit`
        - do_clear(): `clear`
- **voidrecon/core/module.py**
    - load_module()
    - run_module()


## Ideas

- **base.py** 
    - core functions
        - 





- **framework.py**
    - do_show() : `show modules, show options`
    - module dependency check
    - output : `TRUE or False` 
    - add custom modules
    - Running Module
        - load modules
        - parse options
        - validate input
        - call run() with prepared args

- **module.py**
    - load_module()
        - Auto-scan available modules:
            - Add a list_modules() function that traverses modules/ dir and returns names
        - Module dependency checker
            - Ensure required packages for module are installed 
    - run_module()        
        -  Pretty output formatting
            - Clean table output for stdout
            - Save to .json, .txt, or .csv in /output/
        - Timestamped reports
        - Logging support:
            - Log results to a file using your utils/logger.py
        - Standardize module interface
            - Always look for .run(target) and info = {} in each module
        - Error resilience:
            - If a module crashes, handle and continue
        - Chain scans:
            - Run multiple modules on same target (like a scan profile)
