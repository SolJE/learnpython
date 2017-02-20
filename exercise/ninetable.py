# -*- coding:utf-8 -*-
"""
    99乘法表
"""
LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for a in LIST:
    for i in LIST:
        if LIST[i-1] <= a:
            print("%sx%s = %d  " %(LIST[i-1], a, a*LIST[i-1]), end="")
        else:
            print("\n")
            break
