#Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://drive.google.com/file/d/1D2dM98z3RENQ9f5FG9weOJC0FIrEEE5M/view?usp=sharing

def recursion(n):
    if n==1:
        return 1
    else:
        return n+ recursion(n-1)


n = int(input('Введите количество элементов '))

if recursion(n)==n*(n+1)/2:
    print('Равенство выполняется')
else:
    print('Такого не может быть')