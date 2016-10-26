#list的定义
names = ['Michael','Bob','Tracy']
scores = [95,75,85]

#dict的定义
d = {'Michael': 95,'Bob': 75,'Tracy': 85}

#为dict添加key和值
d['Adam'] = 67

#使用in查询key是否在dict内，会返回False或True
print ('Thomas' in d)

#使用get来获取key，若key不在dict内则反回NONE或指定值
d.get('Thomas','NO')

#使用pop来删除dict中的key，其值会一并删除
d.pop('Bob')

d['lily'] = ""
d['lily'] = 'first'

#输出dict d和dict中lily的值
print (d)
print (d['lily'])

l = [1,2,3,4,5]

#将l的元素添加为set的key
s = set(l)
print (s)

#通过add/remove在set中添加/删除key
s.add(9)
s.remove(l[0])
print (s)

#使用def定义一个函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print (my_abs(-15))
