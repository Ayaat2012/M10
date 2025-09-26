#Program to show Time Compexity

def printnumber(n):
    iteration=0
    print("The number entered by user is ", n)
    iteration+=1
    print("Total iteration done by the code is ", iteration, "\n")

printnumber(10)
printnumber(15)
print("\nWith any 'n', the time taken by our code won't change.")
#Time complexity of this code is O(1)