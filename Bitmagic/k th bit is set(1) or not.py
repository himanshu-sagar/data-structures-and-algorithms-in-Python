def KthBitSetLeft(n,k):
    if (n & (1<<(k-1)))!=0:
        print(k,"th bit is set")
    else:
        print(k,"th bit is not set")
KthBitSetLeft(10,2)
