# https://practice.geeksforgeeks.org/problems/two-mirror-trees/1/?track=amazon-trees&batchId=192#
# https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/
def inorder(root):
    if root is None:
        return []
    left = inorder(root.left)
    a = root.data
    right = inorder(root.right)
    return left + [a] + right


def reverse(root):
    if root is None:
        return []
    right = reverse(root.right)
    a = root.data
    left = reverse(root.left)
    return right + [a] + left


def areMirror(root1, root2):
    '''
    :param root1,root2: two root of the given trees.
    :return: True False

    '''
    ls1 = inorder(root1)
    ls2 = reverse(root2)
    return ls1 == ls2
