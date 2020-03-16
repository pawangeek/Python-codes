# Approach : This approach uses hashing technique : O(n) complexity
# We first count the number of remainders and then there count place in a array
# Remainder with 0 and 2 will form (n(n-1)/2) counts each
# Remainder with 1 and 3 form n*m counts together

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))

    freq,ans = 4*[0],0

    for i in range(p):
        freq[arr[i]%4]+=1

    ans = (freq[0]*(freq[0]-1))/2 # n(n-1)/2
    ans+= (freq[2]*(freq[2]-1))/2    
    ans+= freq[1]*freq[3]

    print(int(ans))
    t-=1