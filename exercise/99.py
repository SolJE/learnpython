n=[1,2,3,4,5,6,7,8,9];
for a in n:
    for i in n:
        if n[i-1] <= a:
            print ('%sx%s = %d  ' % (n[i-1],a,a*n[i-1]),end="")
        else: print("\n");break