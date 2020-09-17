class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, data):

        temp = Node(data)

        # If queue is empty new node is rear and front both
        if self.rear is None:
            self.front = temp
            self.rear = temp

        # Add new node at end of queue and change rear
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):

        # if queue is empty return Null
        if self.isempty():
            return None

        # Store prev front and move one forward
        temp = self.front
        self.front = temp.next

        # if front becomes empty after dequeue op
        # make rear empty too
        if self.front is None:
            self.rear = None

    def printqueue(self):

        temp = self.front

        while temp:
            print(temp.data, end = ' -> ')
            temp = temp.next

        print(None)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(8)
    q.enqueue(5)
    q.enqueue(6)
    q.printqueue()

    q.dequeue()
    q.dequeue()

    q.printqueue()
    q.enqueue(1)

    q.printqueue() 
        


