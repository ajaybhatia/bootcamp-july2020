'''
Every iterative problem which have a base condition can be solved using recusion but not vice-versa

10 = 1 + 2 + 3 + 4 ... + 10
10 = 10 + sum of all natural numbers till 9

f(1) = 1,          for all n, where n is natural number and 1
f(n) = n + f(n-1), otherwise
'''


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


print(sum(2))
