# Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

[1,2,3,4,5]

slow = head
fast = head.next
        
# slow goes one step further
# fast goes one step further

while fast:
    slow = slow.next
    fast = fast.next
    if  not fast:
        break
    fast = fast.next
            
print(slow)