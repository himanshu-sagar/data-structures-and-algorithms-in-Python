def levelOrderLineByLine(tree):
    from collections import deque
    q=deque()
    q.append(tree)
    q.append(None)
    size=2
    while size>1:
        temp=q.popleft()
        size-=1
        if temp==None:
            print()
            q.append(None)
            size+=1
            continue
        print(temp.data,end=" ")
        if temp.left!=None:
            q.append(temp.left)
            size+=1
        if temp.right!=None:
            q.append(temp.right)
            size+=1
    print()
