class Node:

    def __init__(self, data):
        self.data = data
        self.head = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, data):
        
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def looplength(self):

        slowptr = self.head
        fastptr = self.head

        while fastptr and fastptr.next:

            # Means loop is there
            if fastptr == slowptr:

                count = 1
                
                # Move slow pointer one step forward otherwise (it's same at that position)
                slowptr = slowptr.next

                while slowptr != fastptr:
                    slowptr = slowptr.next
                    count += 1

                return count

            slowptr = slowptr.next
            fastptr = fastptr.next.next

        return 0

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(1)
    ll.push(4)
    ll.push(8)
    ll.push(6)
    ll.push(2)
    # ll.push(15)
    ll.push(7)

    ll.head.next.next.next.next.next.next = ll.head
    print(ll.looplength()) 