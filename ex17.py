from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

indata = open(from_file).read()
print (indata)
#使用len()查看文本的长度,但这个长度在有换行或中文时怎么计算？
print ("The input file is %r bytes long" % len(indata))
#exists是判断文件存不存在，返回布尔值。
print ("Does the output fils exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input("?")

open(to_file,'w').write(indata)

print ("Alright, all done")
#使用分号可以将多行语句写在一行
open(from_file).close();open(to_file).close()