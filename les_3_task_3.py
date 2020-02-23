# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE) ]

print(array)

if len(array)>1:
    max_el_num = 0
    min_el_num = 0
    for i in range(len(array)):
        if array[max_el_num] < array[i]:
            max_el_num = i
        elif array[min_el_num] > array[i]:
            min_el_num = i

    temp=array[min_el_num]
    array[min_el_num]=array[max_el_num]
    array[max_el_num]=temp

print(array)