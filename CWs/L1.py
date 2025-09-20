import time

#Most efficient function- requires 1 iterations irrespective of the value of n
def fun1(n):
    return n*(n+1)/2

#Requires order of n number iterations
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#Least efficient function- requires order of n square number of iterations
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i, i+1):
            sum += i
    return sum
        
n = 100
print(fun1(n))
print(fun2(n))
print(fun3(n))