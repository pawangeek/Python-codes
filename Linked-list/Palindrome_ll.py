class Node:

    def __init__ (self, data):
        self.head = None
        self.data = data

class Linkedlint:

    def __init__ (self):
        self.head = None

    def push(self, data):
        
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

        print()

    def palindromell(self):

        slow = self.head
        fast = self.head
        rev = None

        # Need to reverse our first half linked list
        while (fast and fast.next):

            fast = fast.next.next

            next = slow.next
            slow.next = rev

            rev = slow
            slow = next

        # Move one step forward to cross the mid (in case of odd lenght)
        # Slow is at mid one so we move one step
        if fast:
            slow = slow.next

        while (rev and slow):
            
            # Check data one by one 
            if rev.data != slow.data:
                return False

            # increment both rev and slow
            rev = rev.next
            slow = slow.next

        return True

if __name__ == "__main__":

    ll = Linkedlint()
    ll.push(1)
    ll.push(2) 
    ll.push(2)
    ll.push(1)

    ll.printlist()
    print(ll.palindromell())       