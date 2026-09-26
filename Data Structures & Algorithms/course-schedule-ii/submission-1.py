class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        res = []
        adj = [[]for _ in range(numCourses)]
        indegree = [0]*(numCourses)
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                res.append(i)
        cnt = 0 
        while queue:
            course = queue.popleft()
            cnt += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    res.append(neighbor)
        if len(res) == numCourses:
            return res
        else:
            return []