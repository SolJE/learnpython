# -*- coding:utf-8 -*-
"""
    99乘法表单循环实现
"""
X = 0
Y = 1
while Y <= 9:
    X = X+1
    print("%sx%s=%d " %(X, Y, X*Y), end="")
    if X == Y:
        X = 0
        Y = Y+1
        print("\n")
