from base import buildTree, Node
from dfs_traversal import InOrder

# note: question is wrong or incomplete do level order
from collections import deque


def get_right_node(root):
    if root is None:
        return
    queue = deque()
    q = deque()
    node = root
    queue.append(node)
    q.append(node)
    while (len(queue) != 0):
        node = queue.popleft()
        # print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
            q.append(node.left)
        if node.right is not None:
            queue.append(node.right)
            q.append(node.right)
    return node, q


def delete(root, key, right):
    if root is None:
        return
    if root.data == key:
        root.data = right.data
        # print(root.data, root.right)
    delete(root.left, key, right)
    delete(root.right, key, right)


def deletionBT(root, key):
    '''
    root: root of tree
    key:  key to be deleted
    return: root after deleting 
    '''
    right, ls = get_right_node(root)

    # print(right, right.data)
    root = root
    delete(root, key, right)
    # print(prev.data, right.data)
    for i in ls:
        if i.right == right:
            i.right = None
            break
        if i.left == right:
            i.left = None
            break


if __name__ == "__main__":
    for _ in range(int(input('testcase: '))):
        root = buildTree(input('tree: '))
        key = int(input('key: '))
        deletionBT(root, key)
        InOrder(root)
