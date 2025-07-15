# Work to do

This file contain work to do on the tool

## scanner.py

- Better CLI args using argparse:

    - `--list-modules` to show available modules dynamically

    - `--output` to save scan results to a specific file

    - `--json or --yaml` to choose output format

    - `--verbose or --quiet` flags

- Help message with examples in `argparse.ArgumentParser`'s `description`
- Exception handling:
    - Catch ModuleNotFoundError, AttributeError, etc., and give user-friendly errors.
- Parallel scanning (if multiple targets given)
- Module category awareness (e.g., network, webrecon, creds)

## module_loader.py

-  Validate module path:
    - Check if it's a valid submodule
    - Print a helpful message if module doesn’t exist
- Auto-scan available modules:
    - Add a list_modules() function that traverses modules/ dir and returns names
- Module dependency checker
    - Ensure required packages for module are installed 

## scanner_runner.py

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