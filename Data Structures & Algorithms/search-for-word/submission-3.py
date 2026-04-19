# Solution:
# - Iterate through the board looking for the first character
# - Where we find it, add the coordinates to the current solution
# - Then, search if any of the neighbors (not included already in the solution) has the next character
# - Once we find all characters we return true

# COMPLETLY WRONG
# Time: O((n * m) ^ word_len) Space: word_len
# CORRECT
# Time: O(N * M * 3^L)
# Why?
# - We start from an N * M loop
# - At each point we explore 3 branches (not 4, because one of them is where we come from, so we know we don't go down there)
# - They have a depth of the size of the word


# Small opt
# - Potential optimizations: do a first O(n * m) pass to see if there's even enough characters to form the word
# - Potential optimizations: check the amount of characters per column, check that the consecutive sum is the # of characters of bigger
# - If these initial tests fail, return False right away

# Cheatsheet / TODO
# - I need to learn/think about time complexity of combinatorial problems

# Gemini Review: https://gemini.google.com/app/283a973a403645eb
# - Once we find the first true value, we can return right away
# - We also can do a simpler directional loop

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        current = set()
        word_len = len(word)
        n, m = len(board), len(board[0])

        def present(i: int, j: int) -> bool:
            if board[i][j] != word[len(current)] or (i, j) in current:
                return False
            elif len(current) + 1 == word_len:
                return True
            current.add((i, j))
            
            # Check neighbors
            res = (
                (i > 0 and present(i - 1, j)) or
                (i < n - 1 and present(i + 1, j)) or
                (j > 0 and present(i, j - 1)) or
                (j < m - 1 and present(i, j + 1))
            )
            
            current.remove((i, j))
            return res


        for i in range(n):
            for j in range(m):
                if present(i, j):
                    return True
                        
        return False

        