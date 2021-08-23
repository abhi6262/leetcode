class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l = len(s)
        i = 0
        r = s[::-1]
        while i < l:
            if s[:l - i] == r[i:]:
                break
            i += 1
        return r[:i] + s
