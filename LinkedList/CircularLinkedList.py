class Node:
    __slots__= 'data','next'
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size #pretty useful tbh can be used as len(self) for loops
    
    def isempty(self):
        return self.size == 0

    def addlast(self, e):
        new_node = Node(e, None)
        if self.isempty():
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.size += 1

    def insertAtbeginning(self, e):
        new_node = Node(e, None)
        if self.isempty():
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1
    

    def insertAtPos(self, e, pos):
        new_node = Node(e, None)
        index = 0
        p = self.head
        while index < pos-1:
            index += 1
            p = p.next
        new_node.next = p.next
        p.next = new_node
        self.size += 1



    def display(self):
        if self.isempty():
            print('empty linked list')
        index = 0
        p = self.head
        while index < self.size:
            print(p.data,end="--> ")
            index += 1
            p = p.next



    def deleteAtbeginning(self):
        if self.isempty():
            return -1
        p = self.head
        self.tail.next = self.head.next
        self.head = self.head.next
        self.size -= 1
        return p.data

    def deleteAtend(self):
        if self.isempty():
            return -1
        p = self.head
        while p.next != self.tail:
            p = p.next
        p.next = self.tail.next
        self.tail = p
        self.size -= 1
        

    def deleteAtpos(self,pos):
        if self.isempty():
            return -1
        p = self.head
        index = 0
        while index < pos - 1:
            p = p.next
            index += 1
        p.next = p.next.next
        self.size -= 1
        

L = CircularLinkedList()
L.addlast(12)
L.addlast(7)
L.addlast(4)
L.insertAtbeginning(1)
L.insertAtPos(2,1)
# L.deleteAtbeginning()
#L.deleteAtend()
L.deleteAtpos(2)
L.display()