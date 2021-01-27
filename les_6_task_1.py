# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import collections
import sys
#sys.setrecursionlimit(20000) # на всякий случай

# Так как три варианта решения задачи находятся в одном файле, посчитаем отдельно память для констант
MIN_ITEM = 2
MAX_ITEM_a = 10
MAX_ITEM_all = 100
CONST = sys.getsizeof(MIN_ITEM)+sys.getsizeof(MAX_ITEM_a)+sys.getsizeof(MAX_ITEM_all)
#print(CONST)
# CONST = 84

#Первый вариант запишем в отдельную функцию
# locals() возвращает словарь локальных переменных функции, по которому и можно будет посчитать память
def way1(left, n, right):
    a = [k for k in range(left, n)]
    count = [0 for k in range(left, n)]
    for number in a:
        count[number - 2] = (right - 1) // number
    return locals()

#Второй вариант. Отличаться должен по идее быстродействием и переменной i.
def way2(left, n, right):
    a = [k for k in range(left, n)]
    count = [0 for k in range(left, n)]
    for i in range(left, right):
        for number in a:
            if i % number == 0:
                count[number - 2] += 1
    return locals()

#Третий вариант. Вместо списка кортеж и очередь.
def way3(left, n, right):
    a = tuple(k for k in range(left, n))
    answer = collections.deque()
    for number in a:
        answer.append((right - 1) // number)
    return locals()

# Сохраним словари в отдельные переменные, хотя это не обязательно
x_1 = way1(MIN_ITEM, MAX_ITEM_a, MAX_ITEM_all)
x_2 = way2(MIN_ITEM, MAX_ITEM_a, MAX_ITEM_all)
x_3 = way3(MIN_ITEM, MAX_ITEM_a, MAX_ITEM_all)

# x_4=globals() # Это тоже можно посчитать, но если увеличить стек и тогда не нужны переменные x_1, x_2, x_3, CONST

#Теперь функция для подсчета памяти. Задается значение local_sum = 0 и к нему добавляем уже память на объект
def show(obj, local_sum):
    local_sum = local_sum + sys.getsizeof(obj)
    #print(f'type={type(obj)}, size = {sys.getsizeof(obj)}, {obj}, {local_sum}') # Отдельно для каждого объекта.
    if hasattr(obj,'__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                #Так как функция рекурсивна и возвращает значение суммы объектов, передавать нужно 0.
                # И складывать с уже ранее посчитанным.
                local_sum = local_sum + show(key, 0) + show(value, 0)
        elif not isinstance(obj, str):
            for item in obj:
                local_sum = local_sum + show(item, 0)
    return local_sum

#Версия Питона:
#print (sys.version)
#3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]


print(show(x_1, 0)) # Значение 1500
print(show(x_2, 0)) # Значение 1578
print(show(x_3, 0)) # Значение 1989 # На очередь очень много памяти.
# type=<class 'collections.deque'>, size = 632, deque([49, 33, 24, 19, 16, 14, 12, 11]), 632

# Если это три отдельные программы прибавим CONST
# Ответ ( 1584, 1662, 2073 )

#print(show(x_1, 0) + CONST) # Значение 1584
#print(show(x_2, 0) +CONST) # Значение 1662
#print(show(x_3, 0) +CONST) # Значение 2073