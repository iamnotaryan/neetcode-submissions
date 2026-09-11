class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = 0
        seen = {0:-1}
        for i in range(len(nums)):
            pre += nums[i]
            pre %= k
            if pre in seen:
                if i - seen[pre] >= 2:
                    return True
            else:
                seen[pre] = i
        return False