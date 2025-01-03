#id1:215060922
#name1:anna barski
#username1:annabarski
#id2:
#name2:
#username2:
from enum import Enum

"""A class represnting a node in an AVL tree"""

class RebalanceCase(Enum):
    CASE_TERMINAL = 0
    CASE_DIFF_0_1_OR_1_0 = 1
    CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_2 = 2
    CASE_PARENT_DIFF_2_0_CHILD_DIFF_2_1 = 3
    CASE_PARENT_DIFF_0_2_CHILD_DIFF_2_1 = 4
    CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_2 = 5
    CASE_DIFF_2_2 = 6
    CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_1 = 7
    CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_1 = 10

    @classmethod
    def from_height_diffs(cls, parent_left_diff, parent_right_diff, node_left_diff, node_right_diff):
        if (parent_left_diff == 1 and parent_right_diff == 1) or (parent_left_diff == 2 and parent_right_diff == 1) or (
                parent_left_diff == 1 and parent_right_diff == 2):
            return RebalanceCase.CASE_TERMINAL
        elif (parent_left_diff == 0 and parent_right_diff == 1) or (parent_left_diff == 1 and parent_right_diff == 0):
            return RebalanceCase.CASE_DIFF_0_1_OR_1_0
        elif (parent_left_diff == 0 and parent_right_diff == 2) and (
                node_left_diff == 1 and node_right_diff == 2):
            return RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_2
        elif (parent_left_diff == 2 and parent_right_diff == 0) and (
                node_left_diff == 2 and node_right_diff == 1):
            return RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_2_1
        elif (parent_left_diff == 0 and parent_right_diff == 2) and (
                node_left_diff == 2 and node_right_diff == 1):
            return RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_2_1
        elif (parent_left_diff == 2 and parent_right_diff == 0) and (
                node_left_diff == 1 and node_right_diff == 2):
            return RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_2
        elif parent_left_diff == 2 and parent_right_diff == 2:
            return RebalanceCase.CASE_DIFF_2_2
        elif (parent_left_diff == 2 and parent_right_diff == 0) and (node_left_diff == 1 and node_right_diff == 1):
            return RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_1
        elif (parent_left_diff == 0 and parent_right_diff == 2) and (node_left_diff == 1 and node_right_diff == 1):
            return RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_1
        else:
            raise Exception


class JoiningRebalanceCase(Enum):
    CASE0 = 0
    CASE1 = 1
    CASE2 = 2

    @classmethod
    def from_joining_height_diffs(cls, tr_with_bigger_keys_height, tr_with_smaller_keys_height):
        if tr_with_smaller_keys_height == tr_with_bigger_keys_height:
            return JoiningRebalanceCase.CASE0
        elif tr_with_bigger_keys_height > tr_with_smaller_keys_height:
            return JoiningRebalanceCase.CASE1
        else:
            return JoiningRebalanceCase.CASE2



