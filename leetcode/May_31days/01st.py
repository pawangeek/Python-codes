# @Date:   2020-05-02T17:04:11+05:30
# @Last modified time: 2020-05-02T17:08:49+05:30

# First Bad Version
# https://leetcode.com/problems/first-bad-version/

# Concept Binary search
def firstBadVersion(self, n):

    l = 1
    r = n

    while l<r:

        # calc mid
        mid =(l+r)//2

        # isBadVersion given function
        if isBadVersion(mid):
            r = mid

        else:
            l = mid+1

    return l
