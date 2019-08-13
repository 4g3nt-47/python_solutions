# Traversing a tree using Breath First Search & Depth First Search
# @author: Krrish

#Breadth First Search
class Node(object):

	def __init__(self, value):

		self.value = value

		self.left_child = None

		self.right_child = None

	def assign_left_child(self, left_child):

		self.left_child = left_child

	def assign_right_child(self, right_child):

		self.right_child = right_child

	def get_left_child(self):

		return self.left_child

	def get_right_child(self):

		return self.right_child

	def get_value(self):

		return self.value

	def has_left_child(self):

		if self.left_child != None:

			return True

		return False

	def has_right_child(self):

		if self.right_child != None:

			return True

		return False



def create_node():

	value = int(input("Enter value for node: "))

	new_node = Node(value)

	return new_node

		

# Initialize a list to store all nodes

all_nodes = []

root = create_node() # Create a root node

all_nodes.append(root) # Add the root node to list



def create_tree(current_node):

	option = input("Does node with value " + str(current_node.get_value()) + " have a left child? [Y/n] ")

 			 	

	if option == "y" or option == "Y":

		new_node = create_node()

		current_node.assign_left_child(new_node)

		all_nodes.append(new_node)

		create_tree(new_node)



	option = input("Does node with value " + str(current_node.get_value()) + " have a right child? [Y/n] ")

 			 	

	if option == "y" or option == "Y":

		new_node = create_node()

		current_node.assign_right_child(new_node)

		all_nodes.append(new_node)

		create_tree(new_node)

 		

create_tree(root)



# Breath First Search Tree Traversal for finding a value in tree

def BFS(root, find):

	"""

		Function to find a value using Breath First Search

		Input: root: Root node object

			  find: Integer value to find in the tree

		Output:

			  Prints the path to node in question

			  Returns only None otherwise

	"""

	if root.get_value() == find:

		print("Found the node with value " + str(find) + " using BFS, path for it is: ")

		print (closed_list	)

	else:

		# Exploring current root

		if root.has_left_child() == True:

			open_list.append(root.get_left_child())

		if root.has_right_child() == True:

			open_list.append(root.get_right_child())

		closed_list.append(root.get_value())

		open_list.remove(root)

		

		if len(open_list) != 0:

			BFS(open_list[0], find)

		else:

			return None



# Depth First Search Tree Traversal for finding a value in tree			

def DFS(root, find):

	"""

		Function to find a value using Depth First Search

		Input: root: Root node object

			  find: Integer value to find in the tree

		Output:

			  Prints the path to node in question

			  Returns only None otherwise

	"""

	if root.get_value() == find:

		print ("Found the node with value " + str(find) + " using DFS, path for it is: ")

		print (closed_list	)

		return None

	else:

		# Exploring current root

		closed_list.append(root.get_value())

		open_list.remove(root)

		if root.has_left_child() == True:

			open_list.insert(0, root.get_left_child())

			BFS(open_list[0], find)

		if root.has_right_child() == True:

			open_list.insert(1, root.get_right_child())

			BFS(open_list[0], find)

		



			

find = int(input("\nEnter a value to find: "))



open_list = []

closed_list = []

open_list.append(root)



BFS(root, find)	



open_list = []

closed_list = []

open_list.append(root)



DFS(root, find)
