# @Date:   2020-04-26T23:29:09+05:30
# @Last modified time: 2020-04-26T23:30:44+05:30

from collections import defaultdict
# The key property is that i+j is the same for all elements of the same diagonal.
# We can then traverse each row from top to bottom and finally reverse the diagonals we find at the end.

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

# we create a dic indexed by sum i+j, as all items in a diagonal will have the same sum.
diagonals = defaultdict(list)

# traverse from top row to bottom; we can see this is reversed order compared to our desired result.
for i, line in enumerate(nums):
    for j in range(len(line)):

        # add the element to the correct bucket.
        diagonals[i+j].append(line[j])

i = 0
ret = []

# we now reverse the buckets and concatenate them to get the result.
while i in diagonals:
    ret.extend(diagonals[i][::-1])
    i += 1
print (ret)
