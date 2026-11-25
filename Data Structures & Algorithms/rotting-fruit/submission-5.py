class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        level = []
        num_fresh = 0
        n_rows = len(grid)
        n_cols = len(grid[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    level.append([i, j])
                if grid[i][j] == 1:
                    num_fresh += 1
        
        minutes = 0
        while level:
            next_level = []
            for i, j in level:
                for di, dj in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                    row = i + di
                    col = j + dj
                    if 0 <= row < n_rows and 0 <= col < n_cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        num_fresh -= 1
                        next_level.append([row, col])
            
            if next_level:
                minutes += 1
            level = next_level
        
        return minutes if num_fresh == 0 else -1