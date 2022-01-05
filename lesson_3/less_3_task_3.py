# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

arr = [random.randint(-10, 10) for _ in range(20)]
print(arr)
max_item = arr[0]
min_item = arr[0]
max_item_index = 0
min_item_index = 0

for i, item in enumerate(arr):
    if item > max_item:
        max_item = item
        max_item_index = i

    if item < min_item:
        min_item = item
        min_item_index = i

arr[max_item_index], arr[min_item_index] = arr[min_item_index], arr[max_item_index]
print(arr)
