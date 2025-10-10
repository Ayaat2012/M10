#Algorithm to find all the prime numbers upto any given limit

def StieveOfEratosthenes(num):
    prime = [True for i in range(0, num+1)]

    p = 2
    while (p * p <= num):

        if (prime[p] == True):

            for i in range(p*p, num+1, p):
                prime[i] = False
        p += 1

    for p in range(2, num+1):
        if prime[p] == True:
            print(p, end=", ")


num = int(input("Enter an integer "))
print("Followings are the prime numbers smaller\nthan or equal to ", num)
StieveOfEratosthenes(num)