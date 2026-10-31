class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(t):
            ways = 0
            if t == 0:
                return 1 
            if t < 0:
                return 0
            if t in memo:
                return memo[t]
            for num in  nums:
                ways += dfs(t-num)
            memo[t] = ways
            return ways
        return dfs(target)