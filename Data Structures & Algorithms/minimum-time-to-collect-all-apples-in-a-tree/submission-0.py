class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[]for i in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node,parent):
            time = 0
            for child in adj[node]:
                if child == parent:
                    continue
                child_t = dfs(child,node)

                if child_t > 0 or hasApple[child]:
                    time += child_t + 2
            return time
        return dfs(0,-1)