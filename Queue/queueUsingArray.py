class QueueUsingArray:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def enqueue(self, e):
        self.data.append(e)

    def dequeue(self):
        return self.data.pop(0)
    
    def first(self):
        if self.isempty():
            print('queue is empty')
            return 
        return self.data[0]
    
    def display(self):
        print(self.data)

s = QueueUsingArray()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.dequeue()
s.display()

    