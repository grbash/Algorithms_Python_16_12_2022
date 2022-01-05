# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.
import sys


def summ(n):
    if n <= 0:
        print('n введено неверно')
        sys.exit()
    res = 0.0
    for i in range(n):
        res += (- 1) ** i * 1/(2 ** i)
    return res


n = int(input('Введите количество элементов: '))
print(summ(n))

