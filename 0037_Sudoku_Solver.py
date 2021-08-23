class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def sub(i: int, j: int) -> int:
            if i < 3:
                if j < 3:
                    return 0
                elif j < 6:
                    return 1
                else:
                    return 2
            elif i < 6:
                if j < 3:
                    return 3
                elif j < 6:
                    return 4
                else:
                    return 5
            else:
                if j < 3:
                    return 6
                elif j < 6:
                    return 7
                else:
                    return 8
        r, c, s = {}, {}, {}
        for i in range(9):
            for j in range(9):
                if i not in r:
                    r[i] = set()
                if j not in c:
                    c[j] = set()
                sb = sub(i, j)
                if sb not in s:
                    s[sb] = set()
                if board[i][j] == '.':
                    continue
                r[i].add(board[i][j])
                c[j].add(board[i][j])
                s[sb].add(board[i][j])
        def rec(i: int, j: int) -> bool:
            if board[i][j] == '.':
                sb = sub(i, j)
                for ki in range(1, 10):
                    k = str(ki)
                    if k not in r[i] and k not in c[j] and k not in s[sb]:
                        board[i][j] = k
                        if i == 8 and j == 8:
                            return True
                        r[i].add(k)
                        c[j].add(k)
                        s[sb].add(k)
                        if j < 8:
                            ni, nj = i, j + 1
                        else:
                            ni, nj = i + 1, 0
                        f = rec(ni, nj)
                        if f == True:
                            return f
                        board[i][j] = '.'
                        r[i].remove(k)
                        c[j].remove(k)
                        s[sb].remove(k)
            else:
                if i == 8 and j == 8:
                    return True
                j += 1
                i += j // 9
                j = j % 9
                f = rec(i, j)
                if f == True:
                    return f
            return False
        rec(0, 0)
