#Linked List Implementation
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            self.head.next=temp       
    def pop(self):
        if self.head==None:
            return -1
        else:
            p=self.head.data
            self.head=self.head.next
            return p
    def display(self):
        head=self.head
        print("Stack")
        while head!=None:
            print("->",head.data)
            head=head.next
            
            
stack=Stack()
for i in range(1,20,3):
    stack.push(i)
stack.display()
stack.pop()
stack.display()
