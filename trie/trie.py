class Node:
    def __init__(self):
        self.flag = False
        self.links = [None] * 26

    def containsKey(self, ch):
        return self.links[ord(ch) - ord("a")] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord("a")] = node

    def get(self, ch):
        return self.links[ord(ch) - ord("a")]

    def setEnd(self):
        self.flag = True


class Trie:
    def __init__(self):
        self.root = Node()

    # O(n)
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)  # move to the next ref
        node.setEnd()

    # O(n)
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.flag

    # O(n)
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True
