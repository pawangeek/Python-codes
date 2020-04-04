arr = [60 ,-65 ,5 ,-21 ,8 ,93]
n = len(arr)
f = 0

arr.sort()
print(arr)

for i in range(0, n-1):

    # initialize left and right
    l,r, x = i+1, n-1, arr[i]

    while (l < r): 
          
        if (x + arr[l] + arr[r] == 0): 

            # print elements if it's sum is zero 
            print(x, arr[l], arr[r]) 
            l, r, f = l+1, r-1, 1

        # If sum of three elements is less than zero then increment in left 
        elif (x + arr[l] + arr[r] < 0): 
            l+=1
        
        # If sum of three greater than zero decrement in right
        else:
            r-=1

print (f==1)