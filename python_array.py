array = [1,2,5,3,6,8,4]
print(array[:-3])
for i in range(len(array) - 1, 0, -1):
    print(i)
    for j in range(0, i):
        print(j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
# http://www.cnblogs.com/buro79xxd/archive/2011/05/23/2054493.html
