# devlopment

This file contains development strategies

## Logic of VoidRecon
    - voidrecon.py - entry point (loads shell interface or web interface)
    - base.py - core logic (can be used by both framework and web interface)
        - System & Utility Functions
            - exit()                           Done
            - clear()                          Done | Linux , Windows
            - help()                           Done
            - print_banner()                   Done 
            - version()
            - check_dependencies()
            - update_tool()        
        - module management
            - list_modules()                   Done Linux , Windows
            - search_modules()                 Done Linux , Windows
            - load_module(path_to_module)      Done 
            - module_info()                    Done
            - module_add()                     Done Linux , Windows
            - module_delete()                  Done Linux , Windows
            - module_template()                Done Linux , Windows
            - reload_module()                  
            - reload_all_modules()
            - unload_module()
        - Option & Configuration Handling
            - set_option(key, value)           Done
            - unset_option(key)                Done 
            - show_options()                   Done
        - Module Execution
            - run_module()                     Done                  
            - run_all()
        - Data Collection & Results
            - show_results()                   Pending
            - clear_results()                  Pending
            - export_results(format="json/csv/txt")         pending
            - save_result(path)                pending
            - load_result(path)                pending
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

