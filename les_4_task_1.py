#Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

#Задача Урок 2 задание 7
#Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
import timeit
import cProfile

def recursion(n):
    if n==1:
        return 1
    else:
        return n+ recursion(n-1)

print( timeit.timeit( 'recursion(10)', number = 100, globals= globals() )) # 0.00010639999999999955
print( timeit.timeit( 'recursion(25)', number = 100, globals= globals() )) # 0.00026339999999999697
print( timeit.timeit( 'recursion(50)', number = 100, globals= globals() )) # 0.000549899999999999
print( timeit.timeit( 'recursion(75)', number = 100, globals= globals() )) # 0.0008429000000000006
print( timeit.timeit( 'recursion(100)', number = 100, globals= globals() )) # 0.0011403000000000038

cProfile.run('recursion(10)')
#10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:11(recursion)

#  У алгоритма линейная сложность. Рекурсия не замедляет, так как алгоритм несложный, каждое значение считается один раз.

def memorize(n):
    memory = {1: 1 }

    def g(n):
        if n in memory:
            return memory[n]
        memory[n]= n + g(n-1)
        return memory[n]

    return g(n)

print()
print( timeit.timeit( 'memorize(10)', number = 100, globals= globals() )) # 0.00020230000000000248
print( timeit.timeit( 'memorize(25)', number = 100, globals= globals() )) # 0.0005528999999999951
print( timeit.timeit( 'memorize(50)', number = 100, globals= globals() )) # 0.0012490000000000001
print( timeit.timeit( 'memorize(75)', number = 100, globals= globals() )) # 0.001641699999999996
print( timeit.timeit( 'memorize(100)', number = 100, globals= globals() )) # 0.004630800000000004

cProfile.run('memorize(10)')
# 10/1    0.000    0.000    0.000    0.000 les_4_task_1.py:29(g)

# Алгоритм работает медленнее, чем первый, но все равно линейный.

def cycle(n):
    sum=0
    for i in range(1, n+1):
        sum=sum + i
    return sum

print()
print( timeit.timeit( 'cycle(10)', number = 100, globals= globals() )) # 6.88000000000008e-05
print( timeit.timeit( 'cycle(25)', number = 100, globals= globals() )) # 0.00010589999999999905
print( timeit.timeit( 'cycle(50)', number = 100, globals= globals() )) # 0.00048789999999999945
print( timeit.timeit( 'cycle(75)', number = 100, globals= globals() )) # 0.00029610000000000053
print( timeit.timeit( 'cycle(100)', number = 100, globals= globals() )) # 0.0008428000000000047

cProfile.run('cycle(10)')

# Алгоритм линейный. Но получается, что быстрее, чем первый и второй.

#print (recursion(100))
#print(memorize(100))
#print(cycle(100))

