from linkedlist import LinkedList
class hashchain:
    def __init__(self):
        self.size = 10
        # self.table = [[] for i in range(10)]
        self.table = [LinkedList() for i in range(10)]


    def hashcode(self, e):
        return e % self.size
    
    def insert(self, e):
        n = self.hashcode(e)
        self.table[n].insertSorted(e)

    def search(self,e):
        n = self.hashcode(e)
        self.table[n].findElement(e) != -1 

    def display(self):
        for i in range(self.size):
            print(' ',i,' ')
            self.table[i].display()
        print()
    
    
        
        

 



'''array implementation below:  time complexity: O(n)
   The initial if statement checks if e is less than 10, which takes constant time O(1).
If e is less than 10, the code appends e to self.table[e], which takes constant time O(1).
If e is greater than or equal to 10, the code calculates n as e % 10, which takes constant time O(1).
The code then checks if self.table[n] is empty, which takes constant time O(1).
If self.table[n] is not empty, the code iterates through the list to find the correct position to insert e. This iteration takes time O(n), where n is the length of self.table[n].
Once the correct position is found, the code inserts e into the list, which takes constant time O(1).
The code then shifts the remaining elements in the list to make room for e, which takes time O(n) in the worst case.

'''
'''
def insert(self, e):
    print(self.table)
    temp = e
    n = e%10
    i = 0
    if len(self.table[n]) == 0:
        self.table[n].append(e)
        return
    while i < len(self.table[n]) and e >= self.table[n][i]:
        i += 1
    if i >= len(self.table[n])-1 :
        self.table[n].append(e)
    else:
        temp = self.table[n][i]
        self.table[n][i] = e
        i += 1
        while i < len(self.table[n]):
            self.table[n][i], temp = temp, self.table[n][i]
            i += 1
        self.table[n].append(temp)
'''        



s = hashchain()
s.insert(54)
s.insert(38)
s.insert(92)
s.insert(64)
s.insert(34)
s.display()

