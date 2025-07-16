class stackArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def isempty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            return -1
        return self.data.pop()
    def top(self):
        if self.isempty():
            return -1
        return self.data[-1]
    

S = stackArray()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
print(S.data)
print(S.pop())
print(S.top())
print(S.data)

