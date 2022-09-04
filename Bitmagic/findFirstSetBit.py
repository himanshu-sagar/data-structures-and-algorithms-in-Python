def findFirstSetBit(n):
    pos=0
    while(n&1==0):
        pos=pos+1
        n=n>>1
        print(n)
    return pos
print(findFirstSetBit(8))
