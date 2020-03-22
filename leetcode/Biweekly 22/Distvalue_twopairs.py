#The distance value is defined as the number of elements arr1[i] 
# such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

# https://leetcode.com/contest/biweekly-contest-22/problems/find-the-distance-value-between-two-arrays/

# Complexity : n^2
# Difficulty : Easy

# Naive Approach (two loops)
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
d = int(input())

for i in arr1:
    for j in arr2:
        if abs(i-j)<=d:
            c+=1
            break
                    
print (len(arr1)-c)

# Can be done in O(nlogm) by using sort + two pointers