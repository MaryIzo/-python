#Определить, является ли год,
# который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/139YjEx24A-HhEx5_GE5mCjyzsIV48FRM/view?usp=sharing

X=int(input('Введите год '))

if X % 4 != 0 or (X % 100 == 0 and X % 400 != 0  ):
    print('Этот год обычный')
else:
    print('Этот год високосный')