def strongestNeighbour(arr,n):
    for i in range(n-1):
        print(max(arr[i],arr[i+1]))
arr=[1,4,3,3,4,5,3,1,2,2]
strongestNeighbour(arr,len(arr))
