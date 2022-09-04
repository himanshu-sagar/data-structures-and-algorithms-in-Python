def majorityWins(arr, n,  x,y):
    # code here
    countx=0
    county=0
    for i in arr:
        if i==x:
            countx+=1
        if y==i:
            county+=1
    if countx>county:
        return x
    elif county>countx:
        return y
    elif county==countx:
        return min(x,y)
