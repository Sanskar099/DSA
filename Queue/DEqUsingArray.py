class DeqUsingArray:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)
    
    def isempty(self):
        return len(self.data) == 0
    
    def pushfirst(self,e):
        if self.isempty():
            self.data.append(e)
        else:
            element = self.data[0]
            self.data[0] = e
            for i in range( 1, len(self.data)):
                self.data[i], element  = element, self.data[i]
            self.data.append(element)

    def pushlast(self,e):
        self.data.append(e)


    def removefirst(self):
        if self.isempty(): 
            print('the dequeue is empty')
            return
        return self.data.pop(0)

    def removelast(self):
        if self.isempty(): 
            print('the dequeue is empty')
            return
        return self.data.pop()
    
    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[-1]

    def display(self):
        print(self.data)

d = DeqUsingArray()
d.pushfirst(1)
d.pushfirst(2)
d.pushfirst(3)
d.pushlast(4)
print(d.removefirst())
print(d.removelast())
d.display()
