class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):             #returns top element but dont delete it
        return self.items[-1]
    def size(self):
        return len(self.items)
    def display(self):
        print('Elememts of stack are: ',self.items)
        
st=Stack()
for i in range(1,20,2):
    st.push(i)
st.display()
st.pop()
st.display()
