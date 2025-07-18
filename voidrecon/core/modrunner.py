# voidrecon/core/module_loader.py

import importlib


def module_loader(module_name):
    """
    Load module dynamically from voidrecon.modules
    e.g., 'network.portscan' -> voidrecon.modules.network.portscan
    """
    try:
        full_path = f'voidrecon.modules.{module_name}'
        module = importlib.import_module(full_path)
        return module 
    except ModuleNotFoundError as e:
        print(f"[!] Module not found: {module_name}")
        raise e


def run_module(module, options): 
    """
    Run the module after loading.
    Expects the module to have a class called ReconModule.
    """
    try: 
        mod_class = getattr(module, 'ReconModule')
        instance = mod_class(options)
        instance.run()
    except AttributeError:
        print("[!] Module missing 'ReconModule' class.")
    except Exception as e:
        print(f"[!] Error while running module: {e}")
