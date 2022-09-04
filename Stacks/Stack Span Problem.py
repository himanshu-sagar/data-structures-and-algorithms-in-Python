def stockSpan(arr):
    st1=[]
    st1.append(0)
    n=len(arr)
    for i in range(1,n):
        while (len(st1)>0 and arr[st1[-1]]<=arr[i]):
            st1.pop()
            
        span=i+1 if len(st1)<=0 else (i-st1[-1])
        print(span,end=" ")
        st1.append(i)
arr=[15,13,12,14,16,8,6,4,10,30]
stockSpan(arr)
