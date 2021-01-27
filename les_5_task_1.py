# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
import collections

Company = collections.Counter()
N = int(input('Сколько предприятий? '))
All_sum = 0
for i in range(N):
    Name = input('Введите наименование предприятия ')
    print('Прибыль за 4 квартала по очереди')
    sum_profit = 0
    for i in range(4):
        sum_profit = sum_profit + int(input())
    Company[Name] = sum_profit
    All_sum = All_sum + sum_profit

All_sum = All_sum / N

print('Средняя прибыль ', All_sum)
print(Company)

higher = collections.deque()
lower = collections.deque()

for element in Company:
    if Company[element] > All_sum:
        higher.append(element)
    else:
        lower.append(element)

print(f'Прибыль выше среднего: {list(higher)} ')
print(f'Прибыль ниже среднего: {list(lower)} ')
