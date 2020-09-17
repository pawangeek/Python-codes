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

    # (i) Calculate length of linked list
    # (ii) Print length-n+1 in another traverse

    def nthbylength(self, n):

        curr, temp = self.head, self.head
        length, count = 0, 0

        while curr:
            length += 1
            curr = curr.next

        if n>length:
            return -1

        while temp:
            count += 1

            if count == length-n+1:
                return temp.data
            
            temp = temp.next

    # (i) Move ref pointer to n nodes from head
    # (ii) Now move both pointers one by one till the ref pointer reach to end
    
    def twopointer(self, n):

        main, ref = self.head, self.head
        count = 0

        while count<n:

            if ref is None:
                return -1

            ref = ref.next
            count += 1

        while ref:

            main = main.next
            ref = ref.next

        return main.data

if __name__ == '__main__':

    ll = Linkedlist()
    ll.push(3)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(9)

    ll.printlist()
    print(ll.nthbylength(8))
    print(ll.twopointer(8))