import os
import colorama
from colorama import Fore as f
from cryptography.fernet import Fernet
from pyfiglet import figlet_format as ff

colorama.init(autoreset=True)

class Encrypt:

    

    def __init__(self) -> None:
        print(f.YELLOW + ff("Encrypter 0.1"))
        self.key =  Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_string(self,string) -> str:
        return self.cipher_suite.encrypt(string)

    def decrypt_string(self,string) -> str:
        return self.cipher_suite.decrypt(string)


        

    """
    def ecrypt_file(self,fname) -> None:
        dlist = os.listdir()
        is_found = False

        for __file__ in dlist:
            if __file__ == fname:
                is_found == True
        
        if not is_found:
            print(f.RED + "file not found")

        #continue later
    """