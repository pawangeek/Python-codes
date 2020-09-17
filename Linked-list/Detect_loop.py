class Node:

    def __init__(self, data):
        self.head = None
        self.data = data

class Linkedlist:

    def __init__(self):
        self.head = None

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def loophash(self):

        temp = self.head
        s = set()

        while temp:

            if temp in s:
                return True
            
            s.add(temp)
            temp = temp.next

        return False

    def floydcycle(self):

        slowptr = self.head
        fastptr = self.head

        # (i) If no cycle : Fastptr reaches end and complexity = O(n)
        # (ii) If cycle : Fastptr: n iterations and Slowptr: k iterations so O(n+k)

        while fastptr and fastptr.next:

            slowptr = slowptr.next
            fastptr = fastptr.next.next

            if fastptr==slowptr:
                return True

        return False