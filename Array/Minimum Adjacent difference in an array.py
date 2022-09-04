def minAdjDiff(arr, n):
    min=abs(arr[1]-arr[0])
    
    for i in range(1,n-1):
        min1=abs(arr[i+1]-arr[i])
        
        if min1<min:
            min=min1
        
    min1=abs(arr[n-1]-arr[0])    
    if min1<min:
        min=min1
    return min
arr=[8 ,-8, 9 ,-9 ,10 ,-11 ,12]
minAdjDiff(arr,len(arr))
