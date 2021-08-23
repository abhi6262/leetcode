class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        l = len(words[0])
        if l == 1:
            return [[x] for x in words]
        root = {}
        for word in words:
            curr = root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['$'] = True
        output, sqr = [], [['#'] * l for i in range(l)]
        def rec(n):
            curr = root
            if n == l:
                output.append([])
                for row in sqr:
                    output[-1].append("".join(row))
                return
            for i in range(n):
                if sqr[i][n] in curr:
                    curr = curr[sqr[i][n]]
                else:
                    return
            i = n
            while i < l and sqr[i][n] != '#':
                curr = curr[sqr[i][n]]
                i += 1
            if i == l:
                rec(n + 1)
            else:
                for child in curr:
                    sqr[n][i] = child
                    sqr[i][n] = child
                    rec(n)
                    sqr[n][i] = '#'
                    sqr[i][n] = '#'
                
        for word in words:
            for i in range(l):
                sqr[0][i] = word[i]
                sqr[i][0] = word[i]
            rec(1)
            for i in range(l):
                sqr[0][i] = '#'
                sqr[i][0] = '#'
                
        return output
            
