# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


def bubble_sort(arr):
    j = 0
    while j < len(arr):
        flag = 0
        for i in range(len(arr) - j - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1
        if flag == 0:
            break
    j += 1


SIZE = 200
MIN_ITEM = -100
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)
bubble_sort(array)
print(array)
