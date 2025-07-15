# voidrecon/scanner.py

import argparse
from core import module_loader, scanner_runner

def main():
    parser = argparse.ArgumentParser(description="VoidRecon CLI Scanner")
    parser.add_argument('--module', required=True, help='Module name (e.g., network.portscan)')
    parser.add_argument('--target', required=True, help='Target IP or domain')
    parser.add_argument('--port', help='Optional port')
    args = parser.parse_args() 

    # Load the module
    mod = module_loader.load_module(args.module)

    # Prepare options to pass to the module
    options = {
        'TARGET': args.target,
        'PORT': args.port
    }

    # Run the module
    scanner_runner.run_module(mod, options)

if __name__ == '__main__':
    main()
