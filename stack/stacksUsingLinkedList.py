class Node:
    __slots__ = 'data','next'
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    
class stackLL:
    def __init__(self):
        self.size = 0
        self.top = None
    
    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def push(self,e):
        new_node = Node(e)
        if self.isempty():
            self.top = new_node
            self.size += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.size += 1
        
    
    def pop(self):
        if self.isempty():
            print('the stack is empty')
            return 
        p = self.top
        self.top = p.next
        return p.data
    
    def Top(self):
        if self.isempty():
            return -1
        return self.top.data
    
    def display(self):
        if self.isempty():
            print('the list is empty')
        p = self.top
        while p:
            print(p.data,end="--> ")
            p = p.next

s = stackLL()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.Top())
s.display()


