class Node:
    __slots__ = 'data','next','prev'
    def __init__(self, data, next= None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def addlast(self,e):
        new_node = Node(e)
        if self.isempty() :
            self.head = new_node
            self.tail = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
            new_node.prev = p
        self.size += 1

    def insertAtbeginning(self, e):
        new_node = Node(e)
        if self.isempty() :
            self.head = new_node
            self.tail = new_node
        else:
            p = self.head
            new_node.next = p
            p.prev = new_node
            self.head = new_node
        self.size += 1

    def insertAnywhere(self, e, pos):
        new_node = Node(e)
        if self.isempty() :
            self.head = new_node
            self.tail = new_node
        else:
            index = 0
            p = self.head
            while index < pos - 1:
                p = p.next
                index += 1
            new_node.next = p.next
            p.next.prev = new_node
            p.next = new_node
            new_node.prev = p
        self.size += 1



    def deleteAtbeginning(self):
        p = self.head.next
        p.prev = None
        self.head = p
        self.size -= 1
    
    def deleteAtend(self):
        p = self.head
        while p.next.next:
            p = p.next
        p.next = None
        self.size -= 1

    def deleteAnywhere(self, pos):
        p = self.head
        index = 0
        while index < pos -1:
            p = p.next
            index += 1
        q = p.next.next
        p.next = q
        q.prev = p
        self.size -= 1

    def display(self):
        if self.isempty():
            print('the list is empty')
        p = self.head
        while p:
            print(p.data,end="--> ")
            p = p.next


D = DoublyLinkedList()
D.addlast(1)
D.addlast(2)
D.addlast(3)
D.insertAtbeginning(4)
D.insertAnywhere(5,2)
# D.deleteAtbeginning()
D.deleteAnywhere(2)
# D.deleteAtend()
D.display()

            
    
