
from collections import deque

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)
    return []


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
    return []


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
    return []


# driver code


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def buildTree(s):
    # corner case
    if ((len(s) == 0 or s[0] == "N")):
        return None

    # creating list of string
    ip = list(map(str, s.split()))

    # root of tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # push the root to queue
    q.append(root)
    size = size + 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1

        # get current node value from ip
        currVal = ip[i]

        # if the left child is not null
        if (currVal != "N"):

            # create the left child for current node
            currNode.left = Node(int(currVal))

            # pish it to the queue
            q.append(currNode.left)
            size += 1
        # for right child
        i += 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # if the right child is not null
        if currVal != "N":

            # create the right child for current node
            currNode.right = Node(int(currVal))

            # push it to the queue
            q.append(currNode.right)
            size += 1
        i = i+1
        # print(q)
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        print("In order Traversal (left - root - right)")
        res = InOrder(root)
        print()
        print("Pre order Traversal (root - left - right)")
        res = preorder(root)
        print()
        print("Post order Traversal (left - right - root)")
        res = postorder(root)
        print()
