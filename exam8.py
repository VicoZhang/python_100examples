"""
输出 9*9 乘法口诀表。
"""
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("{}*{}={}".format(j, i, i * j), end=' ')
    print()
