class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        m = len(grid)
        n = len(grid[0])

        seen_idxs = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen_idxs:
                    num_islands += 1
                    
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        seen_idxs.add((row, col))
                        if grid[row][col] == "1":
                            if row > 0 and (row - 1, col) not in seen_idxs:
                                stack.append((row - 1, col))
                            if row < m - 1 and (row + 1, col) not in seen_idxs:
                                stack.append((row + 1, col))
                            if col > 0 and (row, col - 1) not in seen_idxs:
                                stack.append((row, col - 1))
                            if col < n - 1 and (row, col + 1) not in seen_idxs:
                                stack.append((row, col + 1))


        return num_islands