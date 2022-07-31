# Time Complexity: O(N)
# Space Complexity: O(N)

class DynamicProgramming:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]
        days = set(days)
        for i in range(1,len(dp)):
            if i in days:
                one = dp[i-1] if i-1 >= 0 else 0
                seven = dp[i-7] if i-7 >= 0 else 0
                thirty = dp[i-30] if i-30 >= 0 else 0
                dp[i] = min(one + costs[0], seven + costs[1], thirty + costs[2])
            
            else:
                dp[i] = dp[i-1]
        return dp[-1]
