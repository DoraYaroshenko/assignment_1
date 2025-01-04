# id1:
# name1:
# username1:
# id2:
# name2:
# username2:
from typing import Optional
from enum import Enum

"""A class representing all the possible cases of disbalance created by inserting a node or joining two trees"""


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


"""
A class representing all the possible cases of height differences between two trees that we join
"""


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


"""
A class representing all the possible cases of disbalance after deleting a node
"""


class DeleteRebalanceCase(Enum):
    CASE0 = 0  # node balanced
    CASE1 = 1
    CASE2_1 = 21
    CASE2_2 = 22
    CASE3_1 = 31
    CASE3_2 = 32
    CASE4_1 = 41
    CASE4_2 = 42

    @classmethod
    def determine_balance_after_deletion_case(cls, node):
        if node.balance_factor() == 0 and node.height - node.left.height == 2:  # node is 2,2
            return DeleteRebalanceCase.CASE1
        if node.balance_factor() == 2:  # node is 3,1
            if node.right.balance_factor() == 0:  # right of node is 1,1
                return DeleteRebalanceCase.CASE2_1
            if node.right.balance_factor() == -1:  # right of node is 1,2
                return DeleteRebalanceCase.CASE4_1
            if node.right.balance_factor() == 1:  # right of node is 2,1
                return DeleteRebalanceCase.CASE3_1
        if node.balance_factor() == -2:  # node is 1,3
            if node.left.balance_factor() == 0:  # left of node is 1,1
                return DeleteRebalanceCase.CASE2_2
            if node.left.balance_factor() == -1:
                return DeleteRebalanceCase.CASE3_2
            if node.left.balance_factor() == 1:
                return DeleteRebalanceCase.CASE4_2
        return DeleteRebalanceCase.CASE0


