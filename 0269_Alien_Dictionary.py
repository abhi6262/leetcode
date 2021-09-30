class Solution:
    def alienOrder(self, words: List[str]) -> str:
        lwords = len(words)
        if lwords == 0:
            return ""
        adjList, indeg, unique = defaultdict(list), defaultdict(int), set(c for c in words[0])
        for i in range(0, lwords - 1):
            fwrd, swrd = words[i], words[i+1]
            lfwrd, lswrd = len(fwrd), len(swrd)
            j, l = 0, min(lfwrd, lswrd)
            while j < l and fwrd[j] == swrd[j]:
                unique.add(swrd[j])
                j += 1
            if j == lswrd and j < lfwrd:
                return ""
            if j < l:
                adjList[fwrd[j]].append(swrd[j])
                indeg[swrd[j]] += 1
            while j < lswrd:
                unique.add(swrd[j])
                j += 1
        q, output = deque([]), []
        for node in unique:
            indeg[node] = indeg[node]
        for node in indeg:
            if indeg[node] == 0:
                q.append(node)
        while q:
            node = q.popleft()
            unique.remove(node)
            output.append(node)
            for n in adjList[node]:
                indeg[n] -= 1
                if indeg[n] == 0:
                    q.append(n)
            del(adjList[node])
            del(indeg[node])
        if indeg:
            return ""
        return ''.join(output)
        
            
