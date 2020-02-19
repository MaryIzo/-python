#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1D2dM98z3RENQ9f5FG9weOJC0FIrEEE5M/view?usp=sharing

n = int(input('Введите количество элементов '))

x=1
s=0

for i in range(n):
    s=s+x
    x=-x/2

print(s)