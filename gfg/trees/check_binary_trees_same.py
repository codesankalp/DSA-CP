
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return true/false or 1/0


from collections import deque


def isIdentical(root1, root2):
    # Code here
    if root1 is None and root2 is None:
        return True
    # if root1 is None or root2 is None:
    #     return False
    # if (root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)):
    #     return True
    if root1 is not None and root2 is not None:
        return ((root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)))
    return False


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
        s1 = input()
        s2 = input()
        head1 = buildTree(s1)
        head2 = buildTree(s2)
        if isIdentical(head1, head2):
            print("YES")
        else:
            print("No")
