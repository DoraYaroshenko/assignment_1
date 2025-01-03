# id1:
# name1:
# username1:
# id2:
# name2:
# username2:
from typing import Optional
from enum import Enum


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

    def promote_height(self, delta=1):
        self.height += delta
        return delta

    def demote_height(self, delta=1):
        self.height -= delta

    def is_real_node(self):
        if self is None or self.key is None:
            return False
        return True

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


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self, root=None):
        self.root: AVLNode = root

    """
    method for creation of the left subtree of the current tree
    @rtype: AVLTree
    @returns: the left subtree of the current tree
    time complexity O(1)
    """

    def left_subtree(self):
        ltree = AVLTree()
        ltree.root = self.root.left
        return ltree

    """
    method for creation of the right subtree of the current tree
    @rtype: AVLTree
    @returns: the right subtree of the current tree
    time complexity O(1)
    """

    def right_subtree(self):
        rtree = AVLTree()
        rtree.root = self.root.right
        return rtree

    """
    envelope function for search
    @type k: int
    @param k: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def search_logic(self, k, path):
        if not self.root.is_real_node() or self.root.key == k:
            return self.root, path
        if self.root.key > k:
            return self.left_subtree().search_logic(k, path + 1)
        return self.right_subtree().search_logic(k, path + 1)

    """searches for a node in the dictionary corresponding to the key (starting at the root)
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def search(self, key):
        node, path = self.search_logic(key, 0)
        if not node.is_real_node():
            return node.key, path
        return node, path

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
        node, path = self.finger_search_logic(key)
        if not node.is_real_node():
            return node.key, path
        return node, path

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

        match rebalance_case:
            case RebalanceCase.CASE_TERMINAL:
                pass
            case RebalanceCase.CASE_DIFF_0_1_OR_1_0:
                promotions += self.rebalance_after_insertion_or_join(parent)
            case RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_2:
                self.rotate_right(parent)
                parent.demote_height()
            case RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_2_1:
                self.rotate_left(parent)
                parent.demote_height()
            case RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_2_1:
                right = node.right
                self.left_right_double_rotation(parent)
                node.demote_height()
                parent.demote_height()
                right.promote_height()
            case RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_2:
                left = node.left
                self.right_left_double_rotation(parent)
                node.demote_height()
                parent.demote_height()
                left.promote_height()
            case RebalanceCase.CASE_DIFF_2_2:
                parent.demote_height()
                promotions += self.rebalance_after_insertion_or_join(parent)
            case RebalanceCase.CASE_PARENT_DIFF_2_0_CHILD_DIFF_1_1:
                self.rotate_left(parent)
                promotions += self.rebalance_after_insertion_or_join(node)
            case RebalanceCase.CASE_PARENT_DIFF_0_2_CHILD_DIFF_1_1:
                self.rotate_right(parent)
                promotions += self.rebalance_after_insertion_or_join(node)
        return promotions

    def find_insertion_place(self, key):
        return self.search_logic(key, 0)

    def insert(self, key, val, finger=False):
        node, path_len_counter = self.find_insertion_place(
            key) if not finger else self.find_finger_insertion_place(key)
        new_node = self.create_valid_node(key, val, node.parent)
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

    def find_finger_insertion_place(self, key):
        return self.finger_search_logic(key)

    def finger_insert(self, key, val):
        return self.insert(key, val, True)

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
        match joining_case:
            case JoiningRebalanceCase.CASE0:
                self.join_case0(joining_node, tree_with_bigger_keys, tree_with_smaller_keys)
            case JoiningRebalanceCase.CASE1:
                self.join_case1(joining_node, taller_tree, shorter_tree)
            case JoiningRebalanceCase.CASE2:
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
        node = self.root
        while node.right.is_real_node():
            node = node.right
        return node

    def min_node(self):
        node = self.root
        while node.left.is_real_node():
            node = node.left
        return node

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
