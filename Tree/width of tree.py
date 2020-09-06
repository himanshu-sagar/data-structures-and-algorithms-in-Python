def width(tree):
    from collections import deque
    q=deque()
    q.append(tree)
    q.append(None)
    size=2
    res=0
    while size>1:
        count=size
        res=max(count,res)
        for i in range(size):
            
            temp=q.popleft()
            size-=1
            if temp==None:
                q.append(None)
                size+=1
                continue
            if temp.left!=None:
                q.append(temp.left)
                size+=1
            if temp.right!=None:
                q.append(temp.right)
                size+=1
    return res-1
    
    
    def width1(root):
    from collections import deque
    q=deque()
    q.append(root)
    width=0
    size=1
    while size!=0:
        width=max(size,width)
        for i in range(size):
            temp=q.popleft()
            size-=1
            if temp.left!=None:
                q.append(temp.left)
                size+=1
            if temp.right!=None:
                q.append(temp.right)
                size+=1
    return width
    
    
