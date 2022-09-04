def height(tree):
    if tree==None:
        return 0
    else:
        return max(height(tree.left),height(tree.right))+1
