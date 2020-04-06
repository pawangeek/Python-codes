from collections import defaultdict

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
# Given an array of strings, group anagrams together.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list) # Dictionary initialization

# tuple(sorted(i)) is sorted string like ;'eat' to 'aet' we use that as a key
# Further we append the incoming values to as per the key

for i in strs:
    groups[tuple(sorted(i))].append(i)

# and finally we take the values from corresponding to each key  
print (list(groups.values()))