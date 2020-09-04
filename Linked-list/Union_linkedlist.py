# Approach 1 : SImple traversal

def findIntersection(head1, head2):

    s = set()
    l = linkedList()
    
    while (head2):
        s.add(head2.data)
        head2 = head2.next
    
    while (head1):
        
        if (head1.data in s):
            l.insert(head1.data)
            
        head1 = head1.next

def findIntersection(head1, head2): 

    l = linkedList()
    curr = head2

    while (head1):
        
        head2 = curr
        
        while (head2):
            if head1.data == head2.data:
                l.insert(head1.data)
                
            head2 = head2.next
                    
        head1 = head1.next
            
    return l.head