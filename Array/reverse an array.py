def reverse(arr,n):
    arr1=[]
    for i in arr:
        arr1.insert(0,i)
    return arr1
arr=[1,2,45,3,4,5,65]
reverse(arr,len(arr))

def reverse1(arr,n):
    left=0
    right=n-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=[1,2,45,3,4,5,65]
reverse1(arr,len(arr))
        
        
