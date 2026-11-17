class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix = 0 
        freq = [1,0]
        ans = 0
        for num in arr:
            prefix = (prefix+num) % 2 
            if prefix == 1:
                ans += freq[0]
            else:
                ans += freq[1]
            freq[prefix] += 1
        return ans%MOD