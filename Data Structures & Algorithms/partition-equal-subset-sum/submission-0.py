class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        whole = sum(nums)
        if whole % 2 != 0:
            return False
        targ = whole//2
        dp = [False]*(targ+1)
        dp[0] = True
        for num in nums:
            for s in range(targ,num-1,-1):
                if dp[s-num]:
                    dp[s] = True
        return dp[targ]