def inorder(tree):
    if tree:
        inorder(tree.lchild)
        print(tree.root,end=" ")
        inorder(tree.rchild)
#pass root node in the above function to execute
