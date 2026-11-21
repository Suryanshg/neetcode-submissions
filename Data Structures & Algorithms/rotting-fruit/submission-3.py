class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get position of all 2s
        level = []

        num_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    level.append([i, j])

                elif grid[i][j] == 1:
                    num_fresh += 1

        
        minutes = 0
        visited = set()
        while level:
            next_level = []
            for i, j in level:
                
                if i + 1 < len(grid) and grid[i + 1][j] == 1 and (i + 1, j) not in visited:
                    num_fresh -= 1
                    next_level.append([i + 1, j])
                    visited.add((i + 1, j))

                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1 and (i, j + 1) not in visited:
                    num_fresh -= 1
                    next_level.append([i, j + 1])
                    visited.add((i, j + 1))

                if i - 1 >= 0 and grid[i - 1][j] == 1 and (i - 1, j) not in visited:
                    num_fresh -= 1
                    next_level.append([i - 1, j])
                    visited.add((i - 1, j))

                if j - 1 >=0 and grid[i][j - 1] == 1 and (i, j - 1) not in visited:
                    num_fresh -= 1
                    next_level.append([i, j - 1])
                    visited.add((i, j - 1))


            level = next_level
            if level:
                minutes += 1
            # print(next_level)
            # if minutes == 5:
            #     break


        return minutes if num_fresh == 0 else -1
