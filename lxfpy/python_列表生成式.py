#列表生成式
#通过一行生成[1x1, 2x2, 3x3, ..., 10x10]
[x*x for x in range(1,11)] #把要生成的元素x*x写到前面，后面跟for循环。
#在循环后还可以跟if判断
[x*x for x in range(1,11) if x % 2 == 0]
#还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ'] #较少用于三层及以上循环。为什么？
import os
[d for d in os.listdir()]
[d for d in os.listdir('.')]
os.listdir(os.getcwd())
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
    for k, v in d.items():
        print(k, '=', v)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
