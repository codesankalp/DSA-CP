from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.end_count = 0
        self.prefix_count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.prefix_count += 1
        node.end_count += 1

    def countWordsEqualToString(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return 0
        return node.end_count

    def countWordsStartingWith(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return 0
        return node.prefix_count

    def erase(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            node.prefix_count -= 1
        node.end_count -= 1


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.countWordsStartingWith("app"))
    print(trie.countWordsEqualToString("apple"))
    trie.erase("apple")
    print(trie.countWordsStartingWith("app"))
    print(trie.countWordsEqualToString("apple"))
