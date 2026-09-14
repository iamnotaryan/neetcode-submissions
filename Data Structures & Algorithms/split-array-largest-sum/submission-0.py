class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(max(nums),(sum(nums)+k-1)//k)
        high = sum(nums)
        def can_split(mid):
            curr = 0
            cnt = 1
            for num in nums:
                if curr + num <= mid:
                    curr += num
                else:
                    cnt += 1
                    curr = num
            return cnt <= k
        while low < high:
            mid = (low+high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid +1
        return low