import getpass
import telnetlib

HOST ="192.168.169.1"
user = "root"
password = "admin"

tn = telnetlib.Telnet(HOST)

mac = input("Input Mac Adress:")

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

mac_suffix = mac[-6:]
mac_lan = hex((int(mac_suffix,base=16)+2))
mac_wan = hex((int(mac_suffix,base=16)+3))


mac_two = re.findall(r'.{2}',mac)#mac_two是一个List
    

tn.write(b"ls\n")
tn.write(b"ps\n")
tn.write(b"iwpriv ra0 e2p 4=9684\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))