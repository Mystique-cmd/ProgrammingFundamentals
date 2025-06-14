import sys

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None #Points to the next node
class LinkedList:
	def __init__(self):
		self.head = None #initially empty
	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_end(self,data):
		new_node = Node(data)
		if not self.head: #if list is empty
			self.head = new_node
			return
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = new_node

	def delete_node(self,key):
		temp = self.head
		if temp and temp.data == key: #if the head is key
			self.head = temp.next
			temp = None
			return
		prev = None
		while temp and temp.data != key:
			prev = temp
			temp = temp.next
		if temp is None:
			return
		prev.next = temp.next
		temp = None
	
	def search(self,key):
		temp = self.head
		index = 0
		while temp:
			if temp.data == key:
				return f"Value {key} found at index {index}"
			temp = temp.next
			index += 1
		return f" Value {key} not found"

	def display(self):
		temp = self.head
		while temp:
			print (temp.data, end="->")
			temp = temp.next
		print("None")

ll = LinkedList()

while True:
	print ("\nChoose an operation:")
	print ("1. Insert at the beginning")
	print ("2. Insert at the end")
	print ("3. Delete a value")
	print ("4. Search for a value")
	print ("5. Display the linked list")
	print ("6. Exit")
	choice = input ("Enter your choice (1-6):")
	if choice == "1":
		value = input("Enter the value to insert at the beginning:")
		ll.insert_at_beginning(value)
	elif choice == "2":
		value = input ( " Enter the value to insert at the end:")
		ll.insert_at_end(value)
	elif choice == "3":
		value = input("Enter the value to delete:")
		ll.delete_node(value)
	elif choice == "4":
		value = input("Enter the value to search:")
		print (ll.search(value))
	elif choice == "5":
		ll.display()
	elif choice == "6":
		print ("Exiting program ... Goodbye!")
		sys.exit() #termminate execution
else:
	print ( " Invalid choice, try again")


