#naive
def powerOf2(n):
    if n==0:
        return False
    while (n!=1):
        if (n%2!=0):
            return False
        n=n/2
    return True
print(powerOf2(54475758))

#Using Brian karningham algorithm

#complexity=O(no. of set bits)----O(1)
def powerOf2_1(n):
    if countSetBitBrian(n)==1:
        return True
    else:
        return False
powerOf2_1(32)


#complexity=O(no. of set bits)----O(1)
def powerOf2_2(n):
    return (n!=0)and((n&(n-1))==0)
powerOf2_1(128)
