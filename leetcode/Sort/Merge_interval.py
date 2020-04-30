# @Date:   2020-04-30T17:24:58+05:30
# @Last modified time: 2020-04-30T17:27:44+05:30

# Given a collection of intervals, merge all overlapping intervals.
# https://leetcode.com/problems/merge-intervals/

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key=lambda x: x[0])
m = []

for i in intervals:

    # if the list of merged intervals is empty or if the current
    # interval does not overlap with the previous, simply append it.
    if len(m)==0 or m[-1][1]<i[0]:
        m.append(i)

    # otherwise, there is overlap, so we merge the current and previous intervals.
    else:
        m[-1][1]=max(m[-1][1], i[1])

print (m)          
