
def leftnodes(tree,level):
    if tree==None:
        return
    if maxlevel<level:
        print(tree.data,end=" ")
        maxlevel=level
    printleftnodes(tree.left,level+1)
    printleftnodes(tree.right,level+1)
def printleftnodes(tree,level):
    
    leftnodes(tree,level)
