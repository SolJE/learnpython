from sys import argv

script,filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input ("?")

print ("Opening the file...")
target = open(filename,'w') #此处要注意允许写入
#target = open(filename)

print ("Truncating the file. Goodbye!")
target.truncate() #此处删除打开的文件的内容

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print ("I'm going write these to the file.")

target.write('%s\n%s\n%s\n' % (line1,line2,line3))
#写入之前输入的文本
#target.write("\n") #加入换行
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print ("And finally, we close it.")
target.close() #保存并关闭文件