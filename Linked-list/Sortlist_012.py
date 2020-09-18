class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class Linkedlist:

    def __init__ (self):
        self.head = None

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data , end=' -> ')
            temp = temp.next

        print(None)

    def sortlist(self):

        count = [0]*3
        temp = self.head

        # Create count of every node
        while temp:
            count[temp.data]+=1
            temp = temp.next

        i = 0
        ptr = self.head

        while ptr:

            # If that no. count > 0 put that in list and reduce counter
            if count[i]>0:
                ptr.data = i
                count[i] -= 1

                ptr = ptr.next
    
            # If counter tends to zero than incremment i
            else:
                i += 1

if __name__ == "__main__":
    ll = Linkedlist()

    ll.push(1)
    ll.push(0)
    ll.push(1)
    ll.push(2)
    ll.push(1)

    ll.printlist()
    ll.sortlist()
    ll.printlist()