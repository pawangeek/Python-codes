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

    def addnos(self, first, second):

        first = self.rev(first.head)
        second = self.rev(second.head)
        temp = None
        prev = None
        carry = 0

        while first or second :

            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            sm = fdata + sdata + carry
            carry = 1 if sm>=10 else 0

            print(sm, carry)
            temp = Node(sm%10)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None: 
                first = first.next
            if second is not None: 
                second = second.next

        if carry!=0:
            temp.next = Node(carry)

    def rev(self, head):

        prev = None
        curr = head

        while curr:

            # Before changing next of current store it
            next = curr.next
            curr.next = prev

            # Move prev and curr move one step forward
            prev = curr
            curr = next 

        return prev   

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(3)
    ll.push(5)
    ll.push(4)
    ll.push(8)

    ll2 = Linkedlist()
    ll2.push(3)
    ll2.push(5)
    ll2.push(4)
    ll2.push(8)

    ll.printlist()
    ll2.printlist()

    llist = Linkedlist()
    llist.addnos(ll.head, ll2.head)
    llist.printlist()