# https://practice.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/1/
from base import buildTree, Node
from lca import lca

# global ans


def find_turns(root, val, ans, turn):
    if root is None:
        return False

    if root.data == val:
        return True

    if turn:
        if find_turns(root.left, val, ans, turn):
            return True
        if find_turns(root.right, val, ans, not turn):
            ans += 1
            return True
    else:
        if find_turns(root.left, val, ans, not turn):
            ans += 1
            return True
        if find_turns(root.right, val, ans, turn):
            return True
    return False


def NumberOFTurns(root, first, second):
    global ans
    node = lca(root, first, second)
    if node is None:
        return -1
    ans = 0
    print(node, node.data)
    if node.data != first and node.data != second:
        if find_turns(node.right, first, ans, False) or find_turns(node.left, first, ans, True):
            pass
        if find_turns(node.right, second, ans, False) or find_turns(node.left, second, ans, True):
            pass
        return ans+1

    if node.data == first:
        find_turns(node.right, second, ans, False)
        find_turns(node.left, second, ans, True)
        return ans
    else:
        find_turns(node.right, first, ans, False)
        find_turns(node.left, first, ans, True)
        return ans


if __name__ == "__main__":
    t = input("tree: ")
    root = buildTree(t)
    first, second = list(map(int, input("Enter two nodes: ").split()))
    print(NumberOFTurns(root, first, second))
