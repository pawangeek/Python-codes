# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        # if stack is empty, set the cur_min as x+1 to garantee we can set the updated min x as x when do the min(x, x+1)
        cur_min = x+1 if self.getMin()==None else self.getMin() 
        self.stack.append((x, min(x,cur_min) ))
        
    def pop(self):
        self.stack.pop()
       
    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else None