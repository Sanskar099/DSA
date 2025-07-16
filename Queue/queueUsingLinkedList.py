class Node:
    __slots__ = 'data','next'
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    

class QueueLL:
    def __init__(self):
        self.first = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def first(self):
        return self.first
    
    def enqueue(self,e):
        new_node = Node(e)
        if self.isempty():
            self.first = new_node
        else:
            p = self.first
            while p.next:
                p = p.next
            p.next = new_node
        self.size += 1

    def dequeue(self):
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
            

s = QueueLL()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.dequeue()
s.display()