class Node:
    def __init__ (self, data):
        self.head = None
        self.data = data

    
class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next

        print(None)

    def rotate(self, k):

        curr = self.head
        prev = None

        for _ in range(k):

            prev = curr
            curr = curr.next

        # if length == k then simply return original one
        if curr is None:
            return

        rece = curr
        prev.next = None

        while curr.next:
            curr = curr.next

        curr.next = self.head
        self.head = rece

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(2)
    ll.push(8)
    ll.push(3)
    ll.push(5)
    ll.push(6)
    ll.push(1)

    ll.printlist()
    ll.rotate(6)
    ll.printlist()