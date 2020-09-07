def searchingBST(tree,key):
    if tree==None:
        return None
    if (key==tree.data):
        return tree
    elif(key<tree.data):
        return searchingBST(tree.left,key)
    else:
        return searchingBST(tree.right,key)

flag=searchingBST(tree,3)
if flag==None:
    print("Element is Not Present in the Tree")
else:
    print("Element is found at address: ",flag," and data is: ",flag.data)
def searchingBST_iterative(tree,key):
    while(tree!=None):
        if(key==tree.data):
            return tree
        elif(key<tree.data):
            tree=tree.left
        else:
            tree=tree.right

flag=searchingBST(tree,4)
if flag==None:
    print("Element is Not Present in the Tree")
else:
    print("Element is found at address: ",flag,"\n and data is: ",flag.data)
