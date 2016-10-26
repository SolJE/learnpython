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

enroll(Bob,M,7)
enroll(Adam,M,city="Tianjin")
