# Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
# https://leetcode.com/contest/biweekly-contest-23/problems/construct-k-palindrome-strings/

from collections import Counter

s = "annabelle"
k = 2

# If lenght is smaller then impossible
if len(s) < k:
    print (False)

# Counting occurances of all characters
counter, odd = Counter(s),0

# If one character has odd times occurrences, there must be at least one palindrome, with odd length and this character in middle.
# So we count the characters that appear odd times, the number of odd character should not be bigger than k.

for v in counter.values():
    if v % 2:
        odd += 1

print (odd <= k)