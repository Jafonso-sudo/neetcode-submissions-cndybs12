# Space: O(n + t) where n is the length of a string since we recurse on it and create a stack and t is the # of nodes in the trie
# Time: O(n) since there's at most 2 dots (a constant overhead)
# https://gemini.google.com/app/1ce3ba868fd34b55

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.ending = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.children[c]
        node.ending = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: 'TrieNode') -> bool:
            if i == len(word):
                return node.ending

            c = word[i]
            if c == ".":
                for key in node.children:
                    if dfs(i + 1, node.children[key]):
                        return True
            elif c in node.children:
                return dfs(i + 1, node.children[c])
            
            return False
                        

        return dfs(0, self.trie)
