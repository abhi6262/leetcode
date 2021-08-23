class Solution:
    def __init__(self):
        self.ans = []
    def dc(self, l):
        t = []
        for s in l:
            t.append([])
            for c in s:
                t[-1].append(c)
        return t
    def totalNQueens(self, n: int) -> int:
        def rec(N: int, cb: List[List[str]]) -> None:
            if N == 1:
                for i in range(n):
                    if cb[N-1][i] == '.':
                        cb[N-1][i] = 'Q'
                        self.ans.append(cb)
                        break
                return
            for i in range(n):
                if cb[N-1][i] == '.':
                    temp = self.dc(cb)
                    cb[N-1][i] = 'Q'
                    for j in range(N-1):
                        cb[j][i] = '-'
                        i1, i2 = i - (N-1 - j), i + (N-1 - j)
                        if i1 > -1:
                            cb[j][i1] = '-'
                        if i2 < n:
                            cb[j][i2] = '-'
                    rec(N-1, cb)
                    cb = temp
            return
        cb = [['.'] * n for i in range(n)]
        rec(n, cb)
#        for l in self.ans:
#            for i in range(len(l)):
#                s = l[i]
#                for j in range(len(s)):
#                    if s[j] == '-':
#                        s[j] = '.'
#                l[i] = "".join(s)
        return len(self.ans)
