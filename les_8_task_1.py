#Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
#

import hashlib

def StrtoList(st):
    result = []
    j = len(st) - 1
    left = 0
    right = j
    while j > 0:
        if len(st[left:right]) == j:
            result.append(st[left:right])
            left += 1
            right += 1
        else:
            left = 0
            j = j - 1
            right = j
    return result

def Comparison(x):
    count = len(x)
    for i in range(len(x)):
        ha = hashlib.sha1(x[i].encode('utf-8')).hexdigest()
        for j in range(i+1, len(x)):
            hb = hashlib.sha1(x[j].encode('utf-8')).hexdigest()
            if ha == hb:
                count -= 1
    return count


st_ = input('Введите строку: ')

print(StrtoList(st_))

print(Comparison(StrtoList(st_)))
