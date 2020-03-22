# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge(a, left, mid, right):
    result = [0 for k in range(right - left )]

    i1 = 0
    i2 = 0
    while left + i1 < mid and mid + i2 < right:
        if a[left + i1] < a[mid + i2]:
            result[i1 + i2] = a[left + i1]
            i1 += 1
        else:
            result[i1 + i2] = a[mid + i2]
            i2 += 1

    while left + i1 < mid:
        result[i1 + i2] = a[left + i1]
        i1 += 1
    while mid + i2 < right:
        result[i1 + i2] = a[mid + i2]
        i2 += 1

    for i in range(0, i1 + i2):
       a[left + i] = result[i]


def merge_sort(arr, left, right):
    if left + 1 >= right:
        return
    mid = int((left + right) / 2)
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49

array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for i in range(SIZE)]

print(array)
merge_sort(array, 0, len(array))
print(array)
