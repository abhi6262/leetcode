class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def isvalid(i, j):
            return -1 < i < m and -1 < j < n
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        areas = defaultdict(int)
        def dfs(i, j, uid):
            area = 1
            grid[i][j] = uid
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if isvalid(ni, nj) and grid[ni][nj] == 1:
                    area += dfs(ni, nj, uid)
            return area
        uid = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[uid] = dfs(i, j, uid)
                    uid += 1
        marea = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    nuid = set()
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if isvalid(ni, nj):
                            nuid.add(grid[ni][nj])
                    marea = max(marea, 1 + sum(areas[i] for i in nuid))
        return marea if marea > -1 else m * n
