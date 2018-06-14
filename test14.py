# -*- coding: utf-8 -*-
# 切片
# 教材：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000
def trim(s):
    while True:
        if len(s) == 0:
            return s
        else:
            if s[0] == ' ':
                s = s[1:]
                continue
            elif s[-1] == ' ':
                s = s[:-1]
                continue
            else:
                return s
    

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')