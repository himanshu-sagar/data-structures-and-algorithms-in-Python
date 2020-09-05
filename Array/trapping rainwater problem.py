#Complexity-O(n^2)

def getWater(arr,n):
    unit=0
    for i in range(1,n-1):
        lmax=arr[i]
        for j in range(0,i):
            lmax=max(lmax,arr[j])
        rmax=arr[i]
        for j in range(i+1,n):
            rmax=max(rmax,arr[j])
        unit=unit+(min(lmax,rmax)-arr[i])
    return unit
arr=[3,0,1,2,5]
getWater(arr,len(arr))


#complexity:O(n)
def getWater1(arr,n):
    unit=0
    lmax=[]
    lmax.append(arr[0])
    rmax=[0]*n
    rmax[n-1]=arr[n-1]
    for i in range(1,n):
        lmax.append(max(arr[i],lmax[i-1]))
    for i in range(n-2,-1,-1):
        rmax[i]=max(arr[i],rmax[i+1])
    
    for i in range(1,n-1):
        unit=unit+(min(lmax[i],rmax[i])-arr[i])
    return unit
arr=[3,0,1,2,5]
getWater1(arr,len(arr))
