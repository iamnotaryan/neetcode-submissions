class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left = [0]*(n+1)
        right = [0]*(n+1)

        for i in range(n ):
            left[i+1] = left[i]+ (s[i]=="0")
            right[i+1] = right[i] + (s[i]=="1")

        ans = 0
        for i in range(1,n):
            zeros = left[i]
            ones = right[n] - right[i]
            ans = max(ans,zeros+ones)
        return ans