def nextgreater(arr,n):
    st2=[]
    s=[]
    st2.append(arr[-1])
    s.append(-1)
    for i in range(n-2,-1,-1):
        while (len(st2)>0 and st2[-1]<=arr[i]):
            st2.pop()
        if len(st2)<=0:
            print(s.append(-1))
        else:
            s.append(st2[-1])
        st2.append(arr[i])
    s.reverse()
    return s
arr=[5,15,10,8,6,12,9,18]
print(nextgreater(arr,len(arr)))
