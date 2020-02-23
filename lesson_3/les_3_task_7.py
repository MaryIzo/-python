# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE) ]

print(array)


min_1 = array[0]
min_2 = array[1]
#считаем, что min_1 < min_2
for i in range(1, len(array)):
    if array[i]< min_1:
        min_2 = min_1
        min_1=array[i]
    elif array[i] < min_2:
        min_2=array[i]

print(f' min_1 = {min_1} <= min_ 2 = {min_2}')

