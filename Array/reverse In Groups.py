def reverseInGroups(arr,n,k):
    def reverse(arr,n):
        arr1=[]
        for i in arr:
            arr1.insert(0,i)
        return arr1
    arr2=[]
    for i in range(0,n,k):
        A=reverse(arr[i:i+k],k)
        for a in A:
            arr2.append(a)
    return arr2
arr=[1,2,3,4,5,6,7,8]
reverseInGroups(arr,len(arr),3)
        
    
