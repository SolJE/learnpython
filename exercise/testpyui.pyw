from PyQt5 import QtWidgets,uic
import sys
import os
import time

#from testui import Ui_MainWindow


#qtCreatorFile = "testui.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType("testui.ui")


class mywindow(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        #self.macaddress()
        #self.replace()
        #self.telnetlogin()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    def replace(self):
        #mac = myshow.mac_lineEdit.toPlainText()
        mac = myshow.mac_lineEdit.text()
        start = time.time()
        myshow.result_textEdit.setText("正在修改。。。")
        #time.sleep(5)
        try:
            myshow.result_textEdit.setText("正在修改。。。")
            #time.sleep(2)
            mac_04_28_2E,mac_06,mac_08,mac_2A,mac_2C,mac_30,mac_32 =mywindow.macaddress(mac)
        #判断脚本所在目录是否存在config.txt文件

            if os.path.exists("config.txt") == False:
                #print("使用默认参数连接")
                try:
                    mywindow.telnetlogin()
                    myshow.status_lineEdit.setText("333")
                except Exception as e:
                    #print ("\n\t",Exception,":",e)
                    #print("\n\t操作失败 -_-b\n")
                    exce = Exception,":",e
                    exce = str(exce)
                    myshow.result_textEdit.setText(exce)
            else:
                configlist = []
                config_txt = open("config.txt","r")
                for config in config_txt.readlines():
                    config = config.strip().replace("//n","")
                    configlist.append(config)
                #print ("自定义参数连接：",configlist)
                config_txt.close()

                try:
                    #time.sleep(5)
                    host,user,password = configlist

                    #time.sleep(5)
                    mywindow.telnetlogin(host,user,password)
                except Exception as e:
                    #print ("\n\t",Exception,":",e)
                    #print("\n\t操作失败 -_-b\n")
                    exce = Exception,":",e
                    exce = str(exce)
                    myshow.result_textEdit.setText(exce)

        except Exception as e:
            #print ("\n\t",Exception,":",e)
            #print("\n\t操作失败 -_-b\n")
            exce = Exception,":",e
            exce = str(exce)
            myshow.result_textEdit.setText(exce+"\n 请检查MAC地址")
        end = time.time()
        runtime = "\t%.2f秒" % (end-start)
        myshow.runtime_lineEdit.setText(runtime)

    def telnetlogin(host="192.168.169.1",user="root",password="admin"):#设置host,user,password的默认参数方便使用

        import telnetlib
        #登陆host
        myshow.status_lineEdit.setText(";"+";")
        tn = telnetlib.Telnet(host)
        myshow.status_lineEdit.setText(host+";"+user+";"+password)
        #time.sleep(5)
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
        #print("\n\t修改成功！！！ (^O^)\n")

    def macaddress(mac):
        import re

        #将输入的MAC地址转为大写，并通过正则表达式按每两个字符分割为一个list
        mac = mac.upper().replace(' ','')
        if len(mac) == 12:
            maclist = re.findall(r'.{2}',mac)

            #取MAC地址后8位用于计算LAN口及WAN口地址，并将所得字符串分割为List
            mac_pre = int(mac[:6],base=16)
            mac_suffix = int(mac[-6:],16)
            if mac_suffix <= 16777212:
                mac_lan = hex(mac_suffix + 2)[-6:].replace("x","0").upper()
                while len(mac_lan) < 6:
                    mac_lan = "0"+ mac_lan
                mac_lan_list = re.findall(r'.{2}',mac_lan)
                #print(mac[:6],mac_lan_list)
                mac_wan = hex(mac_suffix + 3)[-6:].replace("x","0").upper()
                while len(mac_wan) < 6:
                    mac_wan = "0"+ mac_wan
                mac_wan_list = re.findall(r'.{2}',mac_wan)
                #print(mac[:6],mac_wan_list)

                #确定MAC地址每一位的值
                mac_04_28_2E = maclist[1]+maclist[0]
                mac_06 = maclist[3]+maclist[2]
                mac_08 = maclist[5]+maclist[4]
                mac_2A = mac_lan_list[0]+maclist[2]
                mac_2C = mac_lan_list[2]+mac_lan_list[1]
                mac_30 = mac_wan_list[0]+maclist[2]
                mac_32 = mac_wan_list[2]+mac_wan_list[1]
                return mac_04_28_2E,mac_06,mac_08,mac_2A,mac_2C,mac_30,mac_32
            else:
                #print("\n\tMAC已超出可用范围，后六位最大允许FFFFFC")
                pass
        else:
            #print("\n\tMAC位数错误，总位数应为12位")
            pass


if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()

    myshow.replace_Button.clicked.connect(mywindow.replace)
    myshow.show()
    myshow.result_textEdit.setText("what?")
    myshow.result_textEdit.setText("yes?")
    sys.exit(app.exec_())
