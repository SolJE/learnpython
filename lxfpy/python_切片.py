L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#切片
#使用L[0:3]表示从索引0开始取值，直到索引3为止，不含索引3。
#若从索引0开始，还可以简写为L[:3]
print(L[0:3])
#tuple也是一种list，也可以使用切片，其结果仍是tuple
(0,1,2,3,4,5)[:3]
#字符串也同样可以切片
'ABCDEFG'[::2]
