class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Init num_islands, num_rows as m, num_cols as n
        num_islands = 0
        m = len(grid)
        n = len(grid[0])

        # Maintain a set of seen_idxs so that we never double visit them
        seen_idxs = set()

        # For each cell in the grid
        for i in range(m):
            for j in range(n):

                # If its 1 and not visited before
                if grid[i][j] == "1" and (i, j) not in seen_idxs:
                    
                    # Explore it as an island via BFS
                    # Maintain a stack where we safely add (i, j) if not visited
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        seen_idxs.add((row, col))

                        # If current row, col is 1, add its 4 neighbors in the stack for
                        # further exploration
                        if grid[row][col] == "1":
                            if row > 0 and (row - 1, col) not in seen_idxs:
                                stack.append((row - 1, col))
                            if row < m - 1 and (row + 1, col) not in seen_idxs:
                                stack.append((row + 1, col))
                            if col > 0 and (row, col - 1) not in seen_idxs:
                                stack.append((row, col - 1))
                            if col < n - 1 and (row, col + 1) not in seen_idxs:
                                stack.append((row, col + 1))

                    # An island is fully explored, so now we can increment the count of islands
                    num_islands += 1

        # Return the final count of islands
        return num_islands