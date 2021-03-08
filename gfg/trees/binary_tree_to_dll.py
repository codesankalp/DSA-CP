# Python program for conversion of binary tree to doubly linked list.
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class BtoDll:

    def __init__(self):
        self.head = None
        self.tail = None

    def convert(self, root):
        # Base case
        if root is None:
            return

        # Recursively convert left subtree
        self.convert(root.left)

        # Now convert this node
        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node

        # Finally convert right subtree
        self.convert(root.right)
        return self.head


def BinaryTree2DoubleLinkedList(root):
    '''
    A simple recursive function to convert a given Binary tree  
    to Doubly Linked List 
    root --> Root of Binary Tree 
    '''
    converter = BtoDll()
    return converter.convert(root)


def print_dll(head):
    '''Function to print nodes in given doubly linked list'''
    while head is not None:
        print(head.data, end=" ")
        head = head.right


#  Driver program to test above functions
if __name__ == "__main__":

    # Let us create the tree as shown in above diagram
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    # convert to DLL
    head = BinaryTree2DoubleLinkedList(root)

    # Print the converted list
    print_dll(head)

# This code is contributed by codesankalp (SANKALP)
