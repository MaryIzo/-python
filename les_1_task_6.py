#Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.
# https://drive.google.com/file/d/139YjEx24A-HhEx5_GE5mCjyzsIV48FRM/view?usp=sharing

X=int(input('Введите номер буквы в алфавите: '))

if X<1 or X>26:
    print('ошибка ввода номера')
else:
    X=X+96
    print(chr(X))