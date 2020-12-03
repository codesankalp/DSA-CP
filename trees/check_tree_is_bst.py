
from base import Node, buildTree

MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')
# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/


def check_bst(root, min_val, max_val):
    if root is None:
        return True

    return root.data > min_val and root.data < max_val and check_bst(root.left, min_val, root.data) and check_bst(root.right, root.data, max_val)

# another method using inorder traversal


if __name__ == '__main__':
    for _ in range(int(input("testcases: "))):
        s = input('tree: ')
        root = buildTree(s)
        if check_bst(root, MIN_VALUE, MAX_VALUE):
            print("BST")
        else:
            print("not BST")
