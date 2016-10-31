def f1(arg):
    print ("f1") #实际打印“f1”
    rl = arg() #此句打印f2
    print(rl) #实际打印"f2r"
    return rl + "f1"
    
@f1
def f2(arg = ""):
    print ("f2") #实际打印“f2”
    return arg + "f2r"

print ("start") #实际打印“start”
print (f2) #实际打印“f2rf1”
#print f2("1") 出错
#print f1(None)

#实际执行和打印顺序为
#第2行：f1
#第3行：f2
#第4行：f2r
#第12行：start
#第13行：f2rf1
#在def f2前@f1 执行的是f2=f1(f2())