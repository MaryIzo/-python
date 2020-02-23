# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM_a = 10
MAX_ITEM_all = 100

a = [k for k in range (2, MAX_ITEM_a)]
count = [0 for k in range (2, MAX_ITEM_a)]

for number in a:
    count[number - 2] = (MAX_ITEM_all-1) // number

print(count)

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Другой способ

count = [0 for k in range (2, MAX_ITEM_a)]

for i in range (2, MAX_ITEM_all):
    for number in a:
        if i % number == 0:
            count[number-2]+=1

print(count)