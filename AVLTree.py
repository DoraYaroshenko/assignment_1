# id1:
# name1:
# username1:
# id2:
# name2:
# username2:
from typing import Optional
from enum import Enum


class InsertRebalanceCase(Enum):
    CASE0 = 0
    CASE1 = 1
    CASE2_1 = 21
    CASE2_2 = 22
    CASE3_1 = 31
    CASE3_2 = 32

    @classmethod
    def from_insert_height_diffs(cls, parent_left_diff, parent_right_diff, node_left_diff, node_right_diff):
        if parent_left_diff == 1 and parent_right_diff == 1:
            return InsertRebalanceCase.CASE0
        elif (parent_left_diff == 0 and parent_right_diff == 1) or (parent_left_diff == 1 and parent_right_diff == 0):
            return InsertRebalanceCase.CASE1
        elif (parent_left_diff == 0 and parent_right_diff == 2) and (
                node_left_diff == 1 and node_right_diff == 2):
            return InsertRebalanceCase.CASE2_1
        elif (parent_left_diff == 2 and parent_right_diff == 0) and (
                node_left_diff == 2 and node_right_diff == 1):
            return InsertRebalanceCase.CASE2_2
        elif (parent_left_diff == 0 and parent_right_diff == 2) and (
                node_left_diff == 2 and node_right_diff == 1):
            return InsertRebalanceCase.CASE3_1
        elif (parent_left_diff == 2 and parent_right_diff == 0) and (
                node_left_diff == 1 and node_right_diff == 2):
            return InsertRebalanceCase.CASE3_2
        else:
            raise Exception


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value, height=-1, parent=None):
        self.key = key
        self.value = value
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.parent: Optional[AVLNode] = parent
        self.height: int = height

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def promote_height(self):
        self.height += 1
        return 1

    def demote_height(self):
        self.height -= 1

    def is_real_node(self):
        if self is None or self.key is None:
            return False
        return True

    def is_leaf(self):
        return (not self.left.is_real_node()) and (not self.right.is_real_node())

    def is_root(self):
        return self.parent is None

    def is_right_child(self):
        if self.parent is not None and self.parent.right is not None and self.parent.right.key == self.key:
            return True
        return False

    def is_left_child(self):
        if self.parent is not None and self.parent.left is not None and self.parent.left.key == self.key:
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

    @staticmethod
    def create_valid_leaf(key, val, parent):
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

    def rebalance_after_insert(self, node):
        promotions = 0
        parent = node.parent
        promotions += node.promote_height()
        if parent is None:
            return promotions

        parent_left_diff = parent.height - parent.left.height
        parent_right_diff = parent.height - parent.right.height
        node_left_diff = node.height - node.left.height
        node_right_diff = node.height - node.right.height
        insertion_case = InsertRebalanceCase.from_insert_height_diffs(
            parent_left_diff=parent_left_diff, parent_right_diff=parent_right_diff,
            node_left_diff=node_left_diff, node_right_diff=node_right_diff
        )

        match insertion_case:
            case InsertRebalanceCase.CASE0:
                pass
            case InsertRebalanceCase.CASE1:
                promotions += self.rebalance_after_insert(parent)
            case InsertRebalanceCase.CASE2_1:
                self.rotate_right(parent)
                parent.demote_height()
            case InsertRebalanceCase.CASE2_2:
                self.rotate_left(parent)
                parent.demote_height()
            case InsertRebalanceCase.CASE3_1:
                right = node.right
                self.left_right_double_rotation(parent)
                node.demote_height()
                parent.demote_height()
                right.promote_height()
            case InsertRebalanceCase.CASE3_2:
                left = node.left
                self.right_left_double_rotation(parent)
                node.demote_height()
                parent.demote_height()
                left.promote_height()
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
        node, is_right, path_len_counter = self.find_insertion_place(key)
        new_node = self.create_valid_leaf(key, val, node.parent)
        parent_is_leaf = node.parent.is_leaf()
        if is_right:
            node.parent.right = new_node
        else:
            node.parent.left = new_node

        promotions = 0
        if new_node.parent.is_root():
            new_node.parent.promote_height()
            promotions += 1
        elif not parent_is_leaf:
            pass
        else:
            promotions = self.rebalance_after_insert(new_node.parent)
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
