"""
斐波那契数列
"""


def f(n):
    if n == 1:
        out = 1
    elif n == 2:
        out = 1
    else:
        out = f(n - 1) + f(n - 2)
    return out


for i in range(1, 11):
    print(f(i))
