        a = 0
        dirs = ['network', 'webrecon', 'credentials', 'vulns', 'whois' ]
        for i in dirs :
            full_path = f'voidrecon.modules.{i}.{keyword}'
            try:
                full_path = f'voidrecon.modules.{i}.{keyword}'
                module = importlib.import_module(full_path)
                #print (f'[+] Module found: {full_path}' )
                short_path = f'modules.{i}.{keyword}'
                a = 1
                break
            except ModuleNotFoundError as e:
                pass
        if a == 1:
            #print (f'[+] Module found: {full_path}' )
            #print (f'[+] Module found: {short_path}' )
            return short_path