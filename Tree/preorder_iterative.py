def preorder_iterative(tree):
    from collections import deque
    q=deque()
    n=0
    while(tree!=None or n!=0):
        if tree!=None:
            print(tree.root,end=" ")
            q.append(tree)
            n+=1
            tree=tree.lchild
        else:
            tree=q.pop()
            n-=1
            tree=tree.rchild 
