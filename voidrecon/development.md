# devlopment

This file contains development strategies

## Current Status

- **voidrecon.py**
    - argparse
        - `--shell, --gui, -m --module, -t --target, -p --port`
    - shell module call
    - gui module call
    - creates 'options' (input api) & gives to module_runner.py
- **shell.py**
    - banner
    - cmd library
        - do_use(): `use`
        - do_set(): `set TARGET google.com`,`set PORT 80`
        - do_show(): `show`
        - do_run(): `run`, 
            - creates 'options' (input api) & gives to module_runner.py
        - do_search(): `search <module>`
        - do_exit(): `exit`
        - do_clear(): `clear`
- **visual.py**
    - Nothing
- **core/module_loader.py**
    - importlib
    - loads module
- **core/module_runner.py** 
    - runs module
    - takes 'options' (input api) as input


## Ideas
- **shell.py**
    - do_show() : `show modules, show options`
    - module dependency check
    - output : `TRUE or False` 
    - add custom modules
    - Running Module
        - load modules
        - parse options
        - validate input
        - call run() with prepared args

- **module_loader.py**
    - Auto-scan available modules:
        - Add a list_modules() function that traverses modules/ dir and returns names
    - Module dependency checker
        - Ensure required packages for module are installed 

- **module_runner.py**
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
- **shell.py**

- **visual.py**
    - Graphical version of tool    