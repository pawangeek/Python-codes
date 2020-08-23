# @Date:   2020-04-30T17:28:00+05:30
# @Last modified time: 2020-04-30T17:29:49+05:30

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# https://leetcode.com/problems/insert-interval/

intervals = [[1,3],[6,9]]
new = [2,5]

merged,t,l = [], 0, len(intervals)
for curr in intervals:

    # If interval[i] completely smaller than new one
    if new[0]>curr[1]:
        merged.append(curr)

    # If interval[i] completely greater than new
    elif curr[0]>new[1]:
        break

    # If interval[i] is overlapping with new
    else:
        # choose minm and maxm boundaries from both
        new[0] = min(new[0], curr[0])
        new[1] = max(new[1], curr[1])

    t+=1

# Apeending last new interval
merged.append(new)

# Now understand this part
# i) If new part extend till end than simply return merged ones
# ii) If not till end than return merged + remainling intervals
print (merged+intervals[t:]) if t<l else print(merged)
