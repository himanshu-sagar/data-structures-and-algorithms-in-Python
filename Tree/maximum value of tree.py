import sys
def maxValOfTree(tree):#O(n),space-O(height)
    if tree==None:
        return -9987877
    else:
        return max(tree.data,max(maxValOfTree(tree.left),maxValOfTree(tree.right)))
