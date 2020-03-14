from itertools import permutations

l = int(input())
arr = list(map(int,input().split()))

print("".join(map(str,max(list(permutations(arr,l))))))