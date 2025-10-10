#Program to find whether user input is prime number or not
from math import sqrt

num = int(input("Enter your desired number: "))
print("\n")

# If entered number is greater than 1
if num > 1:

    #check if number is divisible by 2 to sqrt(number)
    for i in range(2, int(sqrt(num)) + 1):

        #if divisible by any of those numbers, entered number is not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")  