# @Date:   2020-04-30T16:45:50+05:30
# @Last modified time: 2020-04-30T16:52:44+05:30

# You have a queue of integers, you need to retrieve the first unique integer in the queue.

# Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.

# We use an OrderedDict named unique_nums as an ordered hash set to store the unique numbers.
# Only unique numbers will be as a key in unique_nums.

# Then we use a hash set named added_nums to store all numbers ever added
# so that we can know if a number is added before if it is not in unique_nums.

# Time Complexity: O(1) showFirstUnique, O(1) add
# Space Complexity: O(n)

from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique_nums = OrderedDict()
        self.added_nums = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # if unique_nums is not empty, return the first key in it.
        for num in self.unique_nums.keys():
            return num
        return -1

    def add(self, value: int) -> None:
        if value in self.added_nums:
            if value in self.unique_nums:
                del self.unique_nums[value]
        else:
            self.added_nums.add(value)
            self.unique_nums[value] = None # the mapped value doesn't matter