"""
A class representing a node in an AVL tree
"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    @type height: int
    @param height: height of your node
    @type parent: AVLNode
    @param parent: the parent of your node
    """
    def __init__(self, key, value, height=-1, parent=None):
        self.key = key
        self.value = value
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.parent: Optional[AVLNode] = parent
        self.height: int = height

    """
    the method returns whether self is not a virtual node
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    Complexity O(1)
    """
    def is_real_node(self):
        if self is None or self.key is None:
            return False
        return True

    """
    returns the balance factor of the node
    @rtype: int
    @returns: the difference between the heights of node and its left child minus the difference between the heights of
    node and its right child
    Complexity O(1)
    """
    def balance_factor(self):
        if not self.is_real_node():
            return 0
        return (self.height - self.left.height) - (self.height - self.right.height)

    """
    returns whether node has only right child, and doesn't have a left one
    @rtype: boolean
    @returns: True if node has only right child, False otherwise
    Complexity O(1)
    """
    def has_only_right_child(self):
        if not self.left.is_real_node() and self.right.is_real_node():
            return True
        return False

    """
    returns whether node has only left child, and doesn't have a right one
    @rtype: boolean
    @returns: True if node has only left child, False otherwise
    Complexity O(1)
    """
    def has_only_left_child(self):
        if not self.right.is_real_node() and self.left.is_real_node():
            return True
        return False

    """
    the method promotes a height of a given node by delta
    @type delta: int
    @param delta: the value added to the height of the node
    @rtype: int
    @returns: the number of promotions made
    Complexity O(1)
    """
    def promote_height(self, delta=1):
        self.height += delta
        return delta

    """
    the method demotes a height of a given node by delta
    @type delta: int
    @param delta: the value removed from the height of the node
    Complexity O(1)
    """
    def demote_height(self, delta=1):
        self.height -= delta

    """
    returns whether the node is a leaf of the tree
    @rtype: boolean
    @returns: True if the node is a leaf, False otherwise
    Complexity O(1)
    """
    def is_leaf(self):
        return (self.left is None or not self.left.is_real_node()) and (
                self.right is None or not self.right.is_real_node())

    """
    returns whether the node is a root of a tree
    @rtype: boolean
    @returns: True if the node is a root, False otherwise
    Complexity O(1)
    """
    def is_root(self):
        return self.parent is None

    """
    returns whether the node is the right child of its parent
    @rtype: boolean
    @returns: True if the node is a right child, False otherwise
    Complexity O(1)
    """
    def is_right_child(self):
        if self.parent is not None and self.parent.right is not None and self.parent.right is self:
            return True
        return False

    """
    returns whether the node is the left child of its parent
    @rtype: boolean
    @returns: True if the node is a left child, False otherwise
    Complexity O(1)
    """
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
    @type root: AVLNode
    @param root: a future root of the tree
    """

    def __init__(self, root=None):
        self.root: AVLNode = root

    """
    a method that returns a successor of a given node in the tree, implemented the way it was described in class
    @type node: AVLNode
    @param node: a node whose successor we need to find
    @rtype: AVLNode
    @returns: the successor
    Complexity O(logn), because the maximal amount of steps is the height of the tree
    """
    def successor(self, node):
        if node.right.is_real_node():
            left_subtree = AVLTree(node.right)
            return left_subtree.min_node()
        curr = node
        next = node.parent
        while next is not None and curr is next.right:
            curr = next
            next = curr.parent
        return next

    """
    the method creates a tree whose root is the parent of a given node
    @type node: AVLNode
    @param node: a node whose parent will be a root of the created tree
    @rtype: AVLTree
    @returns: a tree whose root is the parent of a given node
    Complexity O(1)
    """
    @staticmethod
    def parent_tree(node):
        ptree = AVLTree()
        ptree.root = node.parent
        return ptree

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
    """
    def search_logic(self, k, path):
        if self.root is None or not self.root.is_real_node() or self.root.key == k:
            return self.root, path
        if self.root.key > k:
            return self.left_subtree().search_logic(k, path + 1)
        return self.right_subtree().search_logic(k, path + 1)

    """
    searches for a node in the dictionary corresponding to the key (starting at the root)
    uses search_logic method to perform the search        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    Complexity O(logn), because search uses search_logic
    """
    def search(self, key):
        node, path = self.search_logic(key, 0)
        if node is None or not node.is_real_node():
            return None, path
        return node, path

    """searches for a node in the dictionary corresponding to the key, starting at the max
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
    """
    def finger_search_logic(self, key):
        if self.root is None:
            return self.root, 0
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
        return curr.left, path+1

    """
    searches for a node in the dictionary corresponding to the key, starting at the max
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    time complexity is O(log(n)), since the first and second loops will have at most log(n) iterations of O(1) complexity
    and then we call on a function of time complexity O(log(n))
    hence the total running time in the worst case is 3log(n)=O(log(n))
    """
    def finger_search(self, key):
        node, path = self.finger_search_logic(key)
        if node is None or not node.is_real_node():
            return None, path
        return node, path

    """
    the method creates a valid node for the tree
    @type key: int
    @param key: the key of the node we create
    @type val: int
    @param: the value of the node we create
    @type parent: AVLNode
    @param parent: the parent of the node we create
    @rtype: AVLNode
    @returns: the new node
    Complexity O(1)
    """
    @staticmethod
    def create_valid_node(key, val, parent=None):
        new_node = AVLNode(key, val, 0)
        new_node.left = AVLNode(None, None, parent=new_node)
        new_node.right = AVLNode(None, None, parent=new_node)
        new_node.parent = parent
        return new_node

    """
    the method rotates right the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant
    """
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

    """the method rotates left the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant
    """
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
    the method performs double rotation left and then right on the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant
    """
    def left_right_double_rotation(self, node):
        AVLTree.rotate_left(self, node.left)
        AVLTree.rotate_right(self, node)

    """
    the method performs double rotation right and then left on the subtree whose root is a given node
    @type node: AVLNode
    @param node: the node we want to start the rotation from
    Complexity O(1), because the amount of time is constant
    """
    def right_left_double_rotation(self, node):
        AVLTree.rotate_right(self, node.right)
        AVLTree.rotate_left(self, node)

    """
    the method rebalances the tree after inserting a node or joining two trees starting from a given node
    @type node: AVLNode
    @param node: the node we start to rebalance from
    @rtype: int
    @returns: the number of height promotions made
    Complexity O(logn), because we walk from the node to the root by the maximum amount of steps equal
    to the height of the tree, and we perform maximum 2 rotations
    """
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

    """finds a place to insert a node in the tree
    @type key: int
    @param key: a key of the node we want to add to the tree
    @rtype: (AVLNode, int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or the node in which place the node with key k
    would be placed in the tree if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    Complexity O(logn), because it uses search_logic method
    """
    def find_insertion_place(self, key):
        return self.search_logic(key, 0)

    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

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
    """
    def insert(self, key, val, finger=False):
        node, path_len_counter = self.find_insertion_place(
            key) if not finger else self.find_finger_insertion_place(key)
        if node is None or (not node.is_real_node() and node.parent is None):
            self.root = self.create_valid_node(key, val)
            return self.root, 0, 0
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

    """finds a place to insert a node in the tree, starting from the max
    @type key: int
    @param key: a key of the node we want to add to the tree
    @rtype: (AVLNode, int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or the node in which place the node with key k
    would be placed in the tree if not found), and e is the number of edges on the path between the starting node and
    ending node+1.
    Complexity O(logn), because it uses finger_search_logic method
    """
    def find_finger_insertion_place(self, key):
        return self.finger_search_logic(key)

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
    Complexity O(logn), because finding the place to insert takes O(logn) at most, inserting time is constant,
    and rebalancing complexity is O(logn)
    """
    def finger_insert(self, key, val):
        return self.insert(key, val, True)

    """
    the method performs the deletion of a leaf
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because deleting a leaf takes constant amount of time
    """
    def handle_delete_leaf(self, node):
        new_pointer = node.right
        if node.is_root():
            self.root = None
        elif node.is_right_child():  # if node is the right child of its parent
            node.parent.right = new_pointer
        else:
            node.parent.left = new_pointer
        pivot = node.parent
        new_pointer.parent = node.parent
        return pivot

    """
    the method performs the deletion of a node with only right child
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because we can connect the only child to the parent and delete the node,
    which takes constant amount of time
    """
    def handle_delete_with_only_right_child(self, node):
        new_pointer = node.right
        if node.is_root():
            self.root = new_pointer
        elif node.is_right_child():  # if node is the right child of its parent
            node.parent.right = new_pointer
        else:
            node.parent.left = new_pointer
        new_pointer.parent = node.parent
        return new_pointer

    """
    the method performs the deletion of a node with only left child
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: a node we start to rebalance from
    Complexity O(1), because we can connect the only child to the parent and delete the node,
    which takes constant amount of time
    """
    def handle_delete_with_only_left_child(self, node):
        new_pointer = node.left
        if node.is_root():
            self.root = new_pointer
        elif node.is_right_child():  # if node is the right child of its parent
            node.parent.right = new_pointer
        else:
            node.parent.left = new_pointer
        new_pointer.parent = node.parent
        return new_pointer

    """
    the method performs the deletion of a node with two children
    if node has two children, 
    we will replace it with its successor and delete its successor which must be a leaf or unary
    @type node: AVLNode
    @param node: the node we need to delete
    @rtype: AVLNode
    @returns: the node we need to start rebalancing from
    Complexity O(logn), because it demands rebalancing
    """
    def handle_normal_delete(self, node):
        new_pointer = self.successor(node)
        temp_key = node.key
        temp_val = node.value
        node.key = new_pointer.key
        node.value = new_pointer.value
        new_pointer.key = temp_key
        new_pointer.value = temp_val
        self.delete(new_pointer)
        return node

    """deletes node from the dictionary
    @type node: AVLNode
    @param node: the node we need to delete
    @pre: node is a real pointer to a node in self
    Complexity O(logn), because it is implemented the way it was described in class
    """
    def delete(self, node):
        if not node.is_real_node():
            return

        if node.is_leaf():
            pivot = self.handle_delete_leaf(node)
        elif node.has_only_right_child():
            pivot = self.handle_delete_with_only_right_child(node)
        elif node.has_only_left_child():
            pivot = self.handle_delete_with_only_left_child(node)
        else:
            pivot = self.handle_normal_delete(node)

        curr_tree = AVLTree(pivot)
        curr_tree.balance_post_deletion()

    """
    a method created to help balance_post_deletion, that handles the rebalancing a tree after deletion in case we do not delete the root
    @type node: AVLNode
    @param node: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion method
    """
    def balance_post_deletion_helper(self, node):
        if node.parent is not None:
            ptree = self.parent_tree(node)
            ptree.balance_post_deletion()

    """
    a method that handles all the rebalancing cases not described in the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case0(self, pivot):
        if pivot.parent is not None:
            case_parent = DeleteRebalanceCase.determine_balance_after_deletion_case(pivot.parent)
            if case_parent == DeleteRebalanceCase.CASE0:
                pass
            else:
                self.balance_post_deletion_helper(pivot)

    """
    a method that handles the rebalancing case 1 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case1(self, pivot):
        pivot.demote_height()
        self.balance_post_deletion_helper(pivot)

    """
    a method that handles the rebalancing case 2 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case2_1(self, pivot):
        new_root = pivot.right
        new_root.promote_height()
        pivot.demote_height()
        self.rotate_left(pivot)
        self.balance_post_deletion_helper(new_root)

    """
    a method that handles the rebalancing case symmetric to the case 2 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case2_2(self, pivot):
        new_root = pivot.left
        new_root.promote_height()
        pivot.demote_height()
        self.rotate_right(pivot)
        self.balance_post_deletion_helper(new_root)

    """
    a method that handles the rebalancing case 3 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case3_1(self, pivot):
        pivot.demote_height()
        pivot.demote_height()
        self.rotate_left(self.root)
        self.balance_post_deletion_helper(pivot)

    """
    a method that handles the rebalancing case symmetric to the case 2 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case3_2(self, pivot):
        pivot.demote_height()
        pivot.demote_height()
        self.rotate_right(self.root)
        self.balance_post_deletion_helper(pivot)

    """
    a method that handles the rebalancing case symmetric to the case 3 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case4_1(self, pivot):
        new_root = pivot.right.left
        new_right = pivot.right
        pivot.demote_height()
        pivot.demote_height()
        new_right.demote_height()
        new_root.promote_height()
        self.right_left_double_rotation(pivot)
        self.balance_post_deletion_helper(new_root)

    """
    a method that handles the rebalancing case symmetric to the case 4 from the lecture
    @type pivot: AVLNode
    @param pivot: the node we start rebalancing from
    Complexity O(logn), because it calls balance_post_deletion_helper method
    """
    def balance_post_deletion_case4_2(self, pivot):
        new_root = pivot.left.right
        new_left = pivot.left
        pivot.demote_height()
        pivot.demote_height()
        new_left.demote_height()
        new_root.promote_height()
        self.left_right_double_rotation(pivot)
        self.balance_post_deletion_helper(new_root)

    """
    a method that rebalances the tree after deleting a node
    Complexity O(logn), because it is implemented the way it was described in class
    """
    def balance_post_deletion(self):
        pivot = self.root
        if pivot.is_real_node():
            deletion_rebalance_case = DeleteRebalanceCase.determine_balance_after_deletion_case(pivot)
            match deletion_rebalance_case:
                case DeleteRebalanceCase.CASE0:  # if node is balanced
                    self.balance_post_deletion_case0(pivot)
                case DeleteRebalanceCase.CASE1:
                    self.balance_post_deletion_case1(pivot)
                case DeleteRebalanceCase.CASE2_1:
                    self.balance_post_deletion_case2_1(pivot)
                case DeleteRebalanceCase.CASE2_2:
                    self.balance_post_deletion_case2_2(pivot)
                case DeleteRebalanceCase.CASE3_1:
                    self.balance_post_deletion_case3_1(pivot)
                case DeleteRebalanceCase.CASE3_2:
                    self.balance_post_deletion_case3_2(pivot)
                case DeleteRebalanceCase.CASE4_1:
                    self.balance_post_deletion_case4_1(pivot)
                case DeleteRebalanceCase.CASE4_2:
                    self.balance_post_deletion_case4_2(pivot)

    """
    the method that finds a node in the bigger tree that we will connect to the joining node,
    as it was described in the lecture
    @type h: int
    @param h: the maximal height that the node we need to find can have
    @type is_right:boolean
    @param is right: True if we need to look for the node in the right edge of the tree, False otherwise
    Complexity O(log(n)), because we walk on the tree from the root to the node with height h at most
    """
    def find_joining_point(self, h, is_right):
        node = self.root
        while node.height > h:
            if is_right:
                node = node.right
            else:
                node = node.left
        return node

    """
    a method which handles the case when both trees are of the same height
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type tree_with_bigger_keys: AVLTree
    @param tree_with_bigger_keys: the tree with bigger keys
    @type tree_with_smaller_keys: AVLTree
    @param tree_with_smaller_keys: the tree with smaller keys
    Complexity O(1), because joining to trees with the same height takes constant amount of time
    """
    def join_case0(self, joining_node, tree_with_bigger_keys, tree_with_smaller_keys):
        joining_node.right = tree_with_bigger_keys.root
        tree_with_bigger_keys.root.parent = joining_node
        joining_node.left = tree_with_smaller_keys.root
        tree_with_smaller_keys.root.parent = joining_node
        self.root = joining_node
        joining_node.promote_height()

    """
    a method which handles the case when the tree with bigger keys is taller
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type taller_tree: AVLTree
    @param taller_tree: the tree with bigger height
    @type shorter_tree: AVLTree
    @param shorter_tree: the tree with smaller height
    Complexity O(logn), because this case demands rebalancing
    """
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

    """
    a method which handles the case when the tree with smaller keys is shorter
    @type joining_node: AVLNode
    @param joining_node: the node given to connect the trees
    @type taller_tree: AVLTree
    @param taller_tree: the tree with bigger height
    @type shorter_tree: AVLTree
    @param shorter_tree: the tree with smaller height
    Complexity O(logn), because this case demands rebalancing
    """
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

    """joins self with item and another AVLTree
    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: the key separting self and tree2
    @type val: string
    @param val: the value corresponding to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
    or the opposite way
    Complexity O(logn), because it is implemented the way we saw in class
    """
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
    Complexity O(logn), because it is implemented the same way it was described in class
    """
    def split(self, node):
        curr_node = node
        node_right_subtree = AVLTree(node.right)
        node_left_subtree = AVLTree(node.left)
        tree_with_bigger_keys = node_right_subtree
        tree_with_bigger_keys.root.parent = None
        tree_with_smaller_keys = node_left_subtree
        tree_with_smaller_keys.root.parent = None
        while curr_node.parent is not None:
            is_right = curr_node.is_right_child()
            curr_node = curr_node.parent
            if is_right:
                node_left_subtree = AVLTree(curr_node.left)
                node_left_subtree.root.parent = None
                if tree_with_smaller_keys.size() == 0:
                    node_left_subtree.insert(curr_node.key, curr_node.value)
                    tree_with_smaller_keys = node_left_subtree
                else:
                    tree_with_smaller_keys.join(node_left_subtree, curr_node.key, curr_node.value)
            else:
                node_right_subtree = AVLTree(curr_node.right)
                node_right_subtree.root.parent = None
                if tree_with_bigger_keys.size() == 0:
                    node_right_subtree.insert(curr_node.key, curr_node.value)
                    tree_with_bigger_keys = node_right_subtree
                else:
                    tree_with_bigger_keys.join(node_right_subtree, curr_node.key, curr_node.value)
        return tree_with_smaller_keys, tree_with_bigger_keys

    """returns an array representing dictionary     
    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    Complexity O(n), because we need to get to every node to fill the array
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
    Complexity O(logn), because the maximal amount of steps is the height of the tree
    """
    def max_node(self):
        node = self.root
        while node.right.is_real_node():
            node = node.right
        return node

    """returns the node with the maximal key in the dictionary
    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    Complexity O(logn), because the maximal amount of steps is the height of the tree
    """
    def min_node(self):
        node = self.root
        while node.left.is_real_node():
            node = node.left
        return node

    """returns the number of items in dictionary 
    @rtype: int
    @returns: the number of items in dictionary
    Complexity O(n), because we reach each node of the tree one time 
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
    Complexity O(1)
    """
    def get_root(self):
        return self.root
