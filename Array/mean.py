def mean(arr,n):
    sum=0
    for i in arr:
        sum=sum+i
    return sum//n
arr=[1,2,3,6,8]
print(mean(arr,len(arr)))
