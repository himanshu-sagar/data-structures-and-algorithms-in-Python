def median(arr,n):
    arr.sort()
    mid=n//2
    return arr[mid]
arr=[1,67,2,3,5,6,8,87]
print(median(arr,len(arr)))
