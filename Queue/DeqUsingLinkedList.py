class Node:
    __slots__ = 'data','next'
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    

class DeQueueLL:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def first(self):
        return self.first
    
    def last(self):
        return self.last
    
    def enqueueFirst(self,e):
        new_node = Node(e)
        if self.isempty():
            self.first = new_node
            self.last = new_node

        else:
            p = self.first
            new_node.next = p
            self.first = new_node
        self.size += 1

    
    def enqueueLast(self,e):
        new_node = Node(e)
        if self.isempty():
            self.first = new_node
            self.last = new_node
        else:
            p = self.first
            while p.next:
                p = p.next
            p.next = new_node
        self.size += 1

    def dequeueLast(self):
        if self.isempty():
            print('the queu is empty')
            return
        p = self.last.data
        q = self.first
        while q.next.next != None:
            q = q.next
        q.next = None
        self.last = q
        self.size -= 1
        return p
    
    def dequeueFirst(self):
        if self.isempty():
            print('the queu is empty')
            return
        p = self.first
        self.first = self.first.next
        self.size -= 1
        return p.data
    
    def display(self):
        if self.isempty():
            print('the queu is empty')
        else:
            p = self.first
            while p:
                print(p.data,end='--> ')
                p = p.next
        print("")
            

s = DeQueueLL()
s.enqueueLast(1)
s.enqueueLast(2)
s.enqueueLast(3)
s.enqueueFirst(4)
s.enqueueFirst(5)
s.display()
s.dequeueFirst()
s.display()
s.dequeueLast()

s.display()