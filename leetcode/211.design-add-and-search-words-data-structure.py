#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        self.ans = False
        # self.dfs(node, word)
        return self.search_in_stack(node, word)
        # return self.ans

    def dfs(self, node, word):
        if not word:
            if node.word:
                self.ans = True
            return
        if word[0] == '.':
            for node_ in node.children.values():
                self.dfs(node_, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

    def search_in_stack(self, node, word):
        stack = [(node, word)]
        while len(stack) != 0:
            node, word = stack.pop()
            if not word:
                if node.word:
                    return True
            elif word[0] == '.':
                for node_ in node.children.values():
                    stack.append((node_, word[1:]))
            else:
                n = node.children.get(word[0])
                if n:
                    stack.append((n, word[1:]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
