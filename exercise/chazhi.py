LIST = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
SET = set(LIST)
count = 0
a = 45
f = 27
j = 5
for b in SET:
    if b > 27:
        print(b)
        for c in SET:
            if c > 27:
                print(c)
                print(count)
                for d in SET:
                    if d >27:
                        #print(d)
                        for e in SET:
                            if e >27:
                                #print(e)
                                for g in SET:
                                    if g < 27:
                                        #print(g)
                                        for h in SET:
                                            if h < 27:
                                                #print(h)
                                                for i in SET:
                                                    if i < 27:
                                                        #print(i)
                                                        if a-b > b-c and b-c > c-d and c-d > d-e and d-e > e-f and e-f > f-g and f-g > g-i and g-i > i-j:
                                                            print("%s\\%s\\%s\\%s\\%s\\%s\\%s\\%s\\%s\\%s" % (a,b,c,d,e,f,g,h,i,j))
                                                            exit
                                                        else: 
                                                            #print("%s//" % count)
                                                            count = count + 1