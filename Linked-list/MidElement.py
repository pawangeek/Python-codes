class Node:

    def __init__(self, data):
        self.data = data
        self.head = None

class Linkedlist:

    def __init__(self):
        self.head = None

    # Two pointers approach
    def printmid(self):
        
        # We assign a slow pointer(+1) and fast pointer(+2)
        # And get our answer when fastpointer is at end

        slowptr = self.head
        fastptr = self.head

        if self.head is not None:
            while fastptr and fastptr.next:
                slowptr = slowptr.next
                fastptr = fastptr.next.next

        print(slowptr.data)

    # Two traverse approach
    def twotraverse(self):

        temp, res = self.head, self.head
        count, i = 0, 0 

        while temp:
            count+=1
            temp = temp.next

        while i!=count//2:
            i+=1
            res = res.next
            
        print(res.data)     

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

if __name__ == '__main__':
    ll = Linkedlist()
    ll.push(1)
    ll.push(4)
    ll.push(8)
    ll.push(6)
    ll.push(2)
    # ll.push(15)
    ll.push(7)

    ll.printmid()
    ll.twotraverse()
    ll.printlist()
    