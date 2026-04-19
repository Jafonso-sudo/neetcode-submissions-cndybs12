# Cheatsheet
# - Trie (prefix tree)
# - "Autovivification": tree = lambda: defaultdict(tree) https://gemini.google.com/app/259acef9aeb7f7fd

class PrefixTree:

    def __init__(self):
        # tree = lambda: defaultdict(tree)
        self.children = {}

    def insert(self, word: str) -> None:
        cur_tree = self.children
        for c in word:
            if c not in cur_tree:
                cur_tree[c] = {}
            cur_tree = cur_tree[c]
        cur_tree[None] = None
        


    def search(self, word: str) -> bool:
        cur_tree = self.children
        for c in word:
            if c not in cur_tree:
                return False
            cur_tree = cur_tree[c]
        return None in cur_tree
        

    def startsWith(self, prefix: str) -> bool:
        cur_tree = self.children
        for c in prefix:
            if c not in cur_tree:
                return False
            cur_tree = cur_tree[c]
        return True
        
        