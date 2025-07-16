def RadixSort(A):
    n = len(A)
    max_e = max(A)
    digits = len(str(max_e))
    bins = [[] for i in range(10)]
    for i in range(0,digits+1):
        for j in range(0,n):
            e = int((A[j]/pow(10,i))%10)
            bins[e].append(A[j])
        k = 0
        for i in range(0,10):
            if len(bins[i]) > 0:
                while bins[i]:
                    A[k] = bins[i].pop(0)
                    k  += 1
            
            


A = [33,12,555,234,123]
RadixSort(A)
print(A)