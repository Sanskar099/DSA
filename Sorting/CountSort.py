'''
The basic approach is to find the max element, create an empty array initalised with
0s from 0 to the max element and increment at the position of the elements found in the array
'''

def CountSort(A:list[int]):
    maxe = max(A)
    B = [0 for i in range(0,maxe+1)]
    for i in A:
        B[i] += 1

    k = 0
    print(B)
    for i in range(0, len(B)):
        if B[i] > 0:
            while(B[i]!= 0):
                A[k] = i
                B[i] -= 1
                k += 1

A= [7,6,4,5,6,5,3,2]
print("original array")
print(A)
CountSort(A)
print('sorted array')
print(A)