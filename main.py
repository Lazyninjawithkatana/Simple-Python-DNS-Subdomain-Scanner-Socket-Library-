import socket
from colorama import Fore, Style, init

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

def dns_list_():
    seclist = []
    try:
        with open('bitquark-subdomains-top100000.txt', 'r', encoding='utf-8') as w:
            for line in w:
                strip_line = line.strip()
                if strip_line:
                    seclist.append(strip_line)
        return seclist
    except Exception as e:
        print(f'{RED}[!] Error with {e}{RESET}')
        return []
    
def main_dns(target):
    dns_list_0 = dns_list_()
    for d in dns_list_0:
        try:
            response_dns = socket.gethostbyname(f'{d}.{target}')
            if response_dns:
                print(f'{GREEN}[#] Response from {d}.{target}{RESET}')
                with open('success_ip_addresses_from_target.txt', 'a') as t:
                    t.write(f'{d}.{target} RESPONSED IP --> {response_dns}\n')
        except Exception as e:
            print(f'{RED}Error with {e}{RESET}')

if __name__ == '__main__':
    user_target_input = str(input('#example.com#\nType your target --> '))
    main_dns(user_target_input)