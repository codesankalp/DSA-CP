# lowest common ancesstor
from base import buildTree, Node


def lca(root, k1, k2):
    if root is None:
        return

    if root.data == k1 or root.data == k2:
        return root

    l = lca(root.left, k1, k2)
    r = lca(root.right, k1, k2)

    if l and r:
        return root

    if l is None:
        return r
    else:
        return l


if __name__ == "__main__":
    tree = input("tree: ")
    root = buildTree(tree)
    k1, k2 = list(map(int, input("Key1 and 2 for finding LCA").split()))
    node = lca(root, k1, k2)
    print(node, node.data)
