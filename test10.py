# -*- coding: utf-8 -*-
# 条件判断
# 教材： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000
# 利用BMI指数判断是否肥胖的方法
# BMI计算方法：BMI = 体重(公斤) / 身高(米)的平方

height = 1.75
weight = 80.5
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("您的 BMI 值为%.2f，体重过轻" % bmi)
elif bmi < 25:
    print("您的 BMI 值为%.2f，体重正常" % bmi)
elif bmi < 28:
    print("您的 BMI 值为%.2f，过重" % bmi)
elif bmi < 32:
    print("您的 BMI 值为%.2f，肥胖" % bmi)
else:
    print("您的 BMI 值为%.2f，严重肥胖" % bmi)