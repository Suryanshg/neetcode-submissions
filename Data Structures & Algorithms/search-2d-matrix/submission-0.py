class Solution:
    def get_1D_idx(self, row, col):
        return (row * self.n) + col 

    def get_2D_idx(self, idx):
        return (idx // self.n), (idx % self.n)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])
        l = 0
        r = (self.m * self.n) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            mid_row, mid_col = self.get_2D_idx(mid)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
