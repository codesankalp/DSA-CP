# every parent value must be the sum of children nodes.

from base import buildTree, Node


def check_children_sum(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    sum = 0
    if root.left is not None:
        sum += root.left.data
    if root.right is not None:
        sum += root.right.data
    return (sum == root.data and check_children_sum(root.right) and check_children_sum(root.left))


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        root = buildTree(s)
        if check_children_sum(root):
            print("Yes")
        else:
            print("No")