class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""

	"""if key and value are None then node is virtual node and its height is -1 and it has no children, otherwise, it is a regular leaf, its children are virtual nodes and its default height is 0"""
	def __init__(self, key, value, height=-1, parent=None):
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
	
	def is_leaf(self):
		return (self.left is None or not self.left.is_real_node()) and (
				self.right is None or not self.right.is_real_node())

	def is_root(self):
		return self.parent is None

	def is_right_child(self):
		if self.parent is not None and self.parent.right is not None and self.parent.right is self:
			return True
		return False

	def is_left_child(self):
		if self.parent is not None and self.parent.left is not None and self.parent.left is self:
			return True
		return False

	
	def promote_height(self, delta=1):
		self.height += delta
		return delta

	def demote_height(self, delta=1):
		self.height -= delta


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
	def __init__(self, root=None):
		self.root =root

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
	@staticmethod
	def create_valid_node(key, val, parent=None):
		new_node = AVLNode(key, val, 0)
		new_node.left = AVLNode(None, None, parent=new_node)
		new_node.right = AVLNode(None, None, parent=new_node)
		new_node.parent = parent
		return new_node

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

	def left_right_double_rotation(self, node):
		AVLTree.rotate_left(self, node.left)
		AVLTree.rotate_right(self, node)

	def right_left_double_rotation(self, node):
		AVLTree.rotate_right(self, node.right)
		AVLTree.rotate_left(self, node)

	def rebalance_after_insertion_or_join(self, node):
		promotions = 0
		parent = node.parent
		promotions += node.promote_height()
		if parent is None:
			return promotions

		parent_left_diff = parent.height - parent.left.height
		parent_right_diff = parent.height - parent.right.height
		node_left_diff = node.height - node.left.height
		node_right_diff = node.height - node.right.height
		rebalance_case = RebalanceCase.from_height_diffs(
			parent_left_diff=parent_left_diff, parent_right_diff=parent_right_diff,
			node_left_diff=node_left_diff, node_right_diff=node_right_diff
		)

		if rebalance_case==RebalanceCase.CASE_TERMINAL:
			pass
		elif rebalance_case==RebalanceCase.CASE_DIFF_0_1_OR_1_0:
			promotions += self.rebalance_after_insertion_or_join(parent)
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_2:
			self.rotate_right(parent)
			parent.demote_height()
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_2_1:
			self.rotate_left(parent)
			parent.demote_height()
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_2_1:
			right = node.right
			self.left_right_double_rotation(parent)
			node.demote_height()
			parent.demote_height()
			right.promote_height()
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_2:
			left = node.left
			self.right_left_double_rotation(parent)
			node.demote_height()
			parent.demote_height()
			left.promote_height()
		elif rebalance_case==RebalanceCase.CASE_DIFF_2_2:
			parent.demote_height()
			promotions += self.rebalance_after_insertion_or_join(parent)
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_1:
			self.rotate_left(parent)
			promotions += self.rebalance_after_insertion_or_join(node)
		elif rebalance_case==RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_1:
			self.rotate_right(parent)
			promotions += self.rebalance_after_insertion_or_join(node)
		return promotions

	def find_insertion_place(self, key):
		return self.search_logic(key, 0)

	def insert(self, key, val, finger=False):
		node, path_len_counter = self.find_insertion_place(
			key) if not finger else self.find_finger_insertion_place(key)
		new_node = self.create_valid_node(key, val, node.parent)
		if (self.root==None or self.root.is_real_node()==False):
			self.root=new_node
			return
		parent_is_leaf = node.parent.is_leaf()
		if node.is_right_child():
			node.parent.right = new_node
		else:
			node.parent.left = new_node

		promotions = 0
		if new_node.parent.is_root() and parent_is_leaf:
			new_node.parent.promote_height()
			promotions += 1
		elif not parent_is_leaf:
			pass
		else:
			promotions = self.rebalance_after_insertion_or_join(new_node.parent)
		return new_node, path_len_counter, promotions



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
	def finger_search_logic(self, key):
		curr = self.max_node()
		if key > curr.key:
			return curr.right, 1
		path = 0
		while curr.key > key and curr.parent is not None and curr.parent.key >= key:
			path = path + 1
			curr = curr.parent
		if curr.key == key:
			return curr, path
		if curr.left.is_real_node():
			ltree = AVLTree()
			ltree.root = curr.left
			return ltree.search_logic(key, path + 1)
		return curr.left, path

	def search_logic(self, k, path):
		if not self.root.is_real_node() or self.root.key == k:
			return self.root, path
		if self.root.key > k:
			return self.left_subtree().search_logic(k, path + 1)
		return self.right_subtree().search_logic(k, path + 1)

	def find_finger_insertion_place(self, key):
		return self.finger_search_logic(key)

	def finger_insert(self, key, val):
		return self.insert(key, val, True)

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
	def find_joining_point(self, h, is_right):
		node = self.root
		while node.height > h:
			if is_right:
				node = node.right
			else:
				node = node.left
		return node

	def join_case0(self, joining_node, tree_with_bigger_keys, tree_with_smaller_keys):
		joining_node.right = tree_with_bigger_keys.root
		tree_with_bigger_keys.root.parent = joining_node
		joining_node.left = tree_with_smaller_keys.root
		tree_with_smaller_keys.root.parent = joining_node
		self.root = joining_node
		joining_node.promote_height()

	def join_case1(self, joining_node, taller_tree, shorter_tree):
		joining_point = taller_tree.find_joining_point(shorter_tree.root.height, False)
		joining_node.parent = joining_point.parent
		joining_node.right = joining_point
		joining_point.parent.left = joining_node
		joining_point.parent = joining_node
		joining_node.left = shorter_tree.root
		shorter_tree.root.parent = joining_node
		self.root = taller_tree.root
		self.rebalance_after_insertion_or_join(joining_node)

	def join_case2(self, joining_node, taller_tree, shorter_tree):
		joining_point = taller_tree.find_joining_point(shorter_tree.root.height, True)
		joining_node.parent = joining_point.parent
		joining_node.left = joining_point
		joining_point.parent.right = joining_node
		joining_point.parent = joining_node
		joining_node.right = shorter_tree.root
		shorter_tree.root.parent = joining_node
		self.root = taller_tree.root
		self.rebalance_after_insertion_or_join(joining_node)

	def join(self, tree2, key, val):
		tree2_has_bigger_keys = tree2.root.key > self.root.key
		tree_with_bigger_keys = tree2 if tree2_has_bigger_keys else self
		tree_with_smaller_keys = self if tree2_has_bigger_keys else tree2
		taller_tree = self if self.root.height > tree2.root.height else tree2
		shorter_tree = tree2 if self.root.height > tree2.root.height else self
		joining_case = JoiningRebalanceCase.from_joining_height_diffs(tree_with_bigger_keys.root.height,
																	  tree_with_smaller_keys.root.height)
		joining_node = self.create_valid_node(key=key, val=val)
		joining_node.height = shorter_tree.root.height
		if joining_case==JoiningRebalanceCase.CASE0:
			self.join_case0(joining_node, tree_with_bigger_keys, tree_with_smaller_keys)
		elif joining_case==JoiningRebalanceCase.CASE1:
			self.join_case1(joining_node, taller_tree, shorter_tree)
		elif joining_case==JoiningRebalanceCase.CASE2:
			self.join_case2(joining_node, taller_tree, shorter_tree)
			
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
		currNode=self.root
		treeLess=AVLTree()
		treeMore=AVLTree()
		inTree=False
		while(currNode.is_real_node()):
			if(currNode.key>node.key):
				currNode=currNode.left
			elif(currNode.key<node.key):
				currNode=currNode.right
			else:
				inTree=True
				break
		if(inTree):
			currNode.right_subtree().join(treeMore, currNode.right.key, currNode.right.value)
			currNode.left_subtree().join(treeLess, currNode.left.key, currNode.left.value)
		while(currNode.parent!=None):
			isRight=currNode.is_right_child()
			currNode=currNode.parent
			if(isRight):
				currNode.left_subtree().join(treeLess, currNode.key, currNode.value)
			else:
				currNode.right_subtree().join(treeMore, currNode.key, currNode.value)

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		if not self.root.is_real_node():
			return []
		root_tup = (self.root.key, self.root.value)
		if self.root.is_leaf():
			return [root_tup]
		left_tree = AVLTree(self.root.left)
		right_tree = AVLTree(self.root.right)
		return left_tree.avl_to_array() + [root_tup] + right_tree.avl_to_array()


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


