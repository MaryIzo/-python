#Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1D2dM98z3RENQ9f5FG9weOJC0FIrEEE5M/view?usp=sharing

x = int(input('Введите число '))
ch=0
n_ch=0

while x*10 // 10 != 0:
    n = x %10
    if n%2==0:
        ch=ch+1
    else:
        n_ch=n_ch+1
    x=x//10

print(f' число четных {ch} нечетных  {n_ch}')