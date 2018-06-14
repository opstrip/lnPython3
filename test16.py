# -*- coding: utf-8 -*-
# 生成器
# 教材： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
# def triangles(n):
    # L = []
    # if n == 1:
        # return [1]
    # elif n == 2:
        # return [1, 1]
    # else:
        # return [1, ]
        
def triangle(n):
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>10:
            break
    return "done"

g=triangle(10)
for i in g:
    print(i)