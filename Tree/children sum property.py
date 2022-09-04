def childrenSumProperty(tree):
    if tree==None:
        return True
    if tree.left==None and tree.right==None:
        return True
    sum=0
    if tree.left!=None:
        sum+=tree.left.data
    if tree.right!=None:
        sum+=tree.right.data
    return (tree.data==sum and childrenSumProperty(tree.left) and childrenSumProperty(tree.right))
