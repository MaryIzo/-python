#Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

count = [1 for i in range(SIZE)]

print(array)

max_count=1

for i in range(len(array)):
    for k in range (i+1, len(array)):
        if array[i]==array[k]:
            count[i]=count[i]+1

    if count[i]>max_count:
        max_count=count[i]

#print(count)

if max_count==1:
    print('все числа встречаются по одноу разу')
else:
    for i in range(len(array)):
        if count[i] == max_count:
            print(f' частота {array[i]} равна {count[i]}')


