class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        allvisited = (1 << n) - 1
        queue = deque([])
        visited = set()
        pathlen = 0
        for i in range(n):
            queue.append((1 << i, i, 0))
            visited.add((1 << i, i))
        while queue:
            state, node, pathlen = queue.popleft()
            if state == allvisited:
                break
            for neighbor in graph[node]:
                nstate = state | (1 << neighbor)
                if (nstate, neighbor) not in visited:
                    visited.add((nstate, neighbor))
                    queue.append((nstate, neighbor, pathlen + 1))
        return pathlen
