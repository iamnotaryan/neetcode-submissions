class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remove = len(nums)
        target = sum(nums)%p
        if target == 0:
            return 0
        dic = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            rem = (prefix)%p
            need = (rem-target)%p
            if need in dic:
                remove = min(remove,i-dic[need])
            dic[rem] = i
        return remove if remove < len(nums) else -1