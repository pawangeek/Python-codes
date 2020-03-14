# logic is break array in two parts from rotaion point
# Example : [1 2 3 4 5] Break it into sub lists [1 2] and [3 4 5] And join them 

l,d = map(int,input().split())
arr = list(map(int,input().split()))

f,c = arr[0:d], arr[d:l]
print(c+f)