class Solution:
    def is_valid_row(self, row_idx, board):
        row_set = set()
        for num in board[row_idx]:
            if num != ".":
                if num in row_set:
                    return False
                row_set.add(num)       
        return True


    def is_valid_column(self, col_idx, board):
        col_set = set()
        for row_idx in range(9):
            num = board[row_idx][col_idx]
            if num != ".":
                if num in col_set:
                    return False
                col_set.add(num)
        return True


    def is_valid_grid(self, grid_idx, board):
        grid_set = set()
        row_start = 3 * (grid_idx // 3)
        col_start = 3 * (grid_idx % 3)
        for row_idx in range(row_start, row_start + 3):
            for col_idx in range(col_start, col_start + 3):
                num = board[row_idx][col_idx]
                if num != ".":
                    if num in grid_set:
                        return False
                    grid_set.add(num)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row-wise
        for row in range(9):
            if not self.is_valid_row(row, board):
                return False


        # Check column-wise
        for col in range(9):
            if not self.is_valid_column(col, board):
                return False



        # Check grid-wise
        for grid in range(9):
            if not self.is_valid_grid(grid, board):
                return False


        # Otherwise, return True
        return True
        