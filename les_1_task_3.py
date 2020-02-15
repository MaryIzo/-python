#По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
# https://drive.google.com/file/d/139YjEx24A-HhEx5_GE5mCjyzsIV48FRM/view?usp=sharing

print('Введите коорд.двух точек')
x1 = float(input('Введите координату x1  '))
y1 = float(input('Введите координату y1  '))
x2 = float(input('Введите координату x2  '))
y2 = float(input('Введите координату y2  '))

if (x1 - x2==0) and (y1- y2 == 0) :
    print('Вы ввели одну и ту же точку')
elif x1 - x2==0 and (y1 - y2!=0):
    print(f'уравнение имеет вид x= {x1}')
else:
    k=(y1-y2)/(x1-x2)
    b=y1-k*x1
    if b<0:
        print(f'уравнение имеет вид y= {k }x - {-b }')
    else:
        print(f'уравнение имеет вид y= {k}x + { b}')




