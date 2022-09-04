def isHeightbalanced(tree):#O(n^2)
    if tree==None:
        return True
    lh=height(tree.left)
    rh=height(tree.right)
    x=lh-rh
    return (abs(x)<=1 and isHeightbalanced(tree.left) and isHeightbalanced(tree.right))
    
def isHeightbalanced1(tree):#O(n)
    if tree==None:
        return 0
    lh=isHeightbalanced1(tree.left)
    if lh==-1:
        return -1
    rh=isHeightbalanced1(tree.right)
    if rh==-1:
        return -1
    x=abs(lh-rh)
    if x>1:
        return -1
    else:
        return max(lh,rh)+1
    
    
        
