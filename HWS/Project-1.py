# Suppose 
n = 3
m = 4

# Multiplying the values in the most efficient method
product = 3 * 4
print(f"The product is {product}")


# Multiplying the values in the least efficient method
def multiply(num1, num2):
    result = 0
    for _ in range(abs(num2)): 
        result += num1
    if num2 < 0:
        return result 
    return result

product = multiply(3, 4)
print(f"Product: {product}")