class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp = [0] * len(cost)
        for i in range(len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        result = min(dp[-1],dp[-2])
        return result