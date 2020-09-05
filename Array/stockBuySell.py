def stockBuySell(price,n):
    
    if (n==1):
        print("no profit")
    i=0
    count=0
    while(i<(n-1)):
        while((i<(n-1)) and (price[i+1]<=price[i])):
            i+=1
        if (i==n-1):
            break
        buy=i
        i+=1
        while((i<n) and (price[i]>=price[i-1])):
            i+=1
        sell=i-1
        count+=1
        print("(",buy," ",sell,")")
    if count==0:
        print("no profit")
            
        
        
              
price=[100 ,180 ,260 ,310, 40 ,535 ,695]
print(stockBuySell(price,len(price)))
