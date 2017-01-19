import telnetlib

HOST = "192.168.169.1"
USER = "root"
PASSWORD = "hebao"
TN = telnetlib.Telnet(HOST)
TN.set_debuglevel(5)
#mac = input("Input Mac Adress:")
try:
    TN.read_until(b"login: ")
    TN.write(USER.encode('ascii') + b"\n")
    if PASSWORD:
        TN.read_until(b"Password: ")
        TN.write(PASSWORD.encode('ascii') + b"\n")
    #if TN.read_some().index("BusyBox") >= 0:
    print("TEST")
    #print(TN.read_some())
    print("TEST")
    TN.write(b"ls\n")
    TN.write(b"ps\n")
    TN.write(b"exit\n")
    print("YES")
    print(TN.read_all().decode('ascii'))
except Exception as e:
    print("NO")