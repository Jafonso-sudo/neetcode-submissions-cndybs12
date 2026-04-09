# Solution 1: O(n^2) --- where n=3 in this case
# - Check rows, then columns, then sections, ensuring count of any seen = 0

# Bugs
# - A few syntax errors
# - Initially had num = int(cell) without the - 1 (remember indexing offset)
# - Box checking was wrong first, I was being a dum dum: i = k // 3, j = k % 3


# class Solution:
#     def validate_cell(self, cell: str, has_num: list[bool]) -> bool:
#         if cell == ".":
#             return True
#         num = int(cell) - 1
#         if has_num[num]:
#             return False
#         has_num[num] = True
#         return True

#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # Check rows
#         for i in range(9):
#             has_num = [False] * 9
#             for j in range(9):
#                 if not self.validate_cell(board[i][j], has_num):
#                     return False

#         # Check columns
#         for j in range(9):
#             has_num = [False] * 9
#             for i in range(9):
#                 if not self.validate_cell(board[i][j], has_num):
#                     return False
        
#         # Check boxes
#         for b in range(9):
#             has_num = [False] * 9
#             for k in range(9):
#                 i = k // 3 + 3 * (b // 3)
#                 j = k % 3 + 3 * (b % 3)
#                 if not self.validate_cell(board[i][j], has_num):
#                     return False
        
#         return True

# GEMINI
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue
                
                # Create unique tuple identifiers for rows, cols, and boxes
                row_id = ('row', r, val)
                col_id = ('col', c, val)
                # Integer division identifies which 3x3 grid we are in (0, 1, or 2)
                box_id = ('box', r // 3, c // 3, val)
                
                # If any of these identifiers are already in the set, the board is invalid
                if row_id in seen or col_id in seen or box_id in seen:
                    return False
                
                # Add the identifiers to our set for future checks
                seen.add(row_id)
                seen.add(col_id)
                seen.add(box_id)
                
        return True