class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        num_islands = 0

        def dfs(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for di, dj in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                row = i + di
                col = j + dj
                if 0 <= row < n_rows and 0 <= col < n_cols:
                    dfs(row, col)

        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands
        