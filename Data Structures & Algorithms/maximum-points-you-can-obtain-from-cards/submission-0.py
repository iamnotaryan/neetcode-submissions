class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        n = len(cardPoints)
        right = sum(cardPoints[n-k:n])
        left = 0
        ans = right
        for i in range(k):
            left += cardPoints[i]
            right -= cardPoints[n-k+i]
            ans = max(ans,left+right)
        return ans