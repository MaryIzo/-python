import math
import timeit
import cProfile

def sieve(k):
    #n=100
    n=k*k
    a = [0]* n
    for i in range(n):
        a[i]=i
    a[1]=0
    m=2
    while m<n:
        if a[m]!=0:
            j=m*m
            while j<n :
                a[j]=0
                j=j+m
        m+=1

    b =[]
    for i in a:
        if a[i]!=0:
            b.append(a[i])
    del a

    return b[k-1]

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def prime(k):
    n=k*k
    #n = 15485863
    b=[]
    for i in range(1,n+1):
        if (i==1):
            continue
        isprime=1
        for j in range(2, i-1):
            if (i%j)==0:
                isprime=0
                break
        if (isprime):
            b.append(i)

    return b[k-1]

print(sieve(10))
print(prime(10))

print( timeit.timeit( 'sieve(5)', number = 100, globals= globals() )) #0.0006200000000000025
print( timeit.timeit( 'sieve(10)', number = 100, globals= globals() )) # 0.0023315000000000002
print( timeit.timeit( 'sieve(15)', number = 100, globals= globals() ))  #0.0056154999999999955
print( timeit.timeit( 'sieve(20)', number = 100, globals= globals() ))  #0.014723800000000002
print( timeit.timeit( 'sieve(100)', number = 100, globals= globals() ))  #0.3921017
# Решето Эратосфена имеет сложность О(n log log n)
print()
print( timeit.timeit( 'prime(5)', number = 100, globals= globals() )) #0.002705199999999963
print( timeit.timeit( 'prime(10)', number = 100, globals= globals() ))  #0.015269199999999983
print( timeit.timeit( 'prime(15)', number = 100, globals= globals() ))  #0.08477000000000001
print( timeit.timeit( 'prime(20)', number = 100, globals= globals() ))  #0.12954899999999991
print( timeit.timeit( 'prime(50)', number = 100, globals= globals() ))  #3.2722892

# На больших значениях алгоритм работает очень медленно. Сложность O (n^2).

cProfile.run('sieve(50)')
# 371 function calls in 0.001 seconds

cProfile.run('prime(50)')
# 371 function calls in 0.030 seconds
#  367    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}