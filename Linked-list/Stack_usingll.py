class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        return (self.head is None)

    def push(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):

        if self.isempty():
            return None

        else:
            popped = self.head
            self.head = self.head.next

            popped.next = None
            return popped.data

    def printlist(self):

        temp = self.head

        while temp:
            print(temp.data, end = ' -> ')
            temp = temp.next

        print(None)


if __name__ == "__main__":

    s = stack()
    s.push(2)
    s.push(4)
    s.push(9)
    s.push(1)

    s.printlist()
    print(s.pop())
    print(s.pop())
    s.printlist()
    s.push(6)
    s.printlist()

    