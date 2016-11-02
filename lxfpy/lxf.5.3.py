#函数的参数

#python除正常定义必选参数外，还可以使用默认参数、可变参数和关键字参数

#位置参数

def power(x)
    return x*x
    
#默认参数
#默认参数可以在该位置无参数输入时，使用默认的参数
#默认参数需在必选参数后面
#当函数有多个参数时，把变化大的参数放在前面，变化小的参数放在后面，变化小的参数可以作为默认参数

def enroll(name,gender):
    print("name:",name)
    print("gender:",gender)

def enroll2(name,gender,age = 6,city = "Beijing"):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)
    
enroll(sarah,F)
#默认参数可以不按顺序提供，当不按顺序提供时，需要把参数名写上
enroll(Bob,M,7)
enroll(Adam,M,city="Tianjin")

#默认参数不要直接使用list，若要使用需要在内部对list做初始化
#在编写程序时，如果可以设计一个不变对象，尽量设计成不变对象，多任务环境下同时读取对象不需要加锁。
def add_end(L = None)
    if L if None
        L = []
    L.append("END")
    return
    
#可变参数
#可以用list或tuple组装成一个参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc([1,2,3])
calc((1,3,5,7))    
#利用可变参数定义函数
#可变参数实质为多个参数在调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2)
calc()
#可以在list或tuple前加上一个*号将其转换为可变参数
num = [1,2,3]
calc(*num)

#关键字参数
#
