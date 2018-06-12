﻿# -*- coding: utf-8 -*-

def product(x, *y):
    if len((y)) == 0:
        return x
    else:
        n = x
        for z in y:
            n *= z
        return n
        
'''
def product(*args):
    if len((args)) == 0:
        raise TypeError
    elif len((args)) == 1:
        return args[0]
    else:
        n = 1
        for x in args:
            n *= x
        return n
'''

# 测试
#print('product() =', product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError as e:
        print('测试成功!')
        print(e)
    except Exception as e:
        print(e)
