class Node:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.prefix_count = 0
        self.ends_with = 0

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch) -> 'Node':
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def increaseEnd(self):
        self.ends_with += 1

    def increasePrefix(self):
        self.prefix_count += 1

    def decreaseEnd(self):
        self.ends_with -= 1

    def decreasePrefix(self):
        self.prefix_count -= 1


class Trie:

    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
                node.increasePrefix()
            node = node.get(ch)
        node.increaseEnd()

    def countWordsEqualToString(self, word: str):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.ends_with

    def countWordsStartingWith(self, word: str):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.prefix_count

    def erase(self, word: str):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.decreasePrefix()
        node.decreaseEnd()


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.countWordsStartingWith("app"))
    print(trie.countWordsEqualToString("apple"))
    trie.erase("apple")
    print(trie.countWordsStartingWith("app"))
    print(trie.countWordsEqualToString("apple"))
