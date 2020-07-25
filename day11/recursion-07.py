'''
Print Multiplication Table of n using recursion

f(n, m)

3 = 30 27 24 21 18 15 12 9 6 3
3 X 1 = 3
3 X 2 = 6
....
3 X 10 = 30
3 X 9 = 30 - 3
3 X 8 = 30 - 3 - 3

f(n, 20) = n*20
f(n, m) =
'''


def multi(n, start=1, end=20):
    if start == end:
        print(n*start)
        return
    else:
        print(n*start, end=" ")
        return multi(n, start+1, end)


multi(5)
