class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def isvalid(i, j):
            return -1 < i < m and -1 < j < n
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x, y in hits:
            grid[x][y] -= 1
            
        def isstable(i, j):
            if i == 0:
                return True
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if isvalid(ni, nj) and grid[ni][nj] == 2:
                    return True
            return False
        
        def dfs(i, j):
            grid[i][j] = 2
            changed = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if isvalid(ni, nj) and grid[ni][nj] == 1:
                    changed += dfs(ni, nj)
            return changed
        
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
                
        nhits = len(hits)
        result = [0] * nhits
        for i in range(nhits - 1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] == 1 and isstable(x, y):
                changed = dfs(x, y)
                result[i] = changed - 1
        return result
