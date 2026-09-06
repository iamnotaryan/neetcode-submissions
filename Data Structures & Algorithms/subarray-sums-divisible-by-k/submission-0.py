class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        cnt = 0
        freq = {0:1}
        for num in nums:
            prefix += num
            rem = prefix % k
            if rem in freq:
                cnt += freq[rem]
            freq[rem] = freq.get(rem,0) + 1
        return cnt