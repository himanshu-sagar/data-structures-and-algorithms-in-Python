def printKthLevel(tree,k):#O(n),space=O(height)
    if tree==None:
        return
    if k==0:
        print(tree.data,end=" ")
    else:
        printKthLevel(tree.left,k-1)
        printKthLevel(tree.right,k-1)
