def majorityWins(arr,n,x,y):
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
arr=[1,4,3,3,4,5,3,1,2,2]
majorityWins(arr,len(arr),2,3)
