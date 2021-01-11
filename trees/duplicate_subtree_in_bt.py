from base import Node, buildTree

# https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1


def preorder(root, subtree={}):
    s = ""
    if root is None:
        s += "$"
        return s
    s += str(root.data)
    s += preorder(root.left, subtree)
    s += preorder(root.right, subtree)
    subtree[s] = subtree.get(s, 0)+1
    return s

# memoization of root traversal to find out duplicate subtree


def dupSub(root):
    subtree = {}
    s = preorder(root, subtree)
    # print(s)
    # print(subtree)
    for k, v in subtree.items():
        if len(k) > 3 and v >= 2:
            return True
    return False


if __name__ == "__main__":
    n = int(input("n = "))
    s = input("tree: ")
    root = buildTree(s)
    a = dupSub(root)
    if a:
        print("1")
    else:
        print("0")
