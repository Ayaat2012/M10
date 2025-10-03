#Program to find factors of user input

#Taking input from user
number = int(input("Enter your desired number to find its factors: "))

#Goes from 1 to number and checks if I divide the number. If yes, then it's a factor
def print_factors(number):
    print("The factors of ", number, "are: ")
    for i in range(1, number+1):
        if number % i == 0:
            print(i)

#Calling our function
print_factors(number)