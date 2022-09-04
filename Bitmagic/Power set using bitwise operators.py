def printPowerSet(st):
    n=len(st)
    powersize=2**n
    for counter in range(powersize):
        for j in range(n):
            if (counter &(1<<j)!=0):
                print(st[j],end=",")
        print(" ")
st='123'
printPowerSet(st)
    
    
