class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        slen = len(s)
        dp = dict()
        def memo(start, end):
            if start > end:
                return 0
            if (start, end) in dp:
                return dp[(start, end)]
            if start == end:
                dp[(start, end)] = 1
            elif start == end - 1:
                if s[start] != s[end]:
                    dp[(start, end)] = 2
                else:
                    dp[(start, end)] = 1
            else:
                ans = memo(start, end - 1) + 1
                for mid in range(end - 1, start - 1, -1):
                    if s[end] == s[mid]:
                        ans = min(ans, memo(start, mid - 1) + memo(mid + 1, end))
                dp[(start, end)] = ans
            return dp[(start, end)]
        ans = memo(0, slen - 1)
        return ans
