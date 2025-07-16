class Node:
    __slots__ = 'data','next' #is slightly more memory efficient else completely optional
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isempty(self):
        return self.size == 0

    def push(self,e):
        new_node = Node(e,None)
        if self.isempty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def display(self):
        p = self.head
        while p:
            print(f'{p.data}->',end="")
            p = p.next
        print('')

    def findElement(self, e):
        p = self.head
        index = 0
        while p:
            if p.data == e:
                print('object found')
                return index
            p = p.next
            index += 1
        return -1
    
    def insertSorted(self,e):
        newest = Node(e, None)
        if self.isempty():
            self.head = newest
        else:
            p = self.head
            q = self.head
            while p and p.data < e:
                q = p
                p = p.next
            if p == self.head:
                newest.next = self.head
                self.head = newest
            else:
                newest.next = q.next
                q.next = newest
        self.size += 1

    def insertAtbeginning(self, e):
        new_node = Node(e, None)
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1


    def insertAtpos(self,e,pos):
        new_node = Node(e, None)
        p = self.head
        index = 0
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            while index != pos-1:
                p = p.next
                index += 1
        new_node.next = p.next
        p.next = new_node
        self.size += 1

    
    def removeAtBeginning(self):
        if self.isempty():
            return -1
        p = self.head
        self.head = self.head.next
        return p.data


    def removeAtEnd(self):
        if self.isempty():
            return -1
        p = self.head
        while p.next.next:
            p = p.next
        self.tail = p
        p.next = None
        
        
    def removeAtpos(self, pos):
        if self.isempty():
            return -1
        index = 0
        p = self.head
        while index != pos-1:
            p = p.next
        p.next = p.next.next




L = LinkedList()
L.push(7)
L.push(4)
L.push(12)
L.insertAtbeginning(1)
L.insertAtpos(2,1)
L.display()
print(L.size)
print(L.findElement(4))
# print(L.removeAtBeginning())
#  L.removeAtEnd()
L.removeAtpos(1)
L.display()
