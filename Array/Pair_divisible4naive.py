# Task : COunt every pair i.e. divisible by 4
# Aprroach : Naive approach by 2 loops (comp:n^2)

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))

    cnt=0
    for i in range(p):
        for j in range(i+1,p):
            if((arr[i]+arr[j])%4==0):
                cnt+=1

    print(cnt)
    t-=1
