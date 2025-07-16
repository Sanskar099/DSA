# from Queue.queueUsingArray import QueueUsingArray
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
class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, e, left=None, right=None):
        self._root = _Node(e,left._root,right._root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

    def preorder(self,troot):
        if troot:
            print(troot._element,end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    
    def levelorder(self):
        q = QueueUsingArray()
        t = self._root
        print(t._element,end=' ')
        q.enqueue(t)
        while not q.isempty():
            t = q.dequeue()
            if t._left:
                print(t._left._element,end=' ')
                q.enqueue(t._left)
            if t._right:
                print(t._right._element,end=' ')
                q.enqueue(t._right)


    def countNodes(self, troot):
        if troot :
            x = self.countNodes(troot._left)
            y = self.countNodes(troot._right)
            return x + y + 1
        return 0
    
    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            print(x,y)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree() #we have to make this null binary tree because for case scenarios where it wont except null for just one value
x.maketree(40,a,a)
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,y)
s.maketree(30,r,a)
t.maketree(10,z,s)
print('Inorder Traversal')
t.inorder(t._root)
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print('level order traversal')
t.levelorder()
print('')
print(t.countNodes(t._root))
print(t.height(t._root)-1) #subtracting one because the function returns one extra as height.
'''
        10
    20        30
40          50
                60      

'''
