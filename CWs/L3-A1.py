def prints(n):
    if(n<=0):
        return
    print("Codingal")

    prints(n//2)
    prints(n//2)

prints(4)
prints(6)

#Time complexity is O(n)