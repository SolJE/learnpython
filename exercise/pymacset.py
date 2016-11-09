# -*- coding:utf-8 -*-
import os
import sys
import glob
#from sys import argv
#import pdb
import time


#获取本时区当前系统时间，并格式化
def GetNowTime():
    return time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
#对MAC地址做自我对比，检查是否有格式错误和重复值
def repeat_mac_now(oldlist):
    mac_now_set = set(oldlist)
    for mac_now in mac_now_set:
        if len(mac_now) != 12:
            print("""
            该文件中：
            \t[%s]
            格式错误
            """ % mac_now)
            input("按回车结束程序")
            exit()

    if len(oldlist) != len(mac_now_set):
        print("""
        该文件中有 %s 个MAC地址重复
        """ % (len(oldlist)-len(mac_now_set)))
        input("按回车结束程序")
        exit()

    return mac_now_set

#将MAC地址与MAC统计表做对比，看是否有重复
def repeat_mac_total(selfset,totallist):
    totallist_set = set(totallist)
    repeat_count = len(selfset & totallist_set)
    if repeat_count !=0:
        print("""
        与 \033[;31m 之前的出货 \033[0m  有 %s 个MAC 重复
        """ % repeat_count)
        input("按回车结束程序")
        exit()

    return selfset


#打印本程序所以目录
#查找程序所在目录有没有Result目录，若没有则新建一个用于存放对比结果

#print("""
#本程序所在目录：%s
#""" % os.path.abspath(argv[0]))

this_path=os.getcwd()
#listfile = os.listdir(this_path)
listfile = glob.glob("*.txt")
if len(listfile) == 0:
    print("好像这里没有文本文件")
    input("按回车结束")
    exit()
print ("""
以下是文件列表：
""" )
for index,item in enumerate(listfile):
    print ("""
    %s    %s
    """ % (index,item))
#file_list= listfile.split()
if os.path.isdir("Result") == False:
    os.mkdir(r'%s\\Result' % this_path)

#判断是否存在本次扫描记录的testmac.txt
#若存在则分别打开testmac.txt和total.txt文件，并分别导入数组list_mac_now和list_mac_total
#if os.path.isfile("testmac.txt") == True:
user_select = input("请输入要对比的文件序号并确定：")
while user_select.isdigit() != True or int(user_select) <0 or int(user_select) >=len(listfile):
    print("\n写你看到的序号好吗？\n")
    user_select=input(">")
#while int(user_select) <0 or int(user_select) >=len(listfile) :
    #print("\n请输入你看到的序号，别写些没用的！\n")
    #user_select=int(input("请重新输入:"))
    #exit()

start=time.time()
mac_txt=open(listfile[int(user_select)],encoding = "utf-8")
#else:
    #print("\n请将扫描所得的MAC地址文本文件命名为testmac.txt后，与本程序放入同一目录下\n")
    #input("按回车结束程序")
    #exit()
total_txt_re = open('%s\\Result\\total.txt' % this_path,'a')
total_txt = open('%s\\Result\\total.txt' % this_path,'r')
list_mac_now = mac_txt.read().replace(' ','').upper().split()
list_mac_total=total_txt.read().replace(' ','').upper().split()

newlist=repeat_mac_now(list_mac_now)
#print("%s OH,YES" % newlist)
no_repeat_list=repeat_mac_total(newlist,list_mac_total)
#print("%s OH,YES TOO" % no_repeat_list)

#将本次对比后无语的MAC写入一份以时间命名的文件备份，并将其追加写入MAC地址统计表total.txt中
new_txt=open('%s\\Result\\%s.txt' % (this_path,GetNowTime()) ,'a')
for mac in no_repeat_list:
    new_txt.write("%s\n" % mac)
    total_txt_re.write("%s\n" % mac)

new_txt.close
total_txt.close
total_txt_re.close

end=time.time()
run_time=end-start
print("""
    本次运行完成\n
    未发现MAC地址重复\n
    用时：%f秒
    """ % run_time)

input("按回车结束程序")
exit()
