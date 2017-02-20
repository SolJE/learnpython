# -*- coding:utf-8 -*-

import os
import time
#import getpass
#import sys

#引入telnet模块，通过telnet修改MAC地址
def telnetlogin(host="192.168.169.1", user="root", password="admin"):#设置host,user,password的默认参数方便使用
    import telnetlib

    #登陆host
    TN = telnetlib.Telnet(host)
    try:
        TN.read_until(b"login: ")
        TN.write(user.encode('ascii') + b"\n")
        if password:
            TN.read_until(b"Password: ")
            TN.write(password.encode('ascii') + b"\n")

            #修改mac地址
            TN.write(b"iwpriv ra0 e2p 4=%s\n" % MAC_04_28_2E.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 6=%s\n" % MAC_06.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 8=%s\n" % MAC_08.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 28=%s\n" % MAC_04_28_2E.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 2A=%s\n" % MAC_2A.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 2C=%s\n" % MAC_2C.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 2E=%s\n" % MAC_04_28_2E.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 30=%s\n" % MAC_30.encode('ascii'))
            TN.write(b"iwpriv ra0 e2p 32=%s\n" % MAC_32.encode('ascii'))

            #重启并退出
            TN.write(b"ralink_init clear 2860\n")
            TN.write(b"reboot\n")
            TN.write(b"exit\n")
            print(TN.read_all().decode('ascii'))
            print("\n\t修改成功！！！ (^O^)\n")
    except Exception as e:
        print("\n\t", Exception, ":", e)
        print("\n\t写入失败 -_-b\n")

def macaddress(mac):
    import re

    #将输入的MAC地址转为大写，并通过正则表达式按每两个字符分割为一个list
    mac = mac.upper().replace(' ', '')
    if len(mac) == 12:
        maclist = re.findall(r'.{2}', mac)

        #取MAC地址后8位用于计算LAN口及WAN口地址，并将所得字符串分割为List
        mac_pre = int(mac[:6], base=16)
        mac_suffix = int(mac[-6:], 16)
        if mac_suffix <= 16777212:
            mac_lan = hex(mac_suffix + 2)[-6:].replace("x", "0").upper()
            while len(mac_lan) < 6:
                mac_lan = "0"+ mac_lan
            mac_lan_list = re.findall(r'.{2}', mac_lan)
            print(mac[:6],mac_lan_list)
            mac_wan = hex(mac_suffix + 3)[-6:].replace("x", "0").upper()
            while len(mac_wan) < 6:
                mac_wan = "0"+ mac_wan
            mac_wan_list = re.findall(r'.{2}', mac_wan)
            print(mac[:6], mac_wan_list)

            #确定MAC地址每一位的值
            MAC_04_28_2E = maclist[1]+maclist[0]
            MAC_06 = maclist[3]+maclist[2]
            MAC_08 = maclist[5]+maclist[4]
            MAC_2A = mac_lan_list[0]+maclist[2]
            MAC_2C = mac_lan_list[2]+mac_lan_list[1]
            MAC_30 = mac_wan_list[0]+maclist[2]
            MAC_32 = mac_wan_list[2]+mac_wan_list[1]
            return MAC_04_28_2E, MAC_06, MAC_08, MAC_2A, MAC_2C, MAC_30, MAC_32
        else:
            print("\n\tMAC已超出可用范围，后六位最大允许FFFFFC")
    else:
        print("\n\tMAC位数错误，总位数应为12位")

#输入需修改的MAC地址
while True:
    mac = input("请输MAC地址:>")
    start = time.time()
    try:
        MAC_04_28_2E, MAC_06, MAC_08, MAC_2A, MAC_2C, MAC_30, MAC_32 = macaddress(mac)

    #判断脚本所在目录是否存在config.txt文件

        if os.path.exists("config.txt") == False:
            print("使用默认参数连接")
            try:
                telnetlogin()
            except Exception as e:
                print("\n\t", Exception, ":", e)
                print("\n\t操作失败 -_-b\n")
        else:
            CONFIGLIST = []
            CONFIG_TXT = open("config.txt", "r")
            for config in CONFIG_TXT.readlines():
                config = config.strip().replace("//n", "")
                CONFIGLIST.append(config)
            print("自定义参数连接：", CONFIGLIST)
            CONFIG_TXT.close()

            try:
                host, user, password = CONFIGLIST
                telnetlogin(host, user, password)
            except Exception as e:
                #exce = str(Exception,":",e)
                #print (exce)
                print("\n\t", Exception, ":", e)
                print("\n\t操作失败 -_-b\n")

    except Exception as e:
        print("\n\t", Exception, ":", e)
        print("\n\t操作失败 -_-b\n")
    end = time.time()
    print("\t%.2f秒" % (end-start))
