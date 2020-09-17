class Node:
    def __init__ (self, data):
        self.next = None
        self.data = data

    
class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self, heads):

        temp = heads

        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next

        print(None)

    def reversegroups(self, head, k):

        if not head:
            return 

        curr, prev = head, None
        count = 0

        while curr and count<k:

            count += 1

            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        head.next = self.reversegroups(curr, k)
        return prev

    def rev(self, k):
        head = self.reversegroups(self.head, k)
        self.printlist(head)

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(2)
    ll.push(8)
    ll.push(3)
    ll.push(5)
    ll.push(6)
    ll.push(1)

    ll.printlist(ll.head)
    ll.rev(4)