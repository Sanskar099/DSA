import heapq as heap
L = []
'''
we can also heapify a list by using heap.heapify(list)
'''

heap.heappush(L,20)
heap.heappush(L,14)
heap.heappush(L,15)
heap.heappush(L,10)
heap.heappush(L,2)
heap.heappush(L,21)

print(L)
print(heap.heappop(L))
print(L)

e = heap.heappushpop(L,45) #inserts the element and then removes the element
# heap.heappushpop(L,1) will return one as 1 gets pushed and its the smallest so it gets popped.
print(e)
print(L)
print(heap.nsmallest(3,L)) #returns the n smallest numbers from the heap
print(heap.nlargest(3,L)) #returns the n largest numbers from the heap
