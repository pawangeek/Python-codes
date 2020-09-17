class Node:
    def __init__ (self, data):
        self.head = None
        self.data = data

class Linkedlist:

    def __init__ (self):
        self.head = None

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end = " ")
            temp = temp.next

        print()

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def hashdups(self):

        prev = None
        curr = self.head

        s = set()

        while curr:

            # If curr.data is new and not in our set simply add it to set
            # And move prev and curr one step forward

            if curr.data not in s:
                s.add(curr.data)
                prev = curr
                curr = curr.next

            # Else assign next of curr to next of prev 
            # (in order to remove curr)

            else:
                prev.next = curr.next
                curr = curr.next

if __name__ == '__main__':

    ll = Linkedlist()
    ll.push(7)
    ll.push(7)
    ll.push(1)
    ll.push(7)
    ll.push(7)

    ll.printlist()
    ll.hashdups()
    ll.printlist()