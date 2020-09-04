class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        # If link list is empty
        if not self.head:
            self.push(value)
        else:
            # Get to last node and add new node
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def SortedMerge(llist1, llist2):
    # Create a new Sorted Merge Link List
    sorted_merge_link = LinkList()

    temp1 = llist1.head
    temp2 = llist2.head

    while temp1 or temp2:

        if temp1 and temp1.data < temp2.data:
            sorted_merge_link.append(temp1.data)
            temp1 = temp1.next
        else:
            sorted_merge_link.append(temp2.data)
            temp2 = temp2.next

    return sorted_merge_link


if __name__ == '__main__':
    # Fist Link List
    first_link_list = LinkList()
    first_link_list.append(2)
    first_link_list.append(5)
    first_link_list.append(7)
    first_link_list.append(19)
    first_link_list.append(22)

    # Second Link List
    second_link_list = LinkList()
    second_link_list.append(3)
    second_link_list.append(6)
    second_link_list.append(11)
    second_link_list.append(12)
    second_link_list.append(23)

    new_llist = SortedMerge(first_link_list, second_link_list)
    new_llist.print()