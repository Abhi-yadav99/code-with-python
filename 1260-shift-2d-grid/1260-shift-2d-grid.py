class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        result = [[0] * n for _ in range(m)]

        k %= m * n

        for i in range(m):
            for j in range(n):
                new_pos = (i * n + j + k) % (m * n)
                new_row = new_pos // n
                new_col = new_pos % n

                result[new_row][new_col] = grid[i][j]

        return result