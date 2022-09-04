#Complexity=O(n^2)

def maxProfit(price,start,end):
    if (end <=start):
        return 0
    profit=0
    curr_profit=0
    for i in range(start,end):
        for j in range(i+1,end):
            if price[j]>price[i]:
                curr_profit=price[j]-price[i]+maxProfit(price,start,i-1)+maxProfit(price,j+1,end)
                profit=max(profit,curr_profit)
    return profit
price=[1,5,3,8,12]
maxProfit(price,0,len(price))



def maxProfit1(price,n):
    profit=0
    for i in range(1,n):
        if price[i]>price[i-1]:
            profit+=(price[i]-price[i-1])
    return profit
price=[1,5,3,8,12]
maxProfit1(price,len(price))
