#Space Complexity:- O(1)
def sum(n):
    return n*(n+1)//2

sum(2)
sum(4)


#Space Complexity:- O(n)
def arraysum(a):
    sum=0
    for i in a:
        sum = sum+i

    return sum

a = [12, 3, 4, 15]
arraysum(a)

def summ(n):
    if(n<=0):
        return 0
    return n + summ(n-1)

summ(4)
summ(8)