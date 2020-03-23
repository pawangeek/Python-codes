# Solution is very simple in 2*O(n) just traverse though them twice
# Using min() function

# Another efficient solution is to traverse them in a single loop

arr = list(map(int,input().split()))
fir, sec = 0,0

if len(arr)<2:
    print("Not possible")

else:
    for i in range(len(arr)):
        if arr[i]>fir:
            sec = fir
            fir = arr[i]

print(fir, sec)