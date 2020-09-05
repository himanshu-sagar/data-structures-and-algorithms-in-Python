def maxIndexDiff(arr,n):
    for i in range(n):
        j=n-i-1
        if arr[i]<=arr[j]:
            return j-i
arr=[65, 6 ,74 ,94 ,56, 89, 9 ,63 ,75 ,25 ,34 ,68, 93 ,48 ,16]

print(maxIndexDiff(arr,len(arr)))
