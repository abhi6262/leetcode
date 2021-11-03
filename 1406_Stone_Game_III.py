class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        nstones = len(stoneValue)
        dp = [float('-inf')] * (nstones + 1)
        dp[-1] = 0
        dp[-2] = stoneValue[-1]
        for i in range(nstones - 2, -1, -1):
            score = 0
            for j in range(i + 1, i + 4):
                if j > nstones:
                    break
                score += stoneValue[j - 1]
                dp[i] = max(dp[i], score - dp[j])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
