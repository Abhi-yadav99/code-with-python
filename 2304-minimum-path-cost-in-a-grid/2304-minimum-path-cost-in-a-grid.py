class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for i in range(m - 1):
            new_dp = [float('inf')] * n
            for j in range(n):
                for k in range(n):
                    cost = dp[j] + moveCost[grid[i][j]][k] + grid[i + 1][k]
                    if cost < new_dp[k]:
                        new_dp[k] = cost
            dp = new_dp
        return min(dp)