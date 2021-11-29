class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        slen = len(s)
        output = []
        currword, currline = [], []
        def dfs(i):
            nonlocal currword, currline
            if i == slen:
                if not currword and currline:
                    output.append(' '.join(currline))
                return
            while i < slen:
                currword.append(s[i])
                curr = ''.join(currword)
                if curr in wordDict:
                    wordcopy, currword = currword, []
                    currline.append(curr)
                    dfs(i + 1)
                    currword = wordcopy
                    currline.pop()
                i += 1
        dfs(0)
        return output
