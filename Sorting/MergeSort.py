# # def merge(A : list[int], left, mid, right):
# #     i = left
# #     j = mid + 1
# #     B = []
# #     while i <= mid and j <= right:
# #         if A[i] <= A[j]:
# #             B.append(A[i])
# #             i += 1
# #         else:
# #             B.append(A[j])
# #             j += 1
# #     while i <= mid:
# #         B.append(A[i])
# #         i += 1

# #     while j <= right:
# #         B.append(A[j])
# #         j += 1

# #     for k in range(left,):
# #         A[k] = B[k]

# def merge(A, left, mid, right):
#     i = left
#     j = mid+1
#     k = left
#     B = [0] * (right+1)
#     while i <= mid and j <= right:
#         if A[i] < A[j]:
#             B[k] = A[i]
#             i = i + 1
#         else:
#             B[k] = A[j]
#             j = j + 1
#         k = k + 1

#     while i <= mid:
#         B[k] = A[i]
#         i = i + 1
#         k = k + 1

#     while j <= right:
#         B[k] = A[j]
#         j = j + 1
#         k = k + 1
#     for x in range(left,right+1):
#         A[x] = B[x]

# def mergeSort(A: list[int], left, right):
#     if left < right:
#         mid = (left + right)//2
#         mergeSort(A,left,mid)
#         mergeSort(A,mid+1, right)
#         merge(A,left,mid,right)

    


# A = [5,3,4,1,2]
# mergeSort([5,3,4,1,2],0,4)
# print(A)
def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right + 1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        B[k] = A[i]
        i = i + 1
        k = k + 1

    while j <= right:
        B[k] = A[j]
        j = j + 1
        k = k + 1
    for x in range(left,right+1):
        A[x] = B[x]


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
mergesort(A,0,len(A)-1)
print('Sorted Array:',A)