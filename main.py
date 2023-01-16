from network import Scan,f,ff,os,DDOS


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
            u = input(f.RED + "Do you want to save it :\n1 - yes\n2 - no\n:- ")

            if u.lower() == 'yes':
                s.save(input('enter a file name: '))

            elif u.lower() == 'no':
                print(f.GREEN + 'Goodbye :)')
                
            else:
                print(f.YELLOW + 'unvalid option I think you mean exit')
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

    user = input(f.RED + 'press any key to exit...')
    os.system('clear')

def main():
    print(f.YELLOW + ff('Helper'))
    print(f.YELLOW + 'type list to see the availble commands')

    cmd = [
        'LIST',
        'EXIT',
        'SCAN',
        'DDOS -alpha-'
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
                elif user != i and user != cmd[1] and user != '' and user.isspace() == False:
                    print('error')
                    break

    except KeyboardInterrupt:
        print('\n')
            
    


if __name__ == '__main__':
    main()
    