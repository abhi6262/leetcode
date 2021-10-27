class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def isvalid(i, j):
            return -1 < i < m and -1 < j < n
        
        dirs = {(1, 0): 3, (-1, 0): 4, (0, 1): 1, (0, -1): 2}
        distheap = [(0, 0, 0)]
        visited = set()
        dist, i, j = 0, 0, 0
        while distheap:
            dist, i, j = heappop(distheap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                break
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if isvalid(ni, nj) and (ni, nj) not in visited:
                    if dirs[(di, dj)] == grid[i][j]:
                        ndist = dist
                    else:
                        ndist = dist + 1
                    heappush(distheap, (ndist, ni, nj))
        return dist
