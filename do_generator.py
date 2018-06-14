# -*- coding: utf-8 -*-
# 生成器
# 教材： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

#def fib(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        yield b
#        a, b = b, a + b
#        n = n + 1
#    return 'done'
#
#f = fib(10)
#print('fib(10):', f)
#for x in f:
#    print(x)
#
## call generator manually:
#g = fib(5)
#while 1:
#    try:
#        x = next(g)
#        print('g:', x)
#    except StopIteration as e:
#        print('Generator return value:', e.value)
#        break
        

def triangles():
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n += 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')