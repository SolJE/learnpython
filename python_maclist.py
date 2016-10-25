# -*- coding:utf-8 -*-

#

import os
#from sys import argv
#import pdb
import time


#获取本时区当前系统时间，并格式化
def GetNowTime():
    return time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
#对MAC地址做自我对比，检查是否有格式错误和重复值
def repeat_mac_now(oldlist):
    index_n=0
    newlist=[]
    while index_n < len(oldlist):
        #print("~^~^",end = "")
        if len(oldlist[index_n]) != 12:
            print("""
            [第%s行]：[%s] 格式错误
            """ % (index_n+1,oldlist[index_n]))
            input("按回车结束程序")
            exit()

        elif oldlist[index_n] in newlist:
            print("""
            文件中中的MAC地址重复:
            [第%s行]：[%s]
            """ % (index_n+1,oldlist[index_n]))
            input("按回车结束程序")
            exit()

        else:
            newlist.append(oldlist[index_n])
        index_n=index_n+1

    if len(oldlist) == len(newlist):
        return newlist

#将MAC地址与MAC统计表做对比，看是否有重复
def repeat_mac_total(selflist,totallist):
    for everymac in selflist:
        #print("[^*^]",end = "")
        if everymac in totallist:
            print("""
            此MAC地址与之前出货重复：
            [%s]
            """ % everymac)
            input("按回车结束程序")
            exit()
    return selflist

start=time.time()

#打印本程序所以目录
#查找程序所在目录有没有Rusut目录，若没有则新建一个用于存放对比结果

#print("""
#本程序所在目录：%s
#""" % os.path.abspath(argv[0]))

rusult_path=os.getcwd()
if os.path.isdir("Rusut") == False:
    os.mkdir(r'%s\\Rusut' % rusult_path)


#判断是否存在本次扫描记录的testmac.txt
#若存在则分别打开testmac.txt和total.txt文件，并分别导入数组list_mac_now和list_mac_total
if os.path.isfile("testmac.txt") == True:
    mac_txt=open("testmac.txt")
else:
    print("\n请将扫描所得的MAC地址文本文件命名为testmac.txt后，与本程序放入同一目录下\n")
    input("按回车结束程序")
    exit()
total_txt_re = open('%s\\Rusut\\total.txt' % rusult_path,'a')
total_txt = open('%s\\Rusut\\total.txt' % rusult_path,'r')
list_mac_now = mac_txt.read().replace(' ','').split()
list_mac_total=total_txt.read().replace(' ','').split()

newlist=repeat_mac_now(list_mac_now)
no_repeat_list=repeat_mac_total(newlist,list_mac_total)

#将本次对比后无语的MAC写入一份以时间命名的文件备份，并将其追加写入MAC地址统计表中
new_txt=open('%s\\Rusut\\%s.txt' % (rusult_path,GetNowTime()) ,'a')
new_txt.write("%s\n" % no_repeat_list)
for mac in no_repeat_list:
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
