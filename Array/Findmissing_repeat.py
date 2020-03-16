# Imp : Task : Find missing and repeating value
# Approach : TO mark them index positive where this thing happen 

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))

    for val in arr:

        arr[abs(val) - 1] *= -1
        print(arr)

        inc = []
        for i in range(p):
            if arr[i]>0:
                inc.append(i+1)
           
    print(inc[0], inc[1]) if inc[0] in arr else print(inc[1],inc[0])      
    t-=1