class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        n_rows = len(grid)
        n_cols = len(grid[0])
            
        max_area = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    level = deque()
                    level.append([i, j])
                    area = 0
                    grid[i][j] = 0
                    while level:
                        area += 1
                        i, j = level.popleft()
                        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            row = i + di
                            col = j + dj
                            if 0 <= row < n_rows and 0 <= col < n_cols and grid[row][col] == 1:
                                grid[row][col] = 0
                                level.append([row, col])

                    max_area = max(max_area, area)
        
        return max_area