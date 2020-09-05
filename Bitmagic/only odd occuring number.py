#naive
def oddOccuringNumber(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if (arr[j]==arr[i]):
                count+=1
        if count%2!=0:
            print(arr[i])
        
#complexity ---O(n^2)
arr=[4,3,4,4,4,5,5]
oddOccuringNumber(arr)

#using xor

def oddOccuringNumber1(arr):
    xor=0
    for i in range(len(arr)):
        xor=xor^arr[i]
    return xor
arr=[4,3,4,4,4,5,5]
oddOccuringNumber1(arr)
