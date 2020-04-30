# @Date:   2020-04-16T16:43:52+05:30
# @Last modified time: 2020-04-30T17:10:35+05:30

# Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

[1,2,3,4,5]

slow = head
fast = head.next

# Approach 1 : Fast and slow pointer

# When traversing list slow, make another pointer fast that traverses twice as fast.
# When fast reaches the end of the list, slow must be in the middle.

# slow goes one step further
# fast goes one step further

while fast:
    slow = slow.next
    fast = fast.next
    if  not fast:
        break
    fast = fast.next

print(slow)

# Approach 2 : Make array

# Put every node into an array A in order. Then the middle node is just A[A.length // 2]
# since we can retrieve each node by index.

A = [head]
while A[-1].next:
    A.append(A[-1].next)

print (A[len(A) / 2])
