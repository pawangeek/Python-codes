class Node:

    def __init__(self, data):
        self.data = data
        self.head = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def printlist(self):
        
        temp = self.head

        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

        print()

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def reverse(self):

        prev = None
        curr = self.head

        while curr:

            # Before changing next of current store it
            next = curr.next

            # Now change next of curr node (Actual reverse happens)
            curr.next = prev

            # Move prev and curr move one step forward
            prev = curr
            curr = next 

        self.head = prev   

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(3)
    ll.push(5)
    ll.push(4)
    ll.push(8)

    ll.printlist()
    ll.reverse()
    ll.printlist()