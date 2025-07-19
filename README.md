# VoidRecon


The VoidRecon is a modular reconnaissance tool for ethical hackers, bug bounty hunters, and red teamers.

---

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Logic](#logic)
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
│   │   ├── shell.py                 # CMD Shell
│   │   ├── base.py                  # Main Logic
│   │   ├── banner.py                # Banner
│   │   ├── web/
│   │
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── module_list.txt
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


## Logic

```
                            +------------------+
                            |  voidrecon.py    |  <-- Entry Point
                            +--------+---------+
                                    |
            +------------------------+-------------------------+
            |                                                  |
    +------------------+                             +------------------+
    |  Shell Interface |                             |  Web Interface   |
    |   (shell.py)     |                             |   (web.py)       |
    +--------+---------+                             +--------+---------+
            |                                                  |
            |                                                  |
            v                                                  v
+---------------------------+                   +---------------------------+
|       Core Engine         |  <-------------   |       Core Engine         |
|      (base.Recon)         |                   |      (base.Recon)         |
+-----------+---------------+                   +-----------+---------------+
            |                                                   |
     +------+-------+                                   +-------+-------+
     |    Module    |                                   |     Module    |
     |   Execution  |                                   |    Execution  |
     +--------------+                                   +---------------+

```


## Example Usage

### Shell Mode

```bash
python3 voidrecon.py
VoidRecon > use network/portscan
VoidRecon > set TARGET 192.168.1.1
VoidRecon > set PORT 80
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

