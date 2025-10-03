def binary_to_decimal(binary):

    decimal_value = 0
    power = 0

    for digit in reversed(binary):
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
    return decimal_value

# Getting user input
input = input("Enter your desired binary number: ")

decimal_result = binary_to_decimal(input)
print(f"The decimal equivalent of {input} is {decimal_result}")