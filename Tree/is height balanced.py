def isHeightbalanced(tree):#O(n^2)
    if tree==None:
        return True
    lh=height(tree.left)
    rh=height(tree.right)
    x=lh-rh
    return (abs(x)<=1 and isHeightbalanced(tree.left) and isHeightbalanced(tree.right))
    
