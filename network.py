import os
import socket
import colorama
from colorama import Fore as f
from pyfiglet import figlet_format as ff

colorama.init(autoreset=True)

"""
self note :- you can use port scan along with ddos to find a port to attack
"""

class Scan:
    
    def __init__(self) -> None:
        os.system('clear')
        print(f.RED + ff("Port Scanner"))

        self.ipv4 = input(f.RED + "Enter a valid ip / hostname to scan: ")
        self.open_ports = []

    def scan(self) -> None:
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.3)
                r = s.connect_ex((self.ipv4 , port))
            
                if r == 0:
                    print(f.CYAN + f'Port {port} is ' + f.GREEN + 'open' + f.CYAN + f' in {self.ipv4}')
                    self.open_ports.append(port)
                s.close()
        except socket.error:
            print(socket.error)
        except KeyboardInterrupt:
            print(KeyboardInterrupt)

    def is_open(self,port) -> bool:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.3)
            if s.connect_ex((self.ipv4 , port)) == 0:
                s.close()
                return True
            else:
                s.close()
                return False
        except socket.error:
            print(socket.error)
            return False
        except KeyboardInterrupt:
            print(KeyboardInterrupt)
            return False

    def get_open_ports(self) -> list:
        return self.open_ports
    
    def save(self,file_name = '') -> None:
        with open(file_name,'w') as wf:
            wf.write(str(self.get_open_ports()))


    def close(self) -> None:
        os.system('clear')

        


        

