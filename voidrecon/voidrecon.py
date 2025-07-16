# voidrecon/voidrecon.py
import textwrap
import argparse
from core import module_loader, module_runner
import visual, shell
import sys

def main():
    parser = argparse.ArgumentParser(
        description="VoidRecon CLI Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            voidrecon.py --module network.portscan --target 192.168.1.1 --port 21
            voidrecon.py --shell
            voidrecon.py --gui
        '''))
    parser.add_argument('--shell', action='store_true', help='Launch Shell Interface')
    parser.add_argument('--gui', action='store_true', help='Launch Graphical Interface')
    parser.add_argument('--module', help='Module name (e.g., network.portscan)')
    parser.add_argument('--target', help='Target IP or domain')
    parser.add_argument('--port', help='Optional port')
    args = parser.parse_args() 

    if args.shell :
        try: 
            shell.run()
            
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(f"[!] Error while running interface: {e}")
    elif args.gui :
        try: 
            interface_class = getattr(visual, 'Main')
            instance = interface_class()
            instance.run()
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(f"[!] Error while running interface: {e}")
    else :
        # Load the module
        mod = module_loader.load_module(args.module)
        # Prepare options to pass to the module
        options = {
            'TARGET': args.target,
            'PORT': args.port
        }
        # Run the module
        module_runner.run_module(mod, options)

if __name__ == '__main__':
    main()
