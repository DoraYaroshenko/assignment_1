#id1:215060922
#name1:anna barski
#username1:annabarski
#id2:
#name2:
#username2:
from enum import Enum

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""

	"""if key and value are None then node is virtual node and its height is -1 and it has no children, otherwise, it is a regular leaf, its children are virtual nodes and its default height is 0"""
	def __init__(self, key, value):
		self.key = key
		if key==None:
			self.value = value
			self.left = None
			self.right = None
			self.parent = None
			self.height=-1
		else:
			self.value = value
			self.left=AVLNode(None, None)
			self.right=AVLNode(None, None)
			self.parent=None
			self.height=0

	def set_left(self,node):
		self.left=node
		node.parent=self
		
	def set_right(self, node):
		self.right=node
		node.parent=self

	def set_height(self, h):
		self.height=h

	def __str__(self):
		st="node with key "+str(self.key)+" height "+str(self.height)
		return st
	
	def is_right_child(self):
		if self.parent==None or self.parent.right!=self:
			return False
		return True

	def is_left_child(self):
		if self.parent==None or self.parent.left!=self:
			return False
		return True
	
	def demote(self):
		self.height=self.height-1

	def promote(self):
		self.height=self.height+1

	class DeleteRebalanceCase(Enum):
		CASE0=0 #node balanced
		CASE1=1
		CASE2_1=21
		CASE2_2=22
		CASE3_1=31
		CASE3_2=32
		CASE4_1=41
		CASE4_2=42
		@staticmethod
		def determine_case(node):
			if (node.BF()==0 and node.height-node.left.height==2):#node is 2,2
				return AVLNode.DeleteRebalanceCase.CASE1
			if (node.BF()==2):#node is 3,1
				if(node.right.BF()==0):#right of node is 1,1
					return AVLNode.DeleteRebalanceCase.CASE2_1
				if(node.right.BF()==-1):#right of node is 1,2
					return AVLNode.DeleteRebalanceCase.CASE4_1
				if(node.right.BF()==1):#right of node is 2,1
					return AVLNode.DeleteRebalanceCase.CASE3_1
			if (node.BF()==-2):#node is 1,3
				if(node.left.BF()==0):#left of node is 1,1
					return AVLNode.DeleteRebalanceCase.CASE2_2
				if(node.left.BF()==-1):
					return AVLNode.DeleteRebalanceCase.CASE4_2
				if(node.left.BF()==1):
					return AVLNode.DeleteRebalanceCase.CASE4_2
			return AVLNode.DeleteRebalanceCase.CASE0
	
	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self==None:
			return False
		if self.height==-1:
			return False
		return True

	def Min(self):
		curr=self
		while(curr.left.is_real_node()==True):
			curr=curr.left
		return curr

	def successor(self):
		if(self.right.is_real_node()==True):
			return self.right.Min()
		curr=self
		next=self.parent
		while(next!=None and curr==next.right):
			curr=next
			next=curr.parent
		return next

	def left_rotate(self):
		child = self.right
		grand = child.left
		child.left = self
		self.right = grand
		self.height = max(height(self.left), height(self.right)) + 1
		child.height = max(height(child.left), height(child.right)) + 1

		return child

	def right_rotate(self):
		child = self.left
		temp = child.right
		child.right = self
		self.left = temp
		self.height = max(height(self.left), height(self.right)) + 1
		child.height = max(height(child.left), height(child.right)) + 1

		return child
	
	def inorder(root):
		if root.is_real_node():
			root.left.inorder()
			print("key: "+str(root.key)+" height:"+str(root.height)+" parent:"+str(root.parent)+"\r\n")
			root.right.inorder()

	def insert(root, node):
		if root.is_real_node()==False:
			node.parent=root.parent
			return node
		if root.key == node.key:
			return root
		
		if root.key < node.key:
			#if root.right.is_real_node()==False:
			#	node.parent=root
			#else:
			root.right = root.right.insert(node)
			root.right.parent=root
		else:
			root.left = root.left.insert(node)
			root.left.parent=root
		return root
			
	def adjust(self):
		if(self.is_real_node()==False):
			return -1
		self.height=max(self.right.adjust(), self.left.adjust())+1
		return self.height

	def BF(self):
		if self.is_real_node()==False:
			return 0
		return self.left.height-self.right.height

	def only_right(self):
		if self.left.is_real_node()==False and self.right.is_real_node()==True:
			return True
		return False

	def only_left(self):
		if self.right.is_real_node()==False and self.left.is_real_node()==True:
			return True
		return False

	def is_leaf(self):
		if(self.left.is_real_node()==False and self.right.is_real_node()==False):
			return True
		return False

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root =AVLNode(None, None)

	def set_root(self, r):
		self.root=r
	
	def is_empty(self):
		if self.root.is_real_node()==False:
			return True
		return False

	def is_root(self, node):
		if(self.root==node):
			return True
		return False

	def parent_tree(self,node):
		ptree=AVLTree()
		ptree.root=node.parent
		return ptree

	def rotate_right(self, node: AVLNode):
		is_right = node.is_right_child()
		new_root = node.left

		new_root.right.parent = node
		node.left = new_root.right
		new_root.right = node

		new_root.parent = node.parent
		node.parent = new_root
		if new_root.parent is None:
			self.root = new_root
			return
		if is_right:
			new_root.parent.right = new_root
		else:
			new_root.parent.left = new_root
		return

	def rotate_left(self, node: AVLNode):
		is_left = node.is_left_child()
		new_root = node.right

		new_root.left.parent = node
		node.right = new_root.left
		new_root.left = node

		new_root.parent = node.parent
		node.parent = new_root
		if new_root.parent is None:
			self.root = new_root
			return
		if is_left:
			new_root.parent.left = new_root
		else:
			new_root.parent.right = new_root
		return
	"""
	method for creation of the left subtree of the current tree
	@rtype: AVLTree
	@returns: the left subtree of the current tree
	time complexity O(1)
	"""
	def left_subtree(self):
		ltree=AVLTree()
		ltree.root=self.root.left
		return ltree
	"""
	method for creation of the right subtree of the current tree
	@rtype: AVLTree
	@returns: the right subtree of the current tree
	time complexity O(1)
	"""
	def right_subtree(self):
		rtree=AVLTree()
		rtree.root=self.root.right
		return rtree
	"""
	envelope function for search
	@type k: int
	@param k: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search_envelope(self, k, path):
		if(self.root.is_real_node()==False):
			return (None, path+1)
		if self.root.key==k:
			return (self.root, path+1)
		if self.root.key>k:
			return self.left_subtree().search_envelope(k, path+1)
		return self.right_subtree().search_envelope(k, path+1)
	
	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	"""
	time complexity is O(log(n)) since in the worst case, the desired node is a leaf, at depth log(n) since this is an AVL tree,
	and in each stage of the recursion, time complexity is at most 4=O(1)
	"""

	def search(self, key):
		return self.search_envelope(key, 0)
		

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""

	"""
	time complexity is O(log(n)), since the first and second loops will have at most log(n) iterations of O(1) complexity
	and then we call on a function of time complexity O(log(n))
	hence the total running time in the worst case is 3log(n)=O(log(n))
	"""
	def finger_search(self, key):
		curr=self.root
		path=0
		while(curr.right.is_real_node()!=False):
			curr=curr.right
		
		while (curr.key>key and curr.parent!=None and curr.parent.key>=key):
			path=path+1
			curr=curr.parent
		print(curr)
		ltree=AVLTree()
		ltree.root=curr
		return ltree.search_envelope(key, path+1)


	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def insert(self, key, val):
		return None, -1, -1


	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def finger_insert(self, key, val):
		return None, -1, -1


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""

	def delete(self, node):
		if node.is_real_node()==False:
			return
		if (node.only_right()):#if node only has a right child, suitable to if node is a leaf
			newPointer=node.right
			if(self.is_root(node)):
				self.root=newPointer
			elif(node.is_right_child()):#if node is the right child of its parent
				node.parent.right=newPointer
			else:
				node.parent.left=newPointer
			newPointer.parent=node.parent
			pivot=newPointer

		elif (node.only_left()):#if node has only left child
			newPointer=node.left
			if(self.is_root(node)):
				self.root=newPointer
			elif(node.is_right_child()):#if node is the right child of its parent
				node.parent.right=newPointer
			else:
				node.parent.left=newPointer
			newPointer.parent=node.parent
			pivot=newPointer

#if node has two children, we will replace it with its successor and delete its successor which must be a leaf or unary
		else:
			newPointer=node.successor()
			tempKey=node.key
			tempVal=node.value
			node.key=newPointer.key
			node.value=newPointer.value
			newPointer.key=tempKey
			newPointer.value=tempVal
			self.delete(newPointer)
			pivot=node
		currTree=AVLTree()
		currTree.root=pivot
		currTree.balance_post_deletion()
			

	def balance_post_deletion(self):
		pivot=self.root
		sdafjhkjasdd
		if (pivot.is_real_node()==True):
			case=AVLNode.DeleteRebalanceCase.determine_case(pivot)
			if (case==AVLNode.DeleteRebalanceCase(0)):#if node is balanced
				print("balanced "+str(pivot))
			if(case==AVLNode.DeleteRebalanceCase(1)):
				pivot.demote()
				if pivot.parent!=None:
					ptree=self.parent_tree(pivot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(21)):
				newRoot=pivot.right
				newRoot.promote()
				pivot.demote()
				self.rotate_left(pivot)
				if newRoot.parent!=None:
					ptree=self.parent_tree(newRoot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(22)):
				newRoot=pivot.left
				newRoot.promote()
				pivot.demote()
				self.rotate_right(pivot)
				if newRoot.parent!=None:
					ptree=self.parent_tree(newRoot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(31)):
				pivot.demote()
				pivot.demote()
				self.rotate_left()
				if pivot.parent!=None:
					ptree=self.parent_tree(pivot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(32)):
				pivot.demote()
				pivot.demote()
				self.rotate_right()
				if pivot.parent!=None:
					ptree=self.parent_tree(pivot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(41)):
				newRoot=pivot.right.left
				newRight=pivot.right
				pivot.demote()
				pivot.demote()
				newRight.demote()
				newRoot.promote()
				self.rotate_right(newRight)
				self.rotate_left(pivot)
				if newRoot.parent!=None:
					ptree=self.parent_tree(newRoot)
					ptree.balance_post_deletion()
			elif (case==AVLNode.DeleteRebalanceCase(42)):
				newRoot=pivot.left.right
				newLeft=pivot.left
				pivot.demote()
				pivot.demote()
				newLeft.demote()
				newRoot.promote()
				self.rotate_left(newRight)
				self.rotate_right(pivot)
				if newRoot.parent!=None:
					ptree=self.parent_tree(newRoot)
					ptree.balance_post_deletion()


	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2, key, val):
		return


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None, None

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		if(self.is_empty()):
			return None
		if(self.root.only_left() or self.root.is_leaf()):
			return self.root
		return max_node(self.right_subtree())

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return -1	


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root


