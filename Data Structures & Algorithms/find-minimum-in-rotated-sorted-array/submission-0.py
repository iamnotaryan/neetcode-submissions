class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        gmin = float('inf')
        while left <= right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                lmin = nums[left]
                left = mid +1
            else:
                lmin = nums[mid]
                right = mid - 1 
            gmin = min(gmin,lmin)
        return gmin 