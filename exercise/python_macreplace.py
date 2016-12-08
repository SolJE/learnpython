# -*- coding:utf-8 -*-

import os

#引入telnet模块，通过telnet修改MAC地址
def telnetlogin(host="192.168.169.1",user="root",password="admin"):#设置host,user,password的默认参数方便使用
    import telnetlib
    
    #登陆host
    tn = telnetlib.Telnet(host)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        
    #修改mac地址
    tn.write(b"iwpriv ra0 e2p 4=%s\n" % mac_04_28_2E.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 6=%s\n" % mac_06.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 8=%s\n" % mac_08.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 28=%s\n" % mac_04_28_2E.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 2A=%s\n" % mac_2A.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 2C=%s\n" % mac_2C.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 2E=%s\n" % mac_04_28_2E.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 30=%s\n" % mac_30.encode('ascii'))
    tn.write(b"iwpriv ra0 e2p 32=%s\n" % mac_32.encode('ascii'))
    
    #重启并退出
    tn.write(b"ralink_init clear 2860\n")
    tn.write(b"reboot\n")
    tn.write(b"exit\n")
    #print(tn.read_all().decode('ascii'))
    print("\n\t修改成功！！！ :)\n")

def macaddress(mac):
    import re
    
    #将输入的MAC地址转为大写，并通过正则表达式按每两个字符分割为一个list
    mac = mac.upper().replace(' ','')
    if len(mac) == 12:
        maclist = re.findall(r'.{2}',mac)
        
        #取MAC地址后8位用于计算LAN口及WAN口地址，并将所得字符串分割为List
        mac_pre = int(mac[:4],base=16)
        mac_suffix = mac[-8:]
        mac_lan = hex((int(mac_suffix,base=16)+2))[-8:].replace("x","0").upper()
        mac_lan_list = re.findall(r'.{2}',mac_lan)
        mac_wan = hex((int(mac_suffix,base=16)+3))[-8:].replace("x","0").upper()
        mac_wan_list = re.findall(r'.{2}',mac_wan)
        
        #确定MAC地址每一位的值
        mac_04_28_2E = maclist[1]+maclist[0]
        mac_06 = maclist[3]+maclist[2]
        mac_08 = maclist[5]+maclist[4]
        mac_2A = mac_lan_list[1]+mac_lan_list[0]
        mac_2C = mac_lan_list[3]+mac_lan_list[2]
        mac_30 = mac_wan_list[1]+mac_wan_list[0]
        mac_32 = mac_wan_list[3]+mac_wan_list[2]
        return mac_04_28_2E,mac_06,mac_08,mac_2A,mac_2C,mac_30,mac_32
        
    else:
        print("\n\tMAC地址位数不对")

#输入需修改的MAC地址    
while True:
    mac = input("请输MAC地址:>")
    try:
        mac_04_28_2E,mac_06,mac_08,mac_2A,mac_2C,mac_30,mac_32 = macaddress(mac)

    #判断脚本所在目录是否存在config.txt文件

        if os.path.exists("config.txt") == False:
            try:
                telnetlogin()
            except Exception as e:
                print ("\n\t",Exception,":",e)
                print("\n\t操作失败 :(\n")
        else:
            configlist = []
            config_txt = open("config.txt","r")
            for config in config_txt.readlines():
                config = config.strip().replace("//n","")
                configlist.append(config)
            print (configlist)
            
            try:
                host,user,password = configlist
                telnetlogin(host,user,password)
            except Exception as e:
                print ("\n\t",Exception,":",e)
                print("\n\t操作失败:(\n")
                
    except Exception as e:
        #print (Exception,":",e)
        print("\n\tMAC地址格式错误 :(\n")