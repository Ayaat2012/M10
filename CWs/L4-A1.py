#Program to show if a number is Armstrong or not

#Take input from the user
number = int(input("Input your number: "))

#Calculate number of digits
digits = len(str(number))

#Initialize result variable
resultnumber = 0

#Find the sum of a^digits of each digit
temp = number
while temp > 0:
    digits = temp % 10
    resultnumber += digits ** digits
    temp//=10

#Display the result
if number == resultnumber:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

#153 = 1**(len(number)) + 5**(len(number)) + 3**(len(number))