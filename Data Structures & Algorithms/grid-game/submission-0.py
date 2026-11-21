class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])

        top = [0]*(n+1)
        bottom = [0]*(n+1)
        for i in range(n):
            top[i+1] = top[i] + grid[0][i]
            bottom[i+1] = bottom[i] + grid[1][i]
        
        ans = float('inf')
        for i in range(n):
            toprem = top[n] - top[i+1]
            botrem = bottom[i]
            bot = max(toprem,botrem)
            ans = min(bot,ans)
        return ans