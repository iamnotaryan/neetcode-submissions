class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n= len(s)
        prefix = [[0]*26 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i].copy()
            prefix[i+1][ord(s[i])-ord('a')] += 1
        first = [-1]*26
        last = [-1]*26
        for i in range(n):
            x = ord(s[i])-ord('a')
            if first[x] == -1:
                first[x] = i
            last[x] = i
        ans = 0
        for i in range(26):
            if first[i] == -1 or first[i] == last[i]:
                continue
            l = first[i]
            r = last[i]
            for c in range(26):
                cnt = prefix[r][c] - prefix[l+1][c]
                if cnt > 0:
                    ans += 1
        return ans