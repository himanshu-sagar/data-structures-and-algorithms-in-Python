def Height(tree):
    if tree==None:
        return 0
    else:
        return max(height(tree.left),height(tree.right))+1
def inorder_predecessor(tree):
    while tree and tree.right:
        tree=tree.right
    return tree

def inorder_successor(tree):
    while tree and tree.left:
        tree=tree.left
    return tree

def deleteBST(tree,key):
    global root# initialise root outside this function with the first node created 
    if tree==None:
        return None
    if tree.left==None and tree.right==None:
        if tree==root:
            tree=None
        return None
    if key<tree.data:
        tree.left=deleteBST(tree.left,key)
        
    elif key>tree.data:
        tree.right=deleteBST(tree.right,key)
        
    else:
        if Height(tree.left)>Height(tree.right):
            temp1=inorder_predecessor(tree.left)
            tree.data=temp1.data
            tree.left=deleteBST(tree.left,temp1.data)
        else:
            temp1=inorder_successor(tree.right)
            tree.data=temp1.data
            tree.right=deleteBST(tree.right,temp1.data)
    return tree
    
tree_after_deletion=deleteBST(tree,7)
print(tree)
inorder(tree_after_deletion)
