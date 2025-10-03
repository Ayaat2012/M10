def my_function1(n):
    if(n>0):
        return
    for i in range(0, n+1):
        print("Codingal")
    my_function1(n//2)
    my_function1(n//3)

def my_function2(n):
    if(n<=1):
        return
    print("Codingal")
    my_function2(n-1)