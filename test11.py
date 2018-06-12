# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    n = b ** 2 - 4 * a * c
    if n < 0:
        print("Error!")
    else:
        return (((math.sqrt(n)-b)/ (a * 2)), ((-math.sqrt(n)-b)/ (a * 2)) )