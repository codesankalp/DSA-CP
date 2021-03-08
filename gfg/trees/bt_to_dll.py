# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1/

from base import buildTree


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class DLLNode():
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.data = val

    def append(self, val):
        if self.data is None:
            self.data = val
            return
        curr = DLLNode(val)
        temp = self
        while temp.right is not None:
            temp = temp.right
        temp.right = curr
        curr.left = temp
        return


class BtoDll:

    def __init__(self):
        self.head = None
        self.tail = None

    def convert(self, root):
        if root is None:
            return
        self.convert(root.left)
        node = Node(root.data)
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node
        self.convert(root.right)
        return self.head


def traverse(head):
    if head is None:
        return []
    left_list = traverse(head.left)
    val = head.data
    right_list = traverse(head.right)
    return left_list + [val] + right_list


def bt_to_dll(root):
    nls = traverse(root)
    start = DLLNode()
    for i in nls:
        start.append(i)
    return start


prev = None


def BinaryTree2DoubleLinkedList(root, head=None, prev=None):
    if root is None:
        return
    BinaryTree2DoubleLinkedList(root.left, head, prev)
    node = Node(root.data)
    if head is None:
        head = node
    else:
        prev.right = node
        node.left = prev
    prev = node
    BinaryTree2DoubleLinkedList(root.right, head, prev)
    return head


def b2dll(root):
    a = BtoDll()
    head = a.convert(root)
    return head


if __name__ == "__main__":
    for _ in range(int(input('testcases: '))):
        s = input("tree: ")
        root = buildTree(s)
        start = BinaryTree2DoubleLinkedList(root)
        # start = b2dll(root)
        # start = bt_to_dll(root)
        # prev = None
        while start is not None:
            # prev = start
            print(start.data, end=" ")
            start = start.right
        print()
        # while prev != None:
        #     print(prev.data, end=" ")
        #     prev = prev.left
