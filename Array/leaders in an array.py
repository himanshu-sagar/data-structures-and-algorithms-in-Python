def leader(arr,n):
    l=arr[n-1]
    leader=[]
    leader.append(l)
    for i in range(n-2,-1,-1):
        if l<=arr[i]:
            l=arr[i]
            leader.append(l)
    leader.reverse()
    return leader
arr=[7,4,5,7,3]
print(leader(arr,len(arr)))

#Time complexity:O(n)
#space complexity:O(1)
