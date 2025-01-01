from AVLTree import AVLNode, AVLTree


def medium_test_tree():
        tree=AVLTree()
        root= AVLNode(25, 25)
        tree.set_root(root)
        node2=AVLNode(9, 9)
        root.insert(node2)
        node3=AVLNode(5, 5)
        root.insert(node3)
        node4=AVLNode(2, 2)
        root.insert(node4)
        node5=AVLNode(13, 13)
        root.insert(node5)
        node6=AVLNode(11, 11)
        root.insert(node6)
        node7=AVLNode(20, 20)
        root.insert(node7)
        node8=AVLNode(18, 18)
        root.insert(node8)
        node9=AVLNode(23, 23)
        root.insert(node9)
        node10=AVLNode(33, 33)
        root.insert(node10)
        node11=AVLNode(29, 29)
        root.insert(node11)
        node12=AVLNode(59, 59)
        root.insert(node12)
        node13=AVLNode(41, 41)
        root.insert(node13)
        node14=AVLNode(31, 31)
        root.insert(node14)
        node15=AVLNode(26, 26)
        root.insert(node15)
        node16=AVLNode(30, 30)
        root.insert(node16)
        node17=AVLNode(32, 32)
        root.insert(node17)
        print("hello1")
        root.height=root.adjust()
        root.inorder()
        print("root height is good")
        find=tree.finger_search(59)
        print("FINAL")
        #print (find[0])
        #print(find[1])
        #print("hello1")
        #find=tree.search(25)
        print (find[0])
        print(find[1])
        print("hello2")
        tree.delete(node13)
        print("AFTER DELETION"+"\r\n"+"\r\n")
        root.inorder()

def small_test():
    root=AVLNode(25,25)
    tree=AVLTree()
    tree.set_root(root)
    node=AVLNode(26,26)
    root.insert(node)
    root.height=root.adjust()
    root.inorder()
    tree.delete(node)
    print("test")
    root.inorder()

def main():
    #small_test()
    medium_test_tree()

if __name__=="__main__":
        main()






