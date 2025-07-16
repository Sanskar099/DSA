def ShellSort(A:list[int])->list[int]:
    gap = len(A)//2
    while gap != 0:
        for i in range(0, len(A)):
            print(A,' ',i,i+ gap)
            if i+ gap >= len(A):
                break
            else:
                print('inside loop 1')
                if A[i] > A[i+gap]:
                    A[i], A[i+gap] = A[gap+i] , A[i]
                if i-gap >= 0:
                    print('inside loop 2')
                    if A[i-gap] > A[i]:
                        A[i], A[i-gap] = A[i-gap], A[i]
        gap = gap//2
    return A

print(ShellSort([5,4,2,3,1]))
