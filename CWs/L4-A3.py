#Program to convert roman numerals into integers

def romanToInt(romanInput):

    # All roman numerals with integer equivalent values
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    #result
    resultInt = 0

    #Go from 0 to len-1: if integer equivalent is greater than next element, add it; else substract it
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i + 1]]:
            resultInt -= roman[romanInput[i]]
        else:
            resultInt += roman[romanInput[i]]

    return resultInt + roman[romanInput[-1]]

# Taking roman as input from user
roman = input("Input roman numeral: ")

# Printing the integer
print("Integer equivalent : ", romanToInt(roman))