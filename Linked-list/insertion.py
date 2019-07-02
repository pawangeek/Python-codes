class Node: 
	def __init__ (self,data): # Function to initialize node object
		self.data=data  	  # Assign data
		self.next=None 		  # Initialize next as null

class LinkedList:
	def __init__ (self):	  # Function to initialize the Linked List object
		self.head=None

	def push(self,new_data):  # Function to insert new node at beginning
		new_node = Node(new_data)	# Allocate the node and put in data
		new_node.next = self.head	# Make next of new node as head
		self.head=new_node			# Move head to point to new node


	def insertafter(self,prev_node,new_data):
		if prev_node is None:
			print("Blank")
			return

		new_node = Node(new_data)   	# create new node and put in data
		new_node.next = prev_node.next	# make next of new node as next of prev node
		prev_node.next = new_node		# make next of prev node as new_node

	def append(self,new_data):
		new_node = Node(new_data) # create new node, put in data, set next node

		if self.head is None: # If linked list is empty make new node as head
			self.head=new_node
			return

		last=self.head 		  # Else traverse till last node
		while (last.next):
			last=last.next

		last.next=new_node 	  # change next of last node

	def printlist(self): 
		temp=self.head
		while (temp):
			print (temp.data)
			temp=temp.next

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(7);
	llist.append(4);
	llist.push(1);
	llist.insertafter(llist.head.next,9)
	llist.printlist()