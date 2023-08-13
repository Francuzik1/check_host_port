import re
HostSyntax = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
HOST = None
PORT = None


def enter_host():

    global HOST

    HOST = input("HOST: ")
    check_host = re.fullmatch(HostSyntax, HOST)
    if check_host is None:
        print("Host - a sequence of 4 numbers (from 0 to 255) separated by dots.")
        print("Enter a host such as: 0.0.0.0 - 255.255.255.255")
        enter_host()


def enter_port():

    global PORT

    PORT = input("PORT: ")
    if PORT.isnumeric() is False:
        print("Port is a number from 1 to 65535")
        enter_port()

    PORT = int(PORT)
    if PORT > 65535:
        print("Port is a number from 1 to 65535")
        enter_port()


enter_host()
enter_port()
print(HOST, PORT)
