#Program to show Time Compexity

def OnTime(n):
    iteration=0
    for i in range(1, n+1):
        iteration+=1
        print("When 'n' is ", n, "Iteration is ", iteration)

OnTime(5)
OnTime(10)
OnTime(105)

print("\nWithe every 'n', the time taken and iterations will increase.")
#Time complexity of this code is O(n)