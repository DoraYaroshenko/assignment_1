AVL TREE INPLEMENTATION PROJECT

Anna Barski, Dora Yaroshenko

This application implements AVL trees and give the user the ability to look for a node in the tree, insert nodes, delete nodes, split and join AVL trees. The project is written in python.

The project implements two major classes: AVLNode, a class that represents a node in AVL tree, and AVLTree, representing the whole tree.

AVLNode:

The constructor of AVLNode gets the following parameters (height and parent have default values -1 and None accordingly):

    @type key: int
    
    @param key: key of your node
    
    @type value: string
    
    @param value: data of your node
    
    @type height: int
    
    @param height: height of your node
    
    @type parent: AVLNode
    
    @param parent: the parent of your node

The class implements the following methods:

    def is_real_node(self):
    the method returns whether self is not a virtual node
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    Complexity O(1)
    
    def balance_factor(self):
    returns the balance factor of the node
    @rtype: int
    @returns: the difference between the heights of node and its left child minus the difference between the heights of
    node and its right child
    Complexity O(1)

    def has_only_right_child(self):
    returns whether node has only right child, and doesn't have a left one
    @rtype: boolean
    @returns: True if node has only right child, False otherwise
    Complexity O(1)

    def has_only_left_child(self):
    returns whether node has only left child, and doesn't have a right one
    @rtype: boolean
    @returns: True if node has only left child, False otherwise
    Complexity O(1)

    def promote_height(self, delta=1):
    the method promotes a height of a given node by delta (delta has a default value 1)
    @type delta: int
    @param delta: the value added to the height of the node
    @rtype: int
    @returns: the number of promotions made
    Complexity O(1)

    def demote_height(self, delta=1):
    the method demotes a height of a given node by delta
    @type delta: int
    @param delta: the value removed from the height of the node
    Complexity O(1)

    def is_leaf(self):
    returns whether the node is a leaf of the tree
    @rtype: boolean
    @returns: True if the node is a leaf, False otherwise
    Complexity O(1)

    def is_root(self):
    returns whether the node is a root of a tree
    @rtype: boolean
    @returns: True if the node is a root, False otherwise
    Complexity O(1)

    def is_right_child(self):
    returns whether the node is the right child of its parent
    @rtype: boolean
    @returns: True if the node is a right child, False otherwise
    Complexity O(1)

    def is_left_child(self):
    returns whether the node is the left child of its parent
    @rtype: boolean
    @returns: True if the node is a left child, False otherwise
    Complexity O(1)

AVLTree:

The constructor of AVLTree has a parameter root with default value None:

    @type root: AVLNode
    @param root: a future root of the tree

The class implements the folliwing methods:

    def successor(self, node):
    a method that returns a successor of a given node in the tree, implemented the way it was described in class
    @type node: AVLNode
    @param node: a node whose successor we need to find
    @rtype: AVLNode
    @returns: the successor
    Complexity O(logn), because the maximal amount of steps is the height of the tree

    def parent_tree(node):
    the method creates a tree whose root is the parent of a given node
    @type node: AVLNode
    @param node: a node whose parent will be a root of the created tree
    @rtype: AVLTree
    @returns: a tree whose root is the parent of a given node
    Complexity O(1)

    def left_subtree(self):
    method for creation of the left subtree of the current tree
    @rtype: AVLTree
    @returns: the left subtree of the current tree
    time complexity O(1)

    def right_subtree(self):
    method for creation of the right subtree of the current tree
    @rtype: AVLTree
    @returns: the right subtree of the current tree
    time complexity O(1)

    def search_logic(self, k, path):
    function implementing search algorithm the way it was described in class in a recursive way
    @type k: int
    @param k: a key to be searched
    @type path: int
    @param path: the length of the path from the root to a given node
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to the key
    (or the node in which place the node with key k would be placed in the tree if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    Complexity O(logn), because the maximal amount of steps during walking on the tree is its height

    def search(self, key):
    searches for a node in the dictionary corresponding to the key (starting at the root)
    uses search_logic method to perform the search        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    Complexity O(logn), because search uses search_logic

    def finger_search_logic(self, key):
    searches for a node in the dictionary corresponding to the key, starting at the max
    implements the algorithm we have seen in class
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or the node in which place the node with key k
    would be placed in the tree if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    time complexity is O(log(n)), since the first and second loops will have at most log(n) iterations of O(1) complexity
    and then we call on a function of time complexity O(log(n))
    hence the total running time in the worst case is 3log(n)=O(log(n))

    def finger_search(self, key):
    searches for a node in the dictionary corresponding to the key, starting at the max
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    time complexity is O(log(n)), since it uses finger_search logic

    def create_valid_node(key, val, parent=None):
    the method creates a valid node for the tree
    @type key: int
    @param key: the key of the node we create
    @type val: int
    @param: the value of the node we create
    @type parent: AVLNode
    @param parent: the parent of the node we create. Has a default value None
    @rtype: AVLNode
    @returns: the new node
    Complexity O(1)

    def rotate_right(self, node: AVLNode):
    the method rotates right the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant

    def rotate_left(self, node: AVLNode):
    the method rotates left the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant

    def left_right_double_rotation(self, node):
    the method performs double rotation left and then right on the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant

    def right_left_double_rotation(self, node):
    the method performs double rotation right and then left on the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant

    def rebalance_after_insertion_or_join(self, node):
    the method rebalances the tree after inserting a node or joining two trees starting from a given node
    @type node: AVLNode
    @param node: the node we start to rebalance from
    @rtype: int
    @returns: the number of height promotions made
    Complexity O(logn), because we walk from the node to the root by the maximum amount of steps equal
    to the height of the tree, and we perform maximum 2 rotations, whose complexity is constant

    def find_insertion_place(self, key):
    finds a place to insert a node in the tree
    @type key: int
    @param key: a key of the node we want to add to the tree
    @rtype: (AVLNode, int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or the node in which place the node with key k
    would be placed in the tree if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    Complexity O(logn), because it uses search_logic method

    def insert(self, key, val, finger=False):
    inserts a new node into the dictionary with corresponding key and value (starting at the root)
    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @type finger: boolean
    @param finger: if True we perform finger search to find the place to insert the node,
    otherwise we search from the node
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    Complexity O(logn), because finding the place to insert takes O(logn) at most, inserting time is constant,
    and rebalancing complexity is O(logn)

    def find_finger_insertion_place(self, key):
    finds a place to insert a node in the tree, starting from the max
    @type key: int
    @param key: a key of the node we want to add to the tree
    @rtype: (AVLNode, int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or the node in which place the node with key k
    would be placed in the tree if not found), and e is the number of edges on the path between the starting node and
    ending node+1.
    Complexity O(logn), because it uses finger_search_logic method

    def finger_insert(self, key, val):
    inserts a new node into the dictionary with corresponding key and value, starting at the max
    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    Complexity O(logn), because finding the place to insert takes O(logn) at most, inserting time is constant,
    and rebalancing complexity is O(logn)

    def handle_delete_leaf(self, node):
    the method performs the deletion of a leaf
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because deleting a leaf takes constant amount of time

    def handle_delete_with_only_right_child(self, node):
    the method performs the deletion of a node with only right child
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because we can connect the only child to the parent of the node we want to delete, and delete the node,
    which takes constant amount of time

    def handle_delete_with_only_left_child(self, node):
    the method performs the deletion of a node with only left child
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because we can connect the only child to the parent and delete the node,
    which takes constant amount of time

    def handle_normal_delete(self, node):
    the method performs the deletion of a node with two children
    if node has two children, 
    we will replace it with its successor and delete its successor which must be a leaf or unary
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: the node we need to start rebalancing from
    Complexity O(logn), because it demands rebalancing

    def delete(self, node):
    deletes node from the dictionary
    @type node: AVLNode
    @param node: the node we need to delete
    @pre: node is a real pointer to a node in self
    Complexity O(logn), because it is implemented the way it was described in class

    def balance_post_deletion_helper(self, node):
    a method created to help balance_post_deletion, that handles the rebalancing a tree after deletion in case we do not delete the root
    @type node: AVLNode
    @param node: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion method

    def balance_post_deletion_case0(self, pivot):
    a method that handles all the rebalancing cases not described in the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case1(self, pivot):
    a method that handles the rebalancing case 1 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case2_1(self, pivot):
    a method that handles the rebalancing case 2 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case2_2(self, pivot):
    a method that handles the rebalancing case symmetric to the case 2 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case3_1(self, pivot):
    a method that handles the rebalancing case 3 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case3_2(self, pivot):
    a method that handles the rebalancing case symmetric to the case 3 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case4_1(self, pivot):
    a method that handles the rebalancing case 4 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion_case4_2(self, pivot):
    a method that handles the rebalancing case symmetric to the case 4 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method

    def balance_post_deletion(self):
    a method that rebalances the tree after deleting a node
    Complexity O(logn), because it is implemented the way it was described in class

    def find_joining_point(self, h, is_right):
    the method that finds a node in the bigger tree that we will connect to the joining node,
    as it was described in the lecture
    @type h: int
    @param h: the maximal height that the node we need to find can have
    @type is_right:boolean
    @param is right: True if we need to look for the node in the right edge of the tree, False otherwise
    Complexity O(log(n)), because we walk on the tree from the root to the node with height h at most

    def join_case0(self, joining_node, tree_with_bigger_keys, tree_with_smaller_keys):
    a method which handles the case when both trees are of the same height
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type tree_with_bigger_keys: AVLTree
    @param tree_with_bigger_keys: the tree with bigger keys
    @type tree_with_smaller_keys: AVLTree
    @param tree_with_smaller_keys: the tree with smaller keys
    Complexity O(1), because joining to trees with the same height takes constant amount of time

    def join_case1(self, joining_node, taller_tree, shorter_tree):
    a method which handles the case when the tree with bigger keys is taller
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type taller_tree: AVLTree
    @param taller_tree: the tree with bigger height
    @type shorter_tree: AVLTree
    @param shorter_tree: the tree with smaller height
    Complexity O(logn), because this case demands rebalancing

    def join_case2(self, joining_node, taller_tree, shorter_tree):
    a method which handles the case when the tree with smaller keys is taller
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type taller_tree: AVLTree
    @param taller_tree: the tree with bigger height
    @type shorter_tree: AVLTree
    @param shorter_tree: the tree with smaller height
    Complexity O(logn), because this case demands rebalancing

    def join(self, tree2, key, val):
    joins self with item and another AVLTree
    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: the key separting self and tree2
    @type val: string
    @param val: the value corresponding to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
    or the opposite way
    Complexity O(logn), because it is implemented the way we saw in class. We connect two trees, and then we perform the
    amount of rebalancing steps that is at most the height pof the tree, which is O(logn).

    def split(self, node):
    splits the dictionary at a given node
    @type node: AVLNode
    @pre: node is in self
    @param node: the node in the dictionary to be used for the split
    @rtype: (AVLTree, AVLTree)
    @returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    Complexity O(logn), because it is implemented the same way it was described in class

    def avl_to_array(self):
    returns an array representing dictionary     
    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    Complexity O(n), because we need to get to every node to fill the array

    def max_node(self):
    returns the node with the maximal key in the dictionary  
    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    Complexity O(logn), because the maximal amount of steps is the height of the tree

    def min_node(self):
    returns the node with the maximal key in the dictionary
    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    Complexity O(logn), because the maximal amount of steps is the height of the tree

    def size(self):
    returns the number of items in dictionary 
    @rtype: int
    @returns: the number of items in dictionary
    Complexity O(n), because we reach each node of the tree one time 

    def get_root(self):
    returns the root of the tree representing the dictionary
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    Complexity O(1)

In addition, the project implements three enum classes whose goal is to determine the case of rebalancing after joining two trees, deletion of a node or insertion of a node
