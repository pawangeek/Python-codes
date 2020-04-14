# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Solution Description : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation

nums = [0,1,0]

count, max_length, table = 0, 0, {0: 0}

for index, num in enumerate(nums, 1):
    count = count-1 if num == 0 else count+1
            
    if count in table:
        max_length = max(max_length, index - table[count])
    else:
        table[count] = index
        
print(max_length)