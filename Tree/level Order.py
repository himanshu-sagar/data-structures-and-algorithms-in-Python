def levelorder(tree):
    from collections import deque
    q=deque()
    q.append(tree)
    size=1
    while size!=0:
        p=q.popleft()
        size-=1
        print(p.root,end=" ")
        if p.lchild!=None:
            q.append(p.lchild)
            size+=1
        if p.rchild!=None:
            q.append(p.rchild)
            size+=1
