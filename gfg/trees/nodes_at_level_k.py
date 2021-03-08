from base import buildTree, Node
from collections import deque
# https://www.geeksforgeeks.org/print-leaf-nodes-at-a-given-level/


def nodes_at_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")
    nodes_at_k(root.left, k-1)
    nodes_at_k(root.right, k-1)


def leaf_nodes_at_given_level(root, k):
    if root is None:
        return
    if k == 0 and (root.left is None) and (root.right is None):
        print(root.data, end=" ")
    leaf_nodes_at_given_level(root.left, k-1)
    leaf_nodes_at_given_level(root.right, k-1)


if __name__ == '__main__':
    for _ in range(int(input("testcases: "))):
        s = input('tree: ')
        k = int(input('k: '))
        root = buildTree(s)
        print("nodes at level k: ")
        nodes_at_k(root, k)
        print()
        print("leaf nodes at level k: ")
        leaf_nodes_at_given_level(root, k)
        print()
