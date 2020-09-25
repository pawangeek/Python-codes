# Mostly likely knapsack problem

target= 9
arr = [3,5,4,2]

dp = [[False for i in range(target+1)] for j in range(len(arr)+1)]
# Createa table with False initialize in it

for i in range(len(arr)+1):
    for j in range(target+1):

        # For 1st row since we can create 0 target with not seleting anyone always
        if j==0:
            dp[i][j] = True
        
        # We can't create anything with 0 elements except 0 (hence just dp[0][0] is True)
        elif i==0:
            dp[i][j] = False

        # Else what we will do
        # We have 
        else:
            if j<arr[i-1]:
                dp[i][j] = dp[i-1][j]

            # Else what we will do we have two choices
            # i) Either 
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

for i in range(len(arr)+1):
    print(dp[i])

print(dp[len(arr)][target])