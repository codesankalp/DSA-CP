from bfs_traversal import InOrder


class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if root.data == val:
            return root
        elif root.data < val:
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root


def search(root, key):

    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


ls = list(map(int, input("Enter the list of numbers: ").split()))
root = None
for i in ls:
    root = insert(root, i)
InOrder(root)
