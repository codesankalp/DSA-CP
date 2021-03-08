from collections import deque

# bfs is also called as level order traversal

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def levelorder(root):
    if root is None:
        return []
    queue = deque()
    queue.append(root)
    while (len(queue) != 0):
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return []


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
        print("Level order Traversal or breadth first traversal")
        res = levelorder(root)
        print()
