# -*- coding: utf-8 -*-
# 递归函数
# 教材：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000
# 算法讲解：https://blog.csdn.net/hikobe8/article/details/50479669
# 运算过程：![思维导图](./Hanoi.jpg)

def move(n, a, b, c):
    if(n == 1):
        print(a,"->",c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

'''
def move(n, a, b, c):
    if(n == 1):
        print(a,"->",c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
'''
# 测试
move(3, "a", "b", "c")
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C