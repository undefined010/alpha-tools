import os
import colorama
from colorama import Fore as f
from cryptography.fernet import Fernet
from pyfiglet import figlet_format as ff

colorama.init(autoreset=True)

class Encrypt:

    

    def __init__(self,string) -> None:
        print(f.YELLOW + ff("Encrypter 0.1"))

        self.key =  Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_string(self,string) -> bytes:
        return self.cipher_suite.encrypt(string)

    def decrypt_string(self,string) -> bytes:
        return self.cipher_suite.decrypt(string)

    def encrypt_file(self , fname) -> None:
        fun = lambda a ,b  : a == b
        cheak = [fun(fname,i) for i in os.listdir() if fun(fname,i)]
        f = []


        if len(cheak) == 0:
            print(f.RED + "File not found")

        with open(fname,'rb') as read_file:
            f = read_file.readlines()
            read_file.close()
            
        encrypt_f = [self.encrypt_string(i) for i in f]

        with open(fname , 'wb') as write_file:
            write_file.writelines(encrypt_f)
            write_file.close()
    
    def decrypt_file(self,fname) -> None:
        try:
            fun = lambda a ,b  : a == b
            cheak = [fun(fname,i) for i in os.listdir() if fun(fname,i)]
            f = []


            if len(cheak) == 0:
                print(f.RED + "File not found")

            with open(fname,'rb') as read_file:
                f = read_file.readlines()
                read_file.close()
            
            encrypt_f = [self.decrypt_string(i) for i in f]

            with open(fname , 'wb') as write_file:
                write_file.writelines(encrypt_f)
                write_file.close()
        except Exception:
            print(Exception)
    
    