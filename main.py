from scanner import Scan,f,ff
from encrypter import Encrypt

def scan():
    s = Scan()
    print("""
    1 - scan all ports in the host
    2 - scan a port in the host  
    """)
    usr_input = int(input(f.RED + 'what mode do you want to chose : '))

    try:
        if usr_input == 1:
            s.scan()
        elif usr_input == 2:
            port = int(input(f.RED + 'enter a port to test it : '))
            val = s.is_open(port)
            if val:
                print(f.GREEN + f'port {port} is open in {s.ipv4}')
            else:
                print(f.RED + f'port {port} isn\'t open in {s.ipv4}')
        else:
            print(f.RED + 'Bad Input !')

    except ValueError:
        print(ValueError)

def encrypt():
    e = Encrypt()
    user_input = str(input(f.YELLOW + 'enter a file in the dir to encrypt it : '))
    e.encrypt_file(user_input)

    

    


def main():
    print(f.YELLOW + ff('Helper'))
    print(f.YELLOW + 'type list to see the availble commands')

    cmd = [
        'LIST',
        'EXIT',
        'SCAN',
        'ENCRYPT'
    ]

    user = ''

    try:
        while user != cmd[1]:
            user = input(f.GREEN + '-').upper()
        
            for i in cmd:
                if user == cmd[0]:
                    print(f.GREEN + f'\t*{i}')
                elif user == cmd[2]:
                    scan()
                    break
                elif user == cmd[3]:
                    encrypt()
                    break
                elif user != i and user != cmd[1] and user != '':
                    print('error')
                    break

    except KeyboardInterrupt:
        print('\n')
            
    


if __name__ == '__main__':
    main()