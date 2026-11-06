class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)
        def dfs(i): # state of dfs is it will return the difference of alice and bob if we start choosing from ith index
            if i == n:
                return 0 # if reached end of list then no more stone left so return 0
            if i in memo:
                return memo[i]
            ans = float('-inf')
            tot = 0
            for take in range(1,4):
                if i + take > n: # to handle out of index error
                    break
                tot += stoneValue[i+take-1]
                diff = tot - dfs(i+take)
                ans = max(ans,diff)
            memo[i] = ans

            return memo[i]
        ans = dfs(0)
        if ans >0:
            return ('Alice')
        elif ans < 0:
            return ('Bob')
        else:
            return ('Tie')
