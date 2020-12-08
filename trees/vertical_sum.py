from base import buildTree, Node

# space optimized approach because no use of dict


def vertical_sum(root, node=Node(0)):
    print(node.data)
    node.data += root.data
    if root.left:
        if node.left is None:
            node.left = Node(0)
            node.left.right = node
        vertical_sum(root.left, node.left)
    if root.right:
        if node.right is None:
            node.right = Node(0)
            node.right.left = node
        vertical_sum(root.right, node.right)
    # return node

# another approach: https://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/


def helper(root):
    ls = []
    print(ls)
    node = Node(0)
    vertical_sum(root, node)
    while node.left is not None:
        node = node.left
    while node is not None:
        ls.append(node.data)
        node = node.right
    return ls


if __name__ == "__main__":
    for _ in range(int(input('testcases: '))):
        root = buildTree(input('tree: '))
        ans = helper(root)
        print(ans)
