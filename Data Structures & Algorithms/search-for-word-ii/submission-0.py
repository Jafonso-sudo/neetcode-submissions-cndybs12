# Solution
# - Add all words to a Trie
# - When searching, keep track of seen words & such

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i
    
    def get(self, c):
        return self.children[ord(c) - ord('a')]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        n, m = len(board), len(board[0])
        trie = TrieNode()
        for i, word in enumerate(words):
            trie.addWord(word, i)

        def dfs(i, j, node):
            prev = node
            if i < 0 or j < 0 or i >= n or j >= m or not node.refs or board[i][j] == "*" or (node := node.get(board[i][j])) is None:
                return
            
            cur_char = board[i][j]
            board[i][j] = "*"

            if node.idx != -1:
                result.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    board[i][j] = cur_char
                    return
            
            dfs(i - 1, j, node)
            dfs(i + 1, j, node)
            dfs(i, j - 1, node)
            dfs(i, j + 1, node)
            board[i][j] = cur_char
        
        for i in range(n):
            for j in range(m):
                dfs(i, j, trie)
        
        return result



        