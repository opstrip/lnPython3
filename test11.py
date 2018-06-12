# -*- coding: utf-8 -*-
# 定义函数
# 教程： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000

import math

def quadratic(a, b, c):
    n = b ** 2 - 4 * a * c
    if n < 0:
        print("Error!")
    else:
        return (((math.sqrt(n)-b)/ (a * 2)), ((-math.sqrt(n)-b)/ (a * 2)) )