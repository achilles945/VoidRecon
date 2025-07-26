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
        - Database Mnagement
            - create_data_db()                 Done
            - create_tasks_db()                Done
            - activate_db()                    Done
            - insert_into_table()
            - select_from_table()
            - log_tasks()
            - get_tasks()
            - update_table()
            - delete_from_table()
        - Workspace & Project Management
            - create_workspace(name)           Done
            - switch_workspace(name)           Done         
            - list_workspaces()                Done
            - delete_workspace(name)           Done
            - rename_workspace(old, new)       Done
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


```
self.recon.insert_into_table("domains", {
    "domain": "example.com",
    "notes": "Found via Google dork",
    "module": "google_dork"
})

```

```
module = "dns_resolver"
args = {"domain": "example.com"}
status = "completed"
start_time = "2025-07-24 18:00:00"
end_time = "2025-07-24 18:00:05"
result = "Resolved 3 A records"
notes = "Ran with default settings"

self.log_tasks("tasks", {
    "module": module,
    "arguments": str(args),  # Serialize dict to string
    "status": status,
    "start_time": start_time,
    "end_time": end_time,
    "result": result,
    "notes": notes
}) 

```



## Database

    # VoidRecon Database Tables

    - companies — Stores company names and related organizational details.
    - contacts — Contains personal information such as names, titles, and phone numbers.
    - credentials — Holds usernames, passwords, or hashes collected during recon.
    - domains — Lists domain names discovered as part of the target scope.
    - emails — Contains email addresses found during information gathering.
    - hosts — Stores hostnames and IP addresses related to targets.
    - locations — Records physical or geographical location data.
    - netblocks — IP address ranges (CIDR blocks) associated with targets.
    - ports — Details open ports and associated services on hosts.
    - profiles — Social media and user profile data (e.g., LinkedIn, GitHub).
    - vulnerabilities — Information on vulnerabilities (CVEs or custom) linked to assets.
    - websites — URLs of websites discovered within the reconnaissance.
    - pages — Metadata about individual web pages such as titles and hashes.
    - repositories — Public code repositories connected to profiles or domains.
    - whois — WHOIS registration data for domains.
    - modules — Logs and metadata about module executions.
    - notes — Analyst notes or custom comments on targets.
    - settings — Configuration and API keys for modules and workspaces.
