class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        n, m = len(heights), len(heights[0])
        def dfs(i, j, seen, prev_height):
            if (i, j) in seen or heights[i][j] < prev_height:
                return
            seen.add((i, j))
            cur_height = heights[i][j]

            if i > 0: dfs(i - 1, j, seen, cur_height)
            if i < n - 1: dfs(i + 1, j, seen, cur_height)
            if j > 0: dfs(i, j - 1, seen, cur_height)
            if j < m - 1: dfs(i, j + 1, seen, cur_height)
        
        for i in range(n):
            dfs(i, 0, pacific, 0)
            dfs(i, m - 1, atlantic, 0)
        for j in range(m):
            dfs(0, j, pacific, 0)
            dfs(n - 1, j, atlantic , 0)
        
        result = []
        for i in range(n):
            for j in range(m):
                coords = (i, j)
                if coords in pacific and coords in atlantic:
                    result.append([i, j])
        
        return result
