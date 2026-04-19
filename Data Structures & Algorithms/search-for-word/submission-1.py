# Solution:
# - Iterate through the board looking for the first character
# - Where we find it, add the coordinates to the current solution
# - Then, search if any of the neighbors (not included already in the solution) has the next character
# - Once we find all characters we return true

# - Potential optimizations: do a first O(n * m) pass to see if there's even enough characters to form the word
# - Potential optimizations: check the amount of characters per column, check that the consecutive sum is the # of characters of bigger
# - If these initial tests fail, return False right away

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
            res = False
            if i > 0:
                res |= present(i - 1, j)
            if i < n - 1:
                res |= present(i + 1, j)
            if j > 0:
                res |= present(i, j - 1)
            if j < m - 1:
                res |= present(i, j + 1)
            
            current.remove((i, j))
            return res


        for i in range(n):
            for j in range(m):
                if present(i, j):
                    return True
                        
        return False

        