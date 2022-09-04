def secondLargest(arr,n):
    arr=set(arr)
    arr=list(arr)
    arr.sort()
    n=len(arr)
    if len(arr)==1:
        return arr[n-1],-1
    else:
        return arr[n-1],arr[n-2]
    
arr=[1,1,1,1,67,1,6,8]
secondLargest(arr,len(arr))
