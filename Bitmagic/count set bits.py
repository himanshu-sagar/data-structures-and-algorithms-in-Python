def countSetBit(n):
    count=0
    while(n>0):
        if (n%2)!=0:
            count+=1
            n=n//2
    print(count)
countSetBit(7)


#complexity= O(no. of set bits)
def countSetBitBrian(n):
    count=0
    while (n>0):
        n=n&(n-1)
        count+=1
    return count
print(countSetBitBrian(3))


