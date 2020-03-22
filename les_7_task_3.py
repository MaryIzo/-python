# Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random


def median(a):
    point = int((len(a) - 1) / 2)
    memory = []
    for i in range(len(a)):
        if a[i] in memory:
            continue
        p = 0 # Количество элементов, меньших данного
        q = 0 # Количество элементов, больших данного
        k = 0 # Количество элементов, равных данному
        for j in range(len(a)):
            if a[j] < a[i]:
                p += 1
            elif a[j] > a[i]:
                q += 1
            elif a[j] == a[i]:
                k += 1
        # Меняем местами p и q, чтобы было удобнее
        if p < q:
            p,q = q, p
        # print(a[i], 'p= ', p, 'q= ', q, 'k= ', k)
        # (p-q == 0) элементов равных медиане нет
        # (p - q - (k - 1) == 0) учитываем завные медиане элементы
        # (k-1) потому что элемент в цикле считает сам себя
        if (k + q <= point) and ((p-q == 0) or (p - q - (k - 1) == 0)):
            return a[i]
        elif k + q > point: # если представить себе отрезое, то равные числа и минимум из больших или меньших выезжает за середину
            return a[i]
        memory.append(a[i])


MIN_ITEM = 0
MAX_ITEM = 10

m = 5
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(size)]
print(array)
#Сортировка массива для проверки
check_array = sorted(array)
print(check_array)
print('median = ', median(array), 'check = ', check_array[m])
