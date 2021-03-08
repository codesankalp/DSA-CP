# to check a given binary tree is balanced.
from base import Node, buildTree
import time

# time complexity -> O(n*n) (when traverse height and then check)


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1


def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)

    return (abs(left_height-right_height) <= 1) and (is_balanced(root.left)) and (is_balanced(root.right))


# new method in O(n) because finding height inside the recursion

def isBalanced(root):
    if root is None:
        # returning height=0 for leaf nodes.
        return 0
    lh = isBalanced(root.left)
    rh = isBalanced(root.right)
    # checking if the subtree is ever false then returning
    # false for the whole recursion
    if lh is False or rh is False:
        return False
    if abs(lh-rh) > 1:
        # returning false if subtree is not balanced
        return False
    else:
        # returning height if subtree is balanced
        return max(lh, rh)+1


# 9 7 N 8 10 N 6 4 N 6 10 N 8
# root = Node(9)
# root.left = Node(7)
# root.left.left = Node(8)
# root.left.right = Node(10)
# root.left.left.right = Node(6)
# root.left.right.left = Node(4)
# root.left.left.right.left = Node(6)
# root.left.left.right.right = Node(10)
# root.left.right.left.right = Node(8)
if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        root = buildTree(s)
        start = time.time()
        print(is_balanced(root))
        half = time.time()
        print(isBalanced(root))
        end = time.time()
        print(half-start, end-half)
