# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

def inverse(n):
    res = ''
    if n < 0:
        res += '-'
        n *= -1
    if n < 10:
        return res + f'{n}'
    return res + f'{n % 10}' + inverse(n // 10)


n = int(input('Введите число: '))

print(inverse(n))