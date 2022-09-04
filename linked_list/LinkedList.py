class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        head = LinkedList()
        data = int(input("Enter Elements(-1 to stop): "))
        while (data != -1):
            if head == None:
                head = Node(data=data)
                tail = Node(data=data)
            else:
                
