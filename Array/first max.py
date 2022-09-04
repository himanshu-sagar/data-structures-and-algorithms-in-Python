def max1(arr,n):
    maxx=arr[0]
    for i in arr:
        if maxx<i:
            maxx=i
    return maxx
arr=[1,4,3,3,4,5,3,1,2,2]
max1(arr,len(arr))
