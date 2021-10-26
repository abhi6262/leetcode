class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        m, INF = len(targetPath), float('inf')
        adjlist = defaultdict(set)
        for road in roads:
            a, b = road[0], road[1]
            adjlist[a].add(b)
            adjlist[b].add(a)
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = [0, None] if names[j] == targetPath[i] else [1, None]
                else:
                    dp[i][j] = [INF, None]
                    for prev in adjlist[j]:
                        if dp[i - 1][prev][0] < dp[i][j][0]:
                            dp[i][j] = [dp[i - 1][prev][0], prev]
                    if names[j] != targetPath[i]:
                        dp[i][j][0] += 1
        output = deque([])
        minedit, start = INF, None
        for i in range(n):
            if dp[-1][i][0] < minedit:
                minedit = dp[-1][i][0]
                start = i
        for i in range(m):
            output.appendleft(start)
            start = dp[m - 1 - i][start][1]
        return output
        
