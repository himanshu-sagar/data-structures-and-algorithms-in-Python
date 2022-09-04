def postorder(tree):
    if tree:
        postorder(tree.lchild)
        postorder(tree.rchild)
        print(tree.root,end=" ")
