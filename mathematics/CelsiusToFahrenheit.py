{
#Initial Template for Python 3
import math
//Position this line where user code will be pasted.
def main():
    
    T=int(input())
    
    while(T>0):
        C=int(input())
        print(math.floor(cToF(C)))
        T-=1
    
    
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
def cToF(C):
    #Your code here
    return ((9/5)*C + 32)