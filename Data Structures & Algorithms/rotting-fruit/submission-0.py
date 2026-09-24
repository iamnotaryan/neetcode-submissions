class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        m = len(grid)
        mu = 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            a = len(queue)
            if fresh == 0:
                return mu
            for _ in range(a):
                i,j = queue.popleft()
                for ni,nj in directions:
                    ni = i+ni
                    nj = j + nj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni,nj))
                        fresh -= 1
            mu +=1
        if fresh > 0:
            return -1
        return mu
