if setkey.upper() == "TARGET":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "PORT":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "URL":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "WORDLIST":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "EMAIL":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "FILE":
                        self.options[key] = setvalue
                        break
                    elif setkey.upper() == "API-KEY":
                        self.options[key] = setvalue
                        break
                    else:
                        print(f"[!] Unknown option: {key}")
                        break