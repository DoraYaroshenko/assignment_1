import math
from abc import ABCMeta
from random import shuffle, randrange

from AVLTree import AVLNode, AVLTree

from pytest import fixture

from tqdm import tqdm

N = 10
I = 10


# def test():
#     for i in range(10):
#         I=i+1
#         test_part_2()
def test_part_2():
    sum_of_hipochim_random = 0
    # i = 1
    for j in range(20):
        sum_of_hipochim_random += test_num_of_hipochim(I)
    print(sum_of_hipochim_random / 20)
    sum_of_hipochim_chance = 0
    for j in range(20):
        sum_of_hipochim_chance += test_num_of_hipochim(I)
    print(sum_of_hipochim_chance / 20)


def test_num_of_hipochim_backwards(i=10):
    counter = 0
    arr = create_sorted_backwards_array(i)
    print(len(arr))
    for j in range(len(arr)):
        curr_num = arr[j]
        for k in range(j, len(arr)):
            if arr[k] < curr_num:
                counter += 1
    print(counter)
    return counter


def test_third_part_test():
    # i = 1  # change with every test until it's 10
    average_promotions_random = 0
    average_promotions_chance = 0
    num_of_steps_sorted = 0
    num_of_steps_sorted_backwards = 0
    """counting promotions on sorted array """
    arr_sorted = create_sorted_array(I)
    tree_sorted = AVLTree()
    for j in range(len(arr_sorted)):
        """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO num_of_promotions_sorted"""
        tree_sorted.finger_insert(arr_sorted[j], arr_sorted[j])
        num_of_steps_sorted += tree_sorted.finger_search(arr_sorted[j])[1]
    print("cost for sorted array: " + str(num_of_steps_sorted))

    """counting promotions on sorted backwards array """
    arr_sorted_backwards = create_sorted_backwards_array(I)
    tree_backwards = AVLTree()
    for j in range(len(arr_sorted)):
        """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO num_of_promotions_sorted_backwards"""
        tree_backwards.finger_insert(arr_sorted_backwards[j], arr_sorted_backwards[j])
        num_of_steps_sorted_backwards += tree_backwards.finger_search(arr_sorted_backwards[j])[1]
    print("cost for sorted backwards array: " + str(num_of_steps_sorted_backwards))

    """counting promotions on randomly shuffled array """

    sum_of_steps_random = 0
    for j in range(20):
        arr_random = create_randomized_array(I)
        curr_num_of_promotions = 0
        tree_random = AVLTree()
        for k in range(len(arr_random)):
            """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO curr_num_of_promotions """
            tree_random.finger_insert(arr_random[k], arr_random[k])
            curr_num_of_promotions += tree_random.finger_search(arr_random[k])[1]
        sum_of_steps_random += curr_num_of_promotions
    average_promotions_random = sum_of_steps_random / 20
    print("cost for random array " + str(average_promotions_random))

    """counting promotions on array in which numbers have a 50% chance of being swapped with their neighbor"""

    sum_of_promotions_random_chance = 0
    for j in range(20):
        arr_random_chance = create_array_sorted_with_chance(I)
        curr_num_of_steps = 0
        tree_chance = AVLTree()
        for k in range(len(arr_random_chance)):
            """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO curr_num_of_promotions """
            tree_chance.finger_insert(arr_random_chance[k], arr_random_chance[k])
            curr_num_of_steps += tree_chance.finger_search(arr_random_chance[k])[1]
        sum_of_promotions_random_chance += curr_num_of_steps
    average_promotions_chance = sum_of_promotions_random_chance / 20
    print("cost for semi randomized array " + str(average_promotions_chance))


def test_first_part_test():
    # i = 1  # change with every test until it's 10
    average_promotions_random = 0
    average_promotions_chance = 0
    num_of_promotions_sorted = 0
    num_of_promotions_sorted_backwards = 0
    """counting promotions on sorted array """
    arr_sorted = create_sorted_array(I)
    tree_sorted = AVLTree()
    for j in range(len(arr_sorted)):
        """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO num_of_promotions_sorted"""
        num_of_promotions_sorted += tree_sorted.finger_insert(arr_sorted[j], arr_sorted[j])[2]
    print("cost for sorted array: " + str(num_of_promotions_sorted))

    """counting promotions on sorted backwards array """
    arr_sorted_backwards = create_sorted_backwards_array(I)
    tree_backwards = AVLTree()
    for j in range(len(arr_sorted)):
        """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO num_of_promotions_sorted_backwards"""
        num_of_promotions_sorted_backwards += \
        tree_backwards.finger_insert(arr_sorted_backwards[j], arr_sorted_backwards[j])[2]
    print("cost for sorted backwards array: " + str(num_of_promotions_sorted_backwards))

    """counting promotions on randomly shuffled array """

    sum_of_promotions_random = 0
    for j in range(20):
        arr_random = create_randomized_array(I)
        curr_num_of_promotions = 0
        tree_random = AVLTree()
        for k in range(len(arr_random)):
            """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO curr_num_of_promotions """
            curr_num_of_promotions += tree_random.finger_insert(arr_random[k], arr_random[k])[2]
        sum_of_promotions_random += curr_num_of_promotions
    average_promotions_random = sum_of_promotions_random / 20
    print("cost for random array " + str(average_promotions_random))

    """counting promotions on array in which numbers have a 50% chance of being swapped with their neighbor"""

    sum_of_promotions_random_chance = 0
    for j in range(20):
        arr_random_chance = create_array_sorted_with_chance(I)
        curr_num_of_promotions = 0
        tree_chance = AVLTree()
        for k in range(len(arr_random_chance)):
            """INSERT EVERY NUMBER AND EACH TIME ADD THE NUMBER OF PROMOTIONS TO curr_num_of_promotions """
            curr_num_of_promotions += tree_chance.finger_insert(arr_random_chance[k], arr_random_chance[k])[2]
        sum_of_promotions_random_chance += curr_num_of_promotions
    average_promotions_chance = sum_of_promotions_random_chance / 20
    print("cost for semi randomized array " + str(average_promotions_chance))


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
    lst = [3,1,2]
        # [i for i in range(N)]
    # [2, 3, 1, 7, 5, 8, 4, 0, 9, 6]
    # [i for i in range(10)]

    # [3, 5, 8, 7, 4, 2, 1, 6, 0, 9]
    # [i for i in range(10)]
    # shuffle(lst)
    # print(lst)
    # root = AVLNode(key=lst[0], value=str(lst[0]), height=0)
    # root.left = AVLNode(key=None, value=None, parent=root)
    # root.right = AVLNode(key=None, value=None, parent=root)
    tree = AVLTree()
    promotions = 0
    for i in lst:
        x, path, promotions, = tree.insert(key=i, val=str(i), finger=True)
        print_tree(tree.root)
        print(promotions)
    valid_proms = promotions <= 2 * math.log2(N)
    assert valid_proms
    # print_tree(tree.root)
    return tree


def build_tree2_from_array():
    lst = [i for i in range(N + 1, 2 * N + 1)]
    # [15,16]
    # [i for i in range(11, 21)]
    shuffle(lst)
    print(lst)
    # root = AVLNode(key=lst[0], value=str(lst[0]), height=0)
    # root.left = AVLNode(key=None, value=None, parent=root)
    # root.right = AVLNode(key=None, value=None, parent=root)
    tree = AVLTree()
    num = randrange(2, N)
    for number in lst[0:num]:
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
        " " * (level * 4) + prefix + f"(Key: {node.key}, Value: {node.value}, Height: {node.height}, Parent: {parent})")
    if node.left:
        print_tree(node.left, level + 1, prefix="L--- ")
    if node.right:
        print_tree(node.right, level + 1, prefix="R--- ")
    # if level==0:
    #     print("\n\n\n")
    # if node is not None:
    #     print_tree(node.left, level + 1)
    #     print(' ' * 4 * level + '-> ' + str(node.value))
    #     print_tree(node.right, level + 1)


def test_avl_size(build_tree):
    assert build_tree.size() == 3


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
    # print(test_balance(build_tree))
    # print(test_children(build_tree))
    assert test_balance(build_tree) and test_children(build_tree)
    return test_balance(build_tree) and test_children(build_tree)


def test_join(build_tree, build_tree2):
    # print_tree(build_tree.root)
    # print_tree(build_tree2.root)
    size1 = build_tree.size()
    size2 = build_tree2.size()
    print(size1, size2)
    build_tree.join(build_tree2, N, N)
    # print_tree(build_tree.root)
    assert test_balance(build_tree) and test_children(build_tree) and build_tree.size() == size1 + size2 + 1
    return test_is_avl_tree(build_tree)


def test_split(build_tree):
    num = randrange(0, N)
    # print(num)
    # print_tree(build_tree.root)
    node = build_tree.search(num)[0]
    minimum = build_tree.min_node()
    maximum = build_tree.max_node()
    build_tree_array = build_tree.avl_to_array()
    build_tree_array = [x[0] for x in build_tree_array]
    build_tree_array.remove(num)
    tree_with_smaller_keys, tree_with_bigger_keys = build_tree.split(node)
    # print_tree(tree_with_smaller_keys.root)
    # print_tree(tree_with_bigger_keys.root)
    assert test_is_avl_tree(tree_with_bigger_keys) and test_is_avl_tree(tree_with_smaller_keys)
    is_valid_split = False
    tree_with_smaller_keys_array = [x[0] for x in tree_with_smaller_keys.avl_to_array()]
    tree_with_bigger_keys_array = [x[0] for x in tree_with_bigger_keys.avl_to_array()]
    all_nums_are_in = set(build_tree_array) == set(tree_with_smaller_keys_array
                                                   + tree_with_bigger_keys_array)
    assert all_nums_are_in and all(x < num for x in tree_with_smaller_keys_array) and all(
        x > num for x in tree_with_bigger_keys_array)
    if node is minimum:
        assert tree_with_smaller_keys.size() == 0 and num < tree_with_bigger_keys.min_node().key
        is_valid_split = tree_with_smaller_keys.size() == 0 and num < tree_with_bigger_keys.min_node().key
    elif node is maximum:
        assert tree_with_bigger_keys.size() == 0 and tree_with_smaller_keys.max_node().key < num
        is_valid_split = tree_with_bigger_keys.size() == 0 and tree_with_smaller_keys.max_node().key < num
    else:
        assert tree_with_smaller_keys.max_node().key < num < tree_with_bigger_keys.min_node().key
        is_valid_split = tree_with_smaller_keys.max_node().key < num < tree_with_bigger_keys.min_node().key
    return test_is_avl_tree(tree_with_bigger_keys) and test_is_avl_tree(tree_with_smaller_keys) and is_valid_split and \
        tree_with_smaller_keys.search(num)[0] is None and tree_with_bigger_keys.search(num)[
            0] is None and all_nums_are_in and all(x < num for x in tree_with_smaller_keys_array) and all(
            x > num for x in tree_with_bigger_keys_array)


def test_split_1000_times():
    for i in tqdm(range(100)):
        tree = build_tree1_from_array()
        flag = test_split(tree)
        assert flag


def test_deletion(build_tree):
    print_tree(build_tree.root)
    num = randrange(0, N)
    node = build_tree.search(num)[0]
    print(node.key)
    build_tree.delete(node)
    print_tree(build_tree.root)
    assert test_is_avl_tree(build_tree) and build_tree.search(num)[0] is None
    return test_is_avl_tree(build_tree) and build_tree.search(num)[0] is None


def test_delete_10000_times():
    for i in tqdm(range(1000)):
        tree1 = build_tree1_from_array()
        flag = test_deletion(tree1)
        assert flag


def test_join_10000_times():
    for i in tqdm(range(100)):
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


def create_sorted_array(i: int):
    arr = [i + 1 for i in range(111 * 2 ** i)]
    # print(arr)
    return arr


def create_sorted_backwards_array(i: int):
    arr = []
    for j in range(111 * 2 ** i):
        arr.append(111 * 2 ** i - j)
    return arr


def create_randomized_array(i: int):
    arr = create_sorted_array(i)
    shuffle(arr)
    return arr


def create_array_sorted_with_chance(i: int):
    arr = create_sorted_array(i)
    for j in range(len(arr) - 1):
        num = randrange(100)
        if (num < 50):
            pass
        else:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    return arr


def test_create_sorted_backwards_array():
    arr = create_sorted_backwards_array(1)
    return arr
    # print(len(arr))
    # print(arr)


def test_create_sorted_array():
    # i = 1
    arr = create_sorted_array(I)
    return arr
    # print(len(arr))
    # print(arr)


def test_create_randomized_array():
    # i = 5
    arr = create_randomized_array(I)
    return arr
    # print(len(arr))
    # print(arr)


def test_create_array_sorted_with_chance():
    # i = 1
    arr = create_array_sorted_with_chance(I)
    return arr
    # print(len(arr))
    # print(arr)


"""
the theoretical upper bound on cost of balancing including rotations in O(log(n)), rotations run on O(1)
time complexity, so if a rotation is needed at any stage of insertion, the work at that stage will remain bound by O(1)
and this is why rotations do not affect the upper bound of the cost of rebalancing
"""

"""PART 2"""
"""
אם נתייחס למערך כתמורה על המספרים הטבעיים הקטנים או שווים ל111*2**i, אז מספר ההיפוכים הוא כמספר החילופים בתמורה
מספר החילופים במערך ממויין הוא תמיד יהיה 0, שהרי כל מספר נמצא במקומו 
מספר החילופים במערך ממויין הפוך יהיה תמיד n/2 מעוגל למטה
כשמדובר במערך אקראי הדברים מסתבכים, אפשר לספרו את כמות ההיפוכים ע"י חילוק התמורה לחילופים ומספר החילופים הוא גם מספר ההיפוכים

"""


def test_num_of_hipochim(i: int):
    arr_randomized = create_randomized_array(i)
    counter = 0
    for j in range(111 * (2 ** I)):
        curr_num = arr_randomized[j]
        for k in range(j, len(arr_randomized)):
            if arr_randomized[k] < curr_num:
                counter += 1
    return counter


def test_num_of_hipochim_chance(i: int):
    arr_chance = create_array_sorted_with_chance(i)
    counter = 0
    for j in range(111 * (2 ** I)):
        curr_num = arr_chance[j]
        for k in range(j, len(arr_chance)):
            if arr_chance[k] < curr_num:
                counter += 1
    return counter
