hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weight = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i) #如不确定list中的元素是什么类型，则需使用%r转换。

elements = []

for i in range(0,5):
    print("Adding %d to the list." % i)
    elements.append(i)

#elements = range(0,5)

for i in elements:
    print("Elements was: %d" % i)
