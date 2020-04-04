# https://leetcode.com/contest/biweekly-contest-23/problems/reducing-dishes/
# Like-time is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  
# i.e.  time[i]*satisfaction[i]. Return the maximum sum of Like-time coefficient

satisfaction = [-2,5,-1,0,3,-3]
s,l = satisfaction.copy(),len(satisfaction)

s.sort()
cnt = 0

for i in range(l):
    temp = 0
    for j in range(i, l):
        temp += s[j] * (j - i + 1)
                
    cnt = max(temp, cnt)

print(cnt)