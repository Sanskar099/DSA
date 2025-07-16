def InsertionSort(A: list[int])->list[int]:
    for i in range(1,len(A)):
        while i > 0 and A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            i -= 1
    return A

print(InsertionSort([5,3,4,1,2]))