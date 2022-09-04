def maxRectangularArea(arr,n):
    res=0
    ps=prevsmaller(arr)
    ns=nextsmaller(arr,len(arr))
    for i in range(len(arr)):
        curr=arr[i]
        curr+=(i-ps[i]-1)*arr[i]
        curr+=(ns[i]-i-1)*arr[i]
        res=max(res,curr)
    return res
arr=[6,2,5,4,1,5,6]
print(maxRectangularArea(arr,len(arr)))
    
