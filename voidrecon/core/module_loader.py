# voidrecon/core/module_loader.py

import importlib

def load_module(module_path):
    """
    Load module dynamically from voidrecon.modules
    e.g., 'network.portscan' -> voidrecon.modules.network.portscan
    """
    try:
        full_path = f'modules.{module_path}'
        module = importlib.import_module(full_path)
        return module 
    except ModuleNotFoundError as e:
        print(f"[!] Module not found: {module_path}")
        raise e
