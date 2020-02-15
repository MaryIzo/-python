# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/139YjEx24A-HhEx5_GE5mCjyzsIV48FRM/view?usp=sharing

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if a > b:
    if b > c:
        print(b)
    elif c>a :
        print(a)
    else:
        print(c)
else:
    if a > c :
        print(a)
    elif c>b :
        print(b)
    else:
        print (c)