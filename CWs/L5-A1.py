#Program to check if the user input is palindrom number or not

# Taking input from the user
number = int(input("Enter your desired number: "))

# Store the original number for later
original_num = number
reversed_num = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

# Checking if the original number is the same as reversed number
if reversed_num == original_num:
    print(f"{original_num} is a palindrom number")
else:
    print(f"{original_num} is not a palindrom number")