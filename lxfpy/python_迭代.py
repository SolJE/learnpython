#所有可迭代的对象都可以使用for...in...的方法来迭代
#可以使用collections的模块的lterable类型来判断
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代
#enumerate函数可以把一个List变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
