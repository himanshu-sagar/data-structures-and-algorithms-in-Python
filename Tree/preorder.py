def preorder(tree):
    if tree:
        print(tree.root,end=" ")
        preorder(tree.lchild)
        preorder(tree.rchild)
