# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
import sys


def formula_check(n):
    if n <= 0:
        print('n введено неверно')
        sys.exit()
    left = 0
    right = n * (n + 1) / 2
    for i in range(n+1):
        left += i
    if left == right:
        return f'Формула верна для {n} элементов'
    return f'Формула не верна для {n} элементов'


print(formula_check(100000))
