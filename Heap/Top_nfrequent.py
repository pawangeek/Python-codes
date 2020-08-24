from collections import Counter
import heapq

def nfrequent(arr, k):

    if k == len(arr):
        return arr

    count = Counter(arr)

    return heapq.nlargest(k, count.keys(), key = count.get)

arr = [1,1,1,2,2,3] 
k = 2

print(nfrequent(arr,k))