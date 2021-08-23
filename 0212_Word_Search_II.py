class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        o = set()
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        seen = set()
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['$'] = True
        def isvalid(i, j):
            return i > -1 and i < m and j > -1 and j < n
        word = []
        def rec(i, j, curr):
            f = False
            if '$' in curr:
                o.add("".join(word))
                if len(curr.keys()) == 1:
                    f = True
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if isvalid(ni, nj) and (ni, nj) not in seen and board[ni][nj] in curr:
                    seen.add((ni, nj))
                    word.append(board[ni][nj])
                    f_child = rec(ni, nj, curr[board[ni][nj]])
                    f &= f_child
                    seen.remove((ni, nj))
                    word.pop()
                    if f_child:
                        del(curr[board[ni][nj]])
            return f
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    seen.add((i, j))
                    word.append(board[i][j])
                    rec(i, j, root[board[i][j]])
                    seen.remove((i, j))
                    word.pop()
        return list(o)
