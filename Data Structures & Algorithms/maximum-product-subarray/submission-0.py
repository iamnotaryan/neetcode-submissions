class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]
        cumin = nums[0]
        glob = nums[0]
        for num in nums[1:]:
            prev_max = curr
            prev_min = cumin
            curr = max(prev_max*num,num,prev_min*num)
            cumin = min(prev_max*num,num,prev_min*num)
            glob = max(curr,glob)
        return glob