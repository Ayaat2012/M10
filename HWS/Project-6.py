#Finding all prime numbers having two digits

def prime(num):
    
    #Checking if a number is prime.
    
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("All two-digit prime numbers:")
for number in range(10, 100):
    if prime(number):
        print(number)