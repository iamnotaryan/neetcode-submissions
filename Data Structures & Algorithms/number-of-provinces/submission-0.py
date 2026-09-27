class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        def dfs(node):
            visited[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)
        return provinces
