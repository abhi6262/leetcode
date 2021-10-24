class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        def isvalid(i, j):
            return -1 < i < m and -1 < j < n
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        currdist, i, j = 0, 0, 0
        visited, queue = {(0, 0, k)}, deque([(0, k, 0, 0)])
        while queue:
            currdist, currk, i, j = queue.popleft()
            if i == m-1 and j == n-1:
                break
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if isvalid(ni, nj) and (ni, nj, currk - grid[ni][nj]) not in visited and (grid[ni][nj] == 0 or currk > 0):
                    ndist, nk = currdist+1, currk - grid[ni][nj]
                    queue.append((ndist, nk, ni, nj))
                    visited.add((ni, nj, nk))
        if i == m-1 and j == n-1:
            return currdist
        return -1
