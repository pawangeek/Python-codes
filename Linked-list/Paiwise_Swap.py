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

    def pairwise(self):

        curr = self.head

        while curr and curr.next:
            curr.data, curr.next.data = curr.next.data, curr.data
            curr = curr.next.next

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(2)
    ll.push(8)
    ll.push(3)
    ll.push(5)
    ll.push(6)
    ll.push(1)

    ll.printlist()
    ll.pairwise()
    ll.printlist()