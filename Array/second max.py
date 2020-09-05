def secondMax(arr,n):
    arr.sort()
    return arr[-2]
arr=[1,4,3,3,4,5,3,1,2,2]
secondMax(arr,len(arr))
