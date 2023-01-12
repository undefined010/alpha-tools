from scanner import Scan

def main():
    s = Scan()
    s.scan()
    print(s.get_open_ports())


if __name__ == '__main__':
    main()