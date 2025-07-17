# voidrecon/voidrecon.py
import textwrap
import argparse
import voidrecon.core.framework as framework
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
    args = parser.parse_args() 
      
    try: 
        framework.run()
    except AttributeError as e:
        print(e)
    except Exception as e:
        print(f"[!] Error while running interface: {e}")

if __name__ == '__main__':
    main()
