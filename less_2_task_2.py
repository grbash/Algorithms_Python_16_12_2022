# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def odd_even_count(n):
    odd = 0
    even = 0
    temp_num = n
    while n > 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return f'В {temp_num} {even} четных и {odd} нечетных цифр'


n = int(input('Введите число: '))
print(odd_even_count(n))
