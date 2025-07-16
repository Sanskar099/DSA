def QuickSort(A:list[int], i, j):
    pivot = i
    while i <= j:
        while A[i] < A[pivot]:
            i += 1
        while A[j] > A[pivot]:
            j -= 1
        if i <= j:
            A[i],A[j] = A[j],A[i]
            
    A[pivot], A[j] = A[j], A[pivot] #now the element j is at right position atleast so im happy
    QuickSort(A, pivot, j)
    QuickSort(A,i, len(A)-1)


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
QuickSort(A,0,len(A)-1)
print('Sorted Array:',A)