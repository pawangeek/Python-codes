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

    def zigzaglist(self):

        curr = self.head
        flag = True

        while (curr.next):

            # If we have a situation like A > B > C where A, B and C are consecutive Nodes 
            # in list we get A > B < C by swapping B and C  
            if flag:
                if curr.data>curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data

            # If we have a situation like A < B < C where A, B and C are consecutive Nodes in list we 
            # get A < C > B by swapping B and C  
            else:
                if curr.data<curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data

            flag = False if flag else True
            curr = curr.next

if __name__ == '__main__':

    ll = Linkedlist()
    ll.push(3)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(9)

    ll.printlist()
    ll.zigzaglist()
    ll.printlist()