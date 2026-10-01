class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Init number of rows (m) and cols (n)
        m = len(grid)
        n = len(grid[0])


        # Find number of fresh fruits and idx of rotten ones
        num_fresh_fruits = 0
        rotten_idxs = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_idxs.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh_fruits += 1

        # init minutes as 0 and an empty visited set
        minutes = 0
        visited = set()

        # For all rotten idxs, add it to a level array (queue) for BFS
        level = []
        for idx in rotten_idxs:
            level.append(idx)
            visited.add(idx)

        # While level array has elements
        while level:
            
            # Accumulate next level by exploring each cell's neighbors in current level
            next_level = []
            for i,j in level:
                if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) not in visited:
                    visited.add((i - 1, j))
                    num_fresh_fruits -= 1
                    next_level.append((i - 1, j))

                if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in visited:
                    visited.add((i, j - 1))
                    num_fresh_fruits -= 1
                    next_level.append((i, j - 1))

                if i < m - 1 and grid[i + 1][j] == 1 and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    num_fresh_fruits -= 1
                    next_level.append((i + 1, j))

                if j < n - 1 and grid[i][j + 1] == 1 and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    num_fresh_fruits -= 1
                    next_level.append((i, j + 1))

            # Set next level to current level
            level = next_level

            # If next level has any elements, increase minutes
            if next_level:
                minutes += 1


        return minutes if not num_fresh_fruits else -1
        