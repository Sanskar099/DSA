# class Heap:
#     def __init__(self):
#         self._maxsize = 10
#         self._data = [-1] * self._maxsize
#         self._csize = 0

#     def __len__(self):
#         return len(self._data)

#     def isempty(self):
#         return len(self._data) == 0

#     def insert(self, e):
#         if self._csize == self._maxsize:
#             print('No Space in Heap')
#             return
#         self._csize = self._csize + 1
#         hi = self._csize
#         while hi > 1 and e > self._data[hi // 2]:
#             self._data[hi] = self._data[hi // 2]
#             hi = hi // 2
#         self._data[hi] = e

#     def max(self):
#         if self._csize == 0:
#             print('Heap is Empty')
#             return
#         return self._data[1]

#     def deletemax(self):
#         if self._csize == 0:
#             print('Heap is Empty')
#             return
#         e = self._data[1]
#         self._data[1] = self._data[self._csize]
#         self._data[self._csize] = -1
#         self._csize = self._csize - 1
#         i = 1
#         j = i * 2
#         while j <= self._csize:
#             if self._data[j] < self._data[j+1]:
#                 j = j + 1
#             if self._data[i] < self._data[j]:
#                 temp = self._data[i]
#                 self._data[i] = self._data[j]
#                 self._data[j] = temp
#                 i = j
#                 j = i * 2
#             else:
#                 break
#         return e


class Heap:
    def __init__(self):
        self.csize = 0
        self.maxsize = 10
        self.data = [-1]*self.maxsize

    def isempty(self):
        return self.data[1] == -1
    
    def __len__(self):
        return len(self.data)
    
    def insert(self, e):
        if self.csize == self.maxsize:
            print('the heap is full')
            return
        self.csize += 1
        hi = self.csize
        while hi > 1 and e > self.data[hi//2]:
            self.data[hi] = self.data[hi//2]
            hi = hi//2
        self.data[hi] = e
    
    def deletemax(self):
        if self.isempty():
            print('empty heap')
            return
        e = self.data[1]
        self.data[1] = self.data[self.csize]
        self.data[self.csize] = -1
        self.csize -= 1
        i = 1 
        j = i*2
        while j <= self.csize:
            if self.data[j] < self.data[j+1]:
                j += 1
            if self.data[i] < self.data[j]:
                (self.data[i],self.data[j]) = (self.data[j],self.data[i])
                i = j
                j = i*2
            else:
                break
        return e

    

s = Heap()
s.insert(20)
s.insert(14)
s.insert(2)
s.insert(15)
s.insert(10)
s.insert(21)
# print(s._data)
# print(s.deletemax())
# print(s._data)
print(s.data)
print(s.deletemax())
print(s.data)

