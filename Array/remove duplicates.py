#Time complexity->O(n)
#Space complexity->O(no. of unique elements)
def removeDuplicates(arr,n):
    temp=[]
    temp.append(arr[0])
    ti=1
    for i in range(1,n):
        if temp[ti-1]!=arr[i]:
            temp.append(arr[i])
            ti+=1
    arr=temp
    return arr
arr=[1,1,2,3,4,4,4]
print(removeDuplicates(arr,len(arr))) 



#Time complexity->O(n)
#Space complexity->O(1)

def removeDuplicates1(arr,n):
    ti=1
    for i in range(1,n):
        if arr[i]!=arr[ti-1]:
            arr[ti]=arr[i]
            ti+=1
    return arr,ti
arr=[0,0,1,1,2,3,3,3,4,4,4]
removeDuplicates1(arr,len(arr))   
