#very bad for sorting large number of arrays
def SelectionSort(A : list[int])->list[int]:
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[j] < A[i]:
                A[i], A[j] = A[j],A[i]
    return A


print(SelectionSort([5,4,2,3,1]))
