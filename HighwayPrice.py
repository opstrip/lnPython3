#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 根据 "四舍五入 → 整数 → 舍二进八，七作五" 规则计算高速公路里程价格
import os

def rule(a):
    num = a
    if isinstance(num, float):
        num = round(num, 0)
    n = num % 10
    if n <= 2:
        total = num - n
    elif n <= 7:
        total = num - n + 5
    else:
        total = num - n + 10
        
    return total
    

def hwp():
    price = 0.55
    try:
        mileage = round(float(input("请输入里程数单位公里： ")), 0)
    except ValueError:
        print("请输入有效的数字！")
        exit()
        
    print("您已行驶 %d 公里，共需支付 %d 元。" % (mileage, rule(mileage * price) ))
    
hwp()