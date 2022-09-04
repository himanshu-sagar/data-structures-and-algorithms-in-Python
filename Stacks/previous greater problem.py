def prevGreater(arr):
    st2=[]
    st2.append(arr[0])
    s=[]
    s.append(-1)
    for i in range(1,len(arr)):
        while (len(st2)>0 and st2[-1]<=arr[i]):
            st2.pop()
        if len(st2)<=0:
            s.append(-1)
        else:
            s.append(st2[-1])
        st2.append(arr[i])
    return s
arr=[15,13,12,14,16,8,6,4,10,30]
print(prevGreater(arr))
