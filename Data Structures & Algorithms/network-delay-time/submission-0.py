class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[]for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))

        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            c_dist,node= heapq.heappop(heap)
            if c_dist > dist[node]:
                continue
            
            for neighbor,weight in adj[node]:
                new_dist = c_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap,(new_dist,neighbor))
        new = max(dist[1:])
        if float('inf') in dist[1:]: 
            return -1
        else: 
            return new