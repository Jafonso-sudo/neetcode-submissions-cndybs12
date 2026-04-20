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
        n = len(word)
        def dfs(i: int, node: 'TrieNode') -> bool:
            # Base Cases
            c = word[i]
            if c == ".":
                for key in node.children:
                    if i == n - 1:
                        if node.children[key].ending:
                            return True
                    else:
                        if dfs(i + 1, node.children[key]):
                            return True
            elif c in node.children:
                if i == n - 1:
                    return node.children[c].ending
                else:
                    return dfs(i + 1, node.children[c])
            
            return False
                        

        return dfs(0, self.trie)
