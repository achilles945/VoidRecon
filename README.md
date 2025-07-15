# VoidRecon


The VoidRecon is a modular reconnaissance tool for ethical hackers, bug bounty hunters, and red teamers.

---

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Example Usage](#example-usage)
- [Planned Modules](#planned-modules)
- [Installation](#installation)
- [License](#license)

---

## Features

- Modular scanner framework
- Support both network and web application recon
- Dynamic module loading
- CLI & Interactive shell interface
- Extensible architecture (add your own modules easily)
- Output reports saved automatically
- Easy to install and use

---

## Directory Structure

```
VoidRecon/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── python-app.yml               # GitHub Actions CI
│   └── CODEOWNERS
│
├── voidrecon/                           # Installable Python package
│   ├── __init__.py
│   ├── scanner.py                       # CLI entry point
│   ├── shell.py                         # Interactive shell
│   ├── visual.py                        # Optional GUI in future
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── module_loader.py             # Dynamic loader
│   │   ├── scanner_runner.py            # Executes modules
│   │   └── state.py                     # Shell state management
│   │
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── network/
│   │   │   ├── __init__.py
│   │   │   ├── portscan.py
│   │   │   ├── ftp-anon.py
│   │   │   └── ping-sweep.py
│   │   ├── webrecon/
│   │   │   ├── __init__.py
│   │   │   ├── http-headers.py
│   │   │   ├── dir-bruteforce.py
│   │   │   └── cms.py
│   │   ├── whois/
│   │   │   ├── __init__.py
│   │   │   ├── whois-lookup.py
│   │   │   └── reverse-whois.py
│   │   ├── vulns/
│   │   │   └── __init__.py
│   │   ├── credentials/
│   │   │   └── __init__.py
│   │   ├── post/
│   │   │   └── __init__.py
│   │   └── auxiliary/
│   │       └── __init__.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py                        # SQLite handling
│   │   └── voidrecon.db                 # Auto-created
│   │
│   ├── output/
│   │   └── report.txt                   # Output file(s)
│   │
│   └── utils/
│       ├── __init__.py
│       └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module_loader.py
│   ├── test_portscan.py
│   └── test_shell.py
│
├── docs/
│   ├── index.md                         # Project overview
│   ├── usage.md                         # How to use
│   ├── dev_guide.md                     # Module writing, contribution
│   └── modules.md                       # Docs for each module
│
├── .gitignore
├── LICENSE                              # e.g. MIT
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── requirements.txt
├── pyproject.toml                       # Modern Python packaging
├── setup.py                             # pip installable
├── setup.cfg                            # Optional tool configs
├── MANIFEST.in                          # Include non-code files
├── README.md                            # Main overview
├── setup.sh                             # Bash installer
└── Dockerfile                           # Optional container build
```

---

## Example Usage

### CLI Mode

```bash
python scanner.py --module portscan --target 192.168.1.1
```

### Shell Mode

```bash
python shell.py
VoidRecon > use network/portscan
VoidRecon > set TARGET 192.168.1.1
VoidRecon > run
```

### Graphical Mode

```
```

---

## Planned Modules

- portscan.py
- ping-sweep.py
- http-headers.py
- cms-detector.py
- ftp-anon.py
- dir-bruteforce.py
- ssh-bruteforce.py
- vuln-checker.py
- ... 

--- 

## Installation

### Quick Install (Linux/macOS)

```bash
chmod +x setup.sh
./setup.sh
```

### Manual (Python 3.8 +)

```bash
pip install -r requirement.txt
```

---

## License

This project is licensed under the MIT License

---

