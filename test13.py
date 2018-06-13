# -*- coding: utf-8 -*-
# Tower of Hanoi
# Three towers A, B, C
# All discs start with A
# Goal: move all discs to C
# Rule:
# 1. Can only move one disc at a time
# 2. Larger disc can never cover up a small disc

def move(n, a, b, c):
    """
    fr: from, tower A
    sp: spare, tower B
    to: to, tower C
    """
    if n == 1:
        # if only one disc in A
        # just move it to C
        print(a, '->', c)
    else:
        # otherwise do recursion
        # move all (n-1) discs except bottom one
        # from A to B
        move(n - 1, a, c, b)
        # move the bottom (1) disc
        # from A to C
        move(1, a, b, c)
        # move the rest (n-1) discs
        # from B to C
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')