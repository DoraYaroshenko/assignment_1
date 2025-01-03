from AVLTree import AVLNode, AVLTree
import math
from abc import ABCMeta
from random import shuffle, randrange

from AVLTree import AVLNode, AVLTree

from pytest import fixture

from tqdm import tqdm


@fixture
def medium_test_tree():
    root = AVLNode(key=4, value="4")

    # Level 1
    left = AVLNode(key=2, value="2")
    right = AVLNode(key=6, value="6")
    root.left = left
    root.right = right
    left.parent = root
    right.parent = root

    # Level 2
    left_left = AVLNode(key=1, value="1")
    left_right = AVLNode(key=3, value="3")
    right_left = AVLNode(key=5, value="5")
    right_right = AVLNode(key=7, value="7")

    left.left = left_left
    left.right = left_right
    left_left.parent = left
    left_right.parent = left

    right.left = right_left
    right.right = right_right
    right_left.parent = right
    right_right.parent = right

    # Level 3
    left_left_left = AVLNode(key=0, value="0")
    right_right_right = AVLNode(key=8, value="8")

    left_left.left = left_left_left
    left_left_left.parent = left_left

    right_right.right = right_right_right
    right_right_right.parent = right_right

    # Adding one more node to make 10 nodes
    top_right = AVLNode(key=9, value="9")
    right_right_right.right = top_right
    top_right.parent = right_right_right

    return AVLTree(root)


@fixture
def big_test_tree():
    root = AVLNode(key=10, value="10")

    # Level 1
    left = AVLNode(key=5, value="5")
    right = AVLNode(key=15, value="15")
    root.left = left
    root.right = right
    left.parent = root
    right.parent = root

    # Level 2
    left_left = AVLNode(key=3, value="3")
    left_right = AVLNode(key=7, value="7")
    right_left = AVLNode(key=13, value="13")
    right_right = AVLNode(key=18, value="18")

    left.left = left_left
    left.right = left_right
    left_left.parent = left
    left_right.parent = left

    right.left = right_left
    right.right = right_right
    right_left.parent = right
    right_right.parent = right

    # Level 3
    left_left_left = AVLNode(key=1, value="1")
    left_left_right = AVLNode(key=4, value="4")
    left_right_left = AVLNode(key=6, value="6")
    left_right_right = AVLNode(key=8, value="8")

    right_left_left = AVLNode(key=12, value="12")
    right_left_right = AVLNode(key=14, value="14")
    right_right_left = AVLNode(key=16, value="16")
    right_right_right = AVLNode(key=19, value="19")

    left_left.left = left_left_left
    left_left.right = left_left_right
    left_left_left.parent = left_left
    left_left_right.parent = left_left

    left_right.left = left_right_left
    left_right.right = left_right_right
    left_right_left.parent = left_right
    left_right_right.parent = left_right

    right_left.left = right_left_left
    right_left.right = right_left_right
    right_left_left.parent = right_left
    right_left_right.parent = right_left

    right_right.left = right_right_left
    right_right.right = right_right_right
    right_right_left.parent = right_right
    right_right_right.parent = right_right

    # Level 4
    left_left_left.left = AVLNode(key=0, value="0")
    left_left_left.right = AVLNode(key=2, value="2")
    left_left_left.left.parent = left_left_left
    left_left_left.right.parent = left_left_left

    left_left_right.left = AVLNode(key=None, value="None")
    left_left_right.right = AVLNode(key=None, value="None")
    left_left_right.left.parent = left_left_right
    left_left_right.right.parent = left_left_right

    left_right_left.left = AVLNode(key=None, value="None")
    left_right_left.right = AVLNode(key=None, value="None")
    left_right_left.left.parent = left_right_left
    left_right_left.right.parent = left_right_left

    left_right_right.left = AVLNode(key=None, value="None")
    left_right_right.right = AVLNode(key=9, value="9")
    left_right_right.left.parent = left_right_right
    left_right_right.right.parent = left_right_right

    right_left_left.left = AVLNode(key=11, value="11")
    right_left_left.right = AVLNode(key=None, value="None")
    right_left_left.left.parent = right_left_left
    right_left_left.right.parent = right_left_left

    right_left_right.left = AVLNode(key=None, value="None")
    right_left_right.right = AVLNode(key=None, value="None")
    right_left_right.left.parent = right_left_right
    right_left_right.right.parent = right_left_right

    right_right_left.left = AVLNode(key=None, value="None")
    right_right_left.right = AVLNode(key=17, value="17")
    right_right_left.left.parent = right_right_left
    right_right_left.right.parent = right_right_left

    right_right_right.left = AVLNode(key=None, value="None")
    right_right_right.right = AVLNode(key=None, value="None")
    right_right_right.left.parent = right_right_right
    right_right_right.right.parent = right_right_right

    # Add children with None keys to 0, 2, 9, 11, and 17
    zero_node = left_left_left.left
    zero_node.left = AVLNode(key=None, value="None")
    zero_node.right = AVLNode(key=None, value="None")
    zero_node.left.parent = zero_node
    zero_node.right.parent = zero_node

    two_node = left_left_left.right
    two_node.left = AVLNode(key=None, value="None")
    two_node.right = AVLNode(key=None, value="None")
    two_node.left.parent = two_node
    two_node.right.parent = two_node

    nine_node = left_right_right.right
    nine_node.left = AVLNode(key=None, value="None")
    nine_node.right = AVLNode(key=None, value="None")
    nine_node.left.parent = nine_node
    nine_node.right.parent = nine_node

    eleven_node = right_left_left.left
    eleven_node.left = AVLNode(key=None, value="None")
    eleven_node.right = AVLNode(key=None, value="None")
    eleven_node.left.parent = eleven_node
    eleven_node.right.parent = eleven_node

    seventeen_node = right_right_left.right
    seventeen_node.left = AVLNode(key=None, value="None")
    seventeen_node.right = AVLNode(key=None, value="None")
    seventeen_node.left.parent = seventeen_node
    seventeen_node.right.parent = seventeen_node
    return AVLTree(root)


@fixture()
def build_tree():
    return build_tree1_from_array()


def build_tree1_from_array():
    lst = [i for i in range(10000)]

    # [3, 5, 8, 7, 4, 2, 1, 6, 0, 9]
    # [i for i in range(10)]
    shuffle(lst)
    print(lst)
    root = AVLNode(key=lst[0], value=str(lst[0]), height=0)
    root.left = AVLNode(key=None, value=None, parent=root)
    root.right = AVLNode(key=None, value=None, parent=root)
    tree = AVLTree(root)
    promotions = 0
    for i in lst[1:]:
        promotions = tree.insert(key=i, val=str(i))[2]
    valid_proms = promotions <= math.log2(10000)
    # print(valid_proms)
    # print_tree(tree.root)
    return tree


def build_tree2_from_array():
    lst = [i for i in range(10001, 20001)]
    # [15,16]
    # [i for i in range(11, 21)]
    shuffle(lst)
    print(lst)
    root = AVLNode(key=lst[0], value=str(lst[0]), height=0)
    root.left = AVLNode(key=None, value=None, parent=root)
    root.right = AVLNode(key=None, value=None, parent=root)
    tree = AVLTree(root)
    num = randrange(2, 10000)
    for number in lst[1:num]:
        tree.insert(key=number, val=str(number))
    return tree


@fixture()
def build_tree2():
    return build_tree2_from_array()


def print_tree(node, level=0, prefix="Root: "):
    """if node.is_real_node():
    """
    parent = node.parent
    if parent is not None:
        parent = parent.key
    print(
        " " * (level * 4) + prefix + "(Key:"+ str(node.key)+" Value: "+str(node.value)+" Height: "+str(node.height)+" Parent:" +str(parent)+")")
    if node.left is not None:
        print_tree(node.left, level + 1, prefix="L--- ")
    if node.right is not None:
        print_tree(node.right, level + 1, prefix="R--- ")
    # if level==0:
    #     print("\n\n\n")
    # if node is not None:
    #     print_tree(node.left, level + 1)
    #     print(' ' * 4 * level + '-> ' + str(node.value))
    #     print_tree(node.right, level + 1)


def test_avl_size(build_tree):
    assert build_tree.size() == 10000


def test_balance(build_tree):
    root = build_tree.root
    if not root.is_real_node():
        return True
    left_diff = root.height - root.left.height
    right_diff = root.height - root.right.height
    case1 = (left_diff == 1 and right_diff == 1)
    case2 = (left_diff == 1 and right_diff == 2)
    case3 = (left_diff == 2 and right_diff == 1)
    return (case1 or case2 or case3) and test_balance(build_tree.left_subtree()) and test_balance(
        build_tree.right_subtree())


def check_bst(root):
    if not root.is_real_node() or (not root.left.is_real_node() and not root.right.is_real_node()):
        return True

    elif not root.right.is_real_node():
        return root.left.key < root.key and check_bst(root.left)

    elif not root.left.is_real_node():
        return root.right.key >= root.key and check_bst(root.right)

    return check_bst(root.left) and check_bst(root.right)


def test_children(build_tree):
    assert check_bst(build_tree.root)
    return check_bst(build_tree.root)


def test_is_avl_tree(build_tree):
    print(test_balance(build_tree))
    print(test_children(build_tree))
    assert test_balance(build_tree) and test_children(build_tree)
    return test_balance(build_tree) and test_children(build_tree)


def test_join(build_tree, build_tree2):
    # print_tree(build_tree.root)
    # print_tree(build_tree2.root)
    print(build_tree.size(), build_tree2.size())
    build_tree.join(build_tree2, 10000, 10000)
    # print_tree(build_tree.root)
    assert test_balance(build_tree) and test_children(build_tree)
    return test_is_avl_tree(build_tree)


def test_10000_times():
    for i in tqdm(range(10)):
        tree1 = build_tree1_from_array()
        tree2 = build_tree2_from_array()
        flag = test_join(tree1, tree2)
        assert flag


def test_insert(build_tree):
    assert test_is_avl_tree(build_tree)


def test_finger_search(build_tree):
    num = randrange(0, 10000)
    node, path = build_tree.finger_search(num)
    assert node.key == num


def test_right_rotate():
    nodeA = AVLNode(2, 2)
    nodeX = AVLNode(4, 4)
    nodeB = AVLNode(5, 5)
    nodeY = AVLNode(7, 7)
    nodeC = AVLNode(9, 9)
    nodeAba = AVLNode(10, 10)
    nodeAba.left = nodeY
    nodeY.parent = nodeAba
    nodeA.parent = nodeX
    nodeX.left = nodeA
    nodeB.parent = nodeX
    nodeX.right = nodeB
    nodeC.parent = nodeY
    nodeY.right = nodeC
    nodeX.parent = nodeY
    nodeY.left = nodeX

    nodeA.left = AVLNode(None, None, parent=nodeA)
    nodeA.right = AVLNode(None, None, parent=nodeA)
    nodeB.left = AVLNode(None, None, parent=nodeB)
    nodeB.right = AVLNode(None, None, parent=nodeB)
    nodeC.left = AVLNode(None, None, parent=nodeC)
    nodeC.right = AVLNode(None, None, parent=nodeC)

    print_tree(nodeAba)
    AVLTree.rotate_right(nodeY)
    print_tree(nodeAba)
    AVLTree.rotate_left(nodeX)
    print_tree(nodeAba)
    AVLTree.left_right_double_rotation(nodeY)
    print_tree(nodeAba)


def test_avl_to_array(build_tree):
    # [0,1,2,3,4,5]

    assert build_tree.avl_to_array() == [(i, str(i)) for i in range(build_tree.size())]

#def main():
#    test_10000_times()


#if __name__=="__main__":
#    main()





