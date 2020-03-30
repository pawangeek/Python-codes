# https://leetcode.com/problems/bulb-switcher-iii/

light = list(map(int,input().split()))

current_max, count = 0, 0
for n,i in enumerate(light):

    print(n,i)

    # Getting max index upto which light should be on
    current_max = max(i,current_max)

    # If that max is equal to n(iterator) here
    if current_max==n+1:
        count+=1

print(count)
 