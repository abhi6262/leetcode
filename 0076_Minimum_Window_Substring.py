class Solution:        
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        unique, curr = len(tCount.keys()), 0
        l = len(s)
        i, j = 0, 0
        start, end, window = -1, -1, float('inf')
        wCount = defaultdict(int)
        while j < l:
            c = s[j]
            if c in tCount:
                wCount[c] += 1
                if wCount[c] == tCount[c]:
                    curr += 1
            while curr == unique and i <= j:
                if window > (j-i+1):
                    window = j-i+1
                    start, end = i, j
                if s[i] in wCount:
                    wCount[s[i]] -= 1
                    if wCount[s[i]] < tCount[s[i]]:
                        curr -= 1
                i += 1
            j += 1
        return s[start:end+1] if start != -1 else ""
