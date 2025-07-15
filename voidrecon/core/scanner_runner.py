# voidrecon/core/scanner_runner.py

def run_module(module, options):
    """
    Run the module after loading.
    Expects the module to have a class called MetasploitModule.
    """
    try: 
        mod_class = getattr(module, 'MetasploitModule')
        instance = mod_class(options)
        instance.run()
    except AttributeError:
        print("[!] Module missing 'MetasploitModule' class.")
    except Exception as e:
        print(f"[!] Error while running module: {e}")
