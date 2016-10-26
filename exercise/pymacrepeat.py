# -*- coding:utf-8 -*-
import os
import sys
import glob
#from sys import argv
#import pdb
import time
import xlrd


def GetNowTime():
    return time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))


def repeat_mac_now(oldlist):
    repeatlist = []
    mac_now_set = set(oldlist)
    for mac_now in mac_now_set:
        if len(mac_now) != 12:
            print("""
            第一份文件中：
            \t[%s]
            格式错误
            """ % mac_now)
            input("按回车结束程序")
            exit()

    if len(oldlist) != len(mac_now_set):
        print("""
        第一份文件中有 %s 个MAC地址重复
        """ % (len(oldlist)-len(mac_now_set)))
        for mac in oldlist:
            if mac not in repeatlist:
                repeatlist.append(mac)
            else:
                print("\t重复的MAC是：" + mac + "\n")
        input("按回车结束程序")
        exit()

    return oldlist

def repeat_mac_total(oldlist,totallist):
    
    for mac in oldlist:
        if mac in totallist:
            totallist.remove(mac)
    return totallist

this_path=os.getcwd()
#listfile = os.listdir(this_path)
listfile = glob.glob("*.txt")
#listfile = listfile.append(glob.glob("*.xls*"))
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
if os.path.isdir("Rusut") == False:
    os.mkdir(r'%s\\Rusut' % this_path)

#判断是否存在本次扫描记录的testmac.txt
#若存在则分别打开testmac.txt和total.txt文件，并分别导入数组list_mac_now和list_mac_total
#if os.path.isfile("testmac.txt") == True:
user_select = input("请输入需对比的文件序号并确定：")
while user_select.isdigit() != True or int(user_select) <0 or int(user_select) >=len(listfile):
    print("\n写你看到的序号好吗？\n")
    user_select=input(">")
#while int(user_select) <0 or int(user_select) >=len(listfile) :
    #print("\n请输入你看到的序号，别写些没用的！\n")
    #user_select=int(input("请重新输入:"))
    #exit()
user_select_2 = input("请输入基准文件序号并确定：")
while user_select_2.isdigit() != True or int(user_select_2) <0 or int(user_select_2) >=len(listfile):
    print("\n写你看到的序号好吗？\n")
    user_select=input(">")
    
start=time.time()
mac_txt=open(listfile[int(user_select)],encoding = "utf-8")
#else:
    #print("\n请将扫描所得的MAC地址文本文件命名为testmac.txt后，与本程序放入同一目录下\n")
    #input("按回车结束程序")
    #exit()

    
    
#total_txt_re = open('%s\\Rusut\\total.txt' % this_path,'a')
total_txt = open(listfile[int(user_select_2)],encoding = "utf-8")
list_mac_now = mac_txt.read().replace(' ','').split()
list_mac_total=total_txt.read().replace(' ','').split()

newlist=repeat_mac_now(list_mac_now)
#print("%s OH,YES" % newlist)
no_repeat_list=repeat_mac_total(newlist,list_mac_total)
#print("%s OH,YES TOO" % no_repeat_list)

#将本次对比后无语的MAC写入一份以时间命名的文件备份，并将其追加写入MAC地址统计表total.txt中
new_txt=open('%s\\Rusut\\%s.txt' % (this_path,GetNowTime()) ,'a')
for mac in no_repeat_list:
    new_txt.write("%s\n" % mac)

new_txt.close
total_txt.close

end=time.time()
run_time=end-start
print("""
    本次运行完成\n
    请到本程序所在目录的《Rusut》文件夹下查看结果\n
    用时：%f秒
    """ % run_time)

input("按回车结束程序")
exit()

