#Program to find HCF of user input

# Enter 2 numbers
largestNum = int(input("Enter largest number: "))
smallestNum = int(input("Enter smallest number: "))

# Using Euclidean Algorithm
while(smallestNum):
    numStore = smallestNum
    smallestNum = largestNum % smallestNum
    largestNum = numStore

print("HCF is ", largestNum)


'''
LCM(6, 10) = 30

6 - 6, 12, 18, 24, 30, 36, 42...
10 - 10, 20, 30, 40, 50, 60, 70...

formula:-
LCM(a, b) = (a*b)/HCF(a, b)

LCM(6, 10) = 60/2 = 30
'''