#Program to find LCM of user input

def LCM(num1, num2):

    #Determinning the greater number
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        #Checking if 'greater' is divisible by both numbers
        if (greater % num1 == 0) and (greater % num2 == 0):
            lcm = greater
            break 
        greater += 1  

    return lcm

#Taking input from the user
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    #Calling the function and print the result
    result_lcm = LCM(number1, number2)
    print(f"The LCM of {number1} and {number2} is {result_lcm}")

except ValueError:
    print("Invalid input. Please enter integers only.")