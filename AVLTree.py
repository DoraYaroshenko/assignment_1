# id1:
# name1:
# username1:
# id2:
# name2:
# username2:

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value, height=-1, parent = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.height = height

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.key is None or self is None:
            return False
        return True

    def is_leaf(self):
        return not self.left.is_real_node() and not self.right.is_real_node()


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self, root=None):
        self.root: AVLNode = root

    """searches for a node in the dictionary corresponding to the key (starting at the root)
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def search(self, key):
        return None, -1

    """searches for a node in the dictionary corresponding to the key, starting at the max
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def finger_search(self, key):
        return None, -1

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

    def rotate_right(self):
        root = self.root
        new_root = self.root.left
        new_root.parent = root.parent
        root.left = new_root.right
        root.left.parent = root
        new_root.right = root
        new_root.right.parent = new_root
        self.root = new_root
        return new_root

    def rotate_left(self):
        root = self.root
        new_root = root.right
        new_root.parent = root.parent
        root.right = new_root.left
        root.right.parent = root
        new_root.left = root
        new_root.left.parent = new_root
        self.root = new_root
        return new_root

    def double_rotation(self):
        root = self.root
        root.left = AVLTree(root.left).rotate_left()
        return self.rotate_right()

    def rebalance(self, node):
        promotions = 0
        parent = node.parent
        left_diff = parent.height - parent.left.height
        right_diff = parent.height - parent.right.height
        if left_diff == 1 and right_diff == 1:
            return 0
        elif (left_diff == 0 and right_diff == 1) or (left_diff == 1 and right_diff == 0):
            parent.height += 1
            promotions += 1 + self.rebalance(parent)
        elif (left_diff == 0 and right_diff == 2) or (left_diff == 2 and right_diff == 0):
            node_children_left_diff = node.height - node.left.height
            node_children_right_diff = node.height - node.right.height
            if node_children_left_diff == 1 and node_children_right_diff == 2:
                new_subtree_root = AVLTree(parent).rotate_right()
                if parent.parent.left.key == parent.key:
                    parent.parent.left = new_subtree_root
                else:
                    parent.parent.right = new_subtree_root
                parent.height -= 1
            else:
                new_subtree_root = AVLTree(parent).double_rotation()
                new_subtree_root.height += 1
                if parent.parent.left.key == parent.key:
                    parent.parent.left = new_subtree_root
                else:
                    parent.parent.right = new_subtree_root
                parent.height -= 1
                node.height -= 1
        return promotions

    def find_insertion_place(self, key):
        node = self.root
        is_right = False
        path_len_counter = 0
        while node.is_real_node():
            if node.key > key:
                node = node.left
                is_right = False
            else:
                node = node.right
                is_right = True
            path_len_counter += 1
        return node, is_right, path_len_counter

    def insert(self, key, val):
        insertion_place_details = self.find_insertion_place(key)
        node = insertion_place_details[0]
        is_right = insertion_place_details[1]
        path_len_counter = insertion_place_details[2]
        needs_rebalance = False
        if node.parent.is_leaf():
            needs_rebalance = True
        new_node = AVLNode(key, val, 0)
        new_node.left = AVLNode(None, None, parent=new_node)
        new_node.right = AVLNode(None, None, parent=new_node)
        new_node.parent = node.parent
        if is_right:
            node.parent.right = new_node
        else:
            node.parent.left = new_node
        promotions = 0
        if needs_rebalance:
            new_node.parent.height += 1
            if new_node.parent.key != self.root.key:
                promotions = 1 + self.rebalance(new_node.parent)
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

    def finger_insert(self, key, val):
        return None, -1, -1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        return

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
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        if not self.root.is_real_node():
            return 0
        if self.root.is_leaf():
            return 1
        return AVLTree(self.root.left).size() + AVLTree(self.root.right).size() + 1

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None
