# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
# значения.

import random

arr = [random.randint(-10, 10) for _ in range(30)]
print(arr)
max_neg_item = arr[0]
max_neg_item_index = 0

for i, item in enumerate(arr):
    if item < 0 and max_neg_item > 0:
        max_neg_item = item
    elif 0 > item > max_neg_item:
        max_neg_item = item
        max_neg_item_index = i

if max_neg_item >= 0:
    print('Все элементы массива больше 0')
else:
    print(f'Максимальный отрицательный элемент массива имеет индекс {max_neg_item_index} и равен {max_neg_item}')
