class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        level = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    level.append([i, j])

                if grid[i][j] == 1:
                    num_fresh += 1

        minutes = 0
        while level:
            next_level = []
            for i, j in level:
                for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                    row = i + di
                    col = j + dj
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        num_fresh -= 1
                        next_level.append([row, col])
            if next_level:
                minutes += 1
            level = next_level

        return minutes if num_fresh == 0 else -1