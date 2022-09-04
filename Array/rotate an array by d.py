
def rotateArray(arr,n,d):
    for i in range(d):
        arr.append(arr[0])
        arr.remove(arr[0])
    return arr
arr=[1,2,3,4,5]
print(rotateArray(arr,len(arr),2))

#Time complexity:O(nd)
#space Complexity:O(1)
def rotateArray1(arr,n,d):
    i=0
    while(i<d):
        temp=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
        i+=1
        
    return arr
arr=[1,2,3,4,5]
print(rotateArray1(arr,len(arr),3))

#Time complexity:O(n)
#space Complexity:O(d)
def rotateArray2(arr,n,d):
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(d):
        arr[n-d+i]=temp[i]
    return arr
arr=[1,2,3,4,5]
print(rotateArray2(arr,len(arr),3))

#Time complexity:O(2n)
#space Complexity:O(1)

def reverse2(arr,left,right):
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
def rotateArrayByd(arr,n,d):
    reverse2(arr,0,d-1)
    reverse2(arr,d,n-1)
    reverse2(arr,0,n-1)
    return arr
arr=[1,2,3,4,5]
print(rotateArrayByd(arr,len(arr),3))


