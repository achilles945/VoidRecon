# voidrecon/core/scanner_runner.py

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
