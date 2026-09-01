class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(1,len(prefix)):
            if prefix[i-1] == prefix[len(prefix)-1] - prefix[i]: return i-1
        return -1             