#定义函数，空函数；参数检查
#定义函数使用def语句，随后依次写出函数名，括号，在括号中定义参数，后面以“：”结尾
#后面的函数体要写在缩进块中
#函数的返回值通过return返回，return后面不用加“：”
#若不需函数返回数据，则可以只写return，此时会返回“None”，若不写return，也会返回“None”

def my_abs(x):
    if x >=0:
        return x
    if x < 0:
        return -x
        
        
#可以通过from [script] import [def] 的方式对其它文件中的函数作引用
#空函数：在函数体中只写pass，则函数会直接跳过，不会报错。以后可以在函数体中再写语句
#pass也可以用在其它语句中

def nop()
    pass
    
if age >= 18:
    pass
    
#python内置函数通常都会有参数检查，但自定义函数python解释器很多时候无法帮助检查
#可以使用内置函数isinstance()对参数类型做检查

def my_abs_2(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    if x < 0:
        return -x
        
        
#一个函数可以返回多个值
#python 返回的多值其实是一个tuple
#tuple按位置赋值给对应的变量


import math

def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
    
    x,y = move(100,100,60, math.pi / 6)
    print (x,y)
    
