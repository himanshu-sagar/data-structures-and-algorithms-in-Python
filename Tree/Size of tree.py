def sizeOfTree(tree):#O(n),space-O(height)
    if tree==None:
        return 0
    else:
        return 1+sizeOfTree(tree.left)+sizeOfTree(tree.right)
