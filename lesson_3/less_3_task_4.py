# Определить, какое число в массиве встречается чаще всего.

import random


def quicksort(array, left, right):
    if left >= right:
        return
    i, j = left, right
    rand_item = array[random.randint(left, right)]

    while i <= j:
        while array[i] < rand_item:
            i += 1
        while array[j] > rand_item:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quicksort(array, left, j)
    quicksort(array, i, right)


def max_count_item(array):
    res = array[0]
    curr_item_counter = 1
    counter = 1

    for i, item in enumerate(array[1:]):
        if item == array[i]:
            curr_item_counter += 1
        if item > array[i] or i == len(array) - 2:
            if curr_item_counter > counter:
                res = array[i]
                counter = curr_item_counter
            curr_item_counter = 1
    return res


arr = [random.randint(-10, 10) for _ in range(100)]
print(arr)

quicksort(arr, 0, len(arr) - 1)

print(f'Число {max_count_item(arr)} встречается в массиве чаще всего')
