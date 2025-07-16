def BubbleSort(A:list[int])->list[int]:
    passes = len(A) -1
    while passes > 0:
    #   swapped = False
        for i in range(0, passes):
            if A[i] > A[i+1]:
                A[i+1], A[i] = A[i], A[i+1]  
        passes -= 1          
    return A


print(BubbleSort([3,5,4,1,2]))
        