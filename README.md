# VoidRecon


The VoidRecon is a modular reconnaissance tool for ethical hackers, bug bounty hunters, and red teamers.

---

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Example Usage](#example-usage)
- [Planned Modules](#planned-modules)
- [License](#license)

---

## Features

- Modular scanner framework
- Support both network and web application recon
- Dynamic module loading
- Interactive shell interface
- Extensible architecture (add your own modules easily)
- Output reports saved automatically
- Easy to install and use

---

## Directory Structure

```
VoidRecon/
│
├── voidrecon/                           # Installable Python package
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── framework.py             # CMD Shell
│   │   ├── base.py                  # Main Logic
│   │   ├── module.py                # Executes modules
│   │
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── network/
│   │   │   ├── __init__.py
│   │   │   ├── portscan.py
│   │   │   ├── ftp-anon.py
│   │   │   └── ping-sweep.py
│   │   ├── webrecon/
│   │   ├── whois/
│   │   ├── vulns/
│   │   ├── credentials/
│   │   ├── post/
│   │   └── auxiliary/
│   │
│   └── utils/
│       ├── __init__.py
│       └── logger.py
│
├── voidrecon.py                         # CLI Entry Point
├── .gitignore
├── LICENSE                              # e.g. MIT
├── requirements.txt
├── README.md                            # Main overview

```

---

## Example Usage

### Shell Mode

```bash
python3 voidrecon.py
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


### Manual (Python 3.8 +)

```bash
pip install -r requirement.txt
```

---

## License

This project is licensed under the MIT License

---

