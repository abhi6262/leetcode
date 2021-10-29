class Solution:
    def distinctSubseqII(self, s: str) -> int:
        slen = len(s)
        dp = [0] * (slen + 1)
        lastoccur = [-1] * 26
        M = 10 ** 9 + 7
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            if lastoccur[index] == -1:
                dp[i + 1]  = (2 * dp[i] + 1) % M
            else:
                dp[i + 1] = (2 * dp[i] - dp[lastoccur[index]]) % M
            lastoccur[index] = i
        return dp[-1]
