def myfunction(n):
    for i in range(0, n+1):
        print("First Loop") #This loop's time complexity is O(n)

    j=1
    while(j<=n+1):
        print("Second Loop", j)
        j=j*2               #This loop's time complexity is O(log n)

    for i in range(0, 100):
        print("Third Loop") #This loop's time complexity is O(1)

    #The overall time complexity will be the sum of the loops: O(n) + O(log n) + O(1).
    #Since "O(n)" repeats more times, it's the dominant term
    #So that is the total complexity of the whole code
    print(f"\nThe overall time complexity of this code is O(n).")

myfunction(8)