class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjmat = [set() for i in range(n)]
        for ai, bi in edges:
            adjmat[ai].add(bi)
            adjmat[bi].add(ai)
        pathmap = {i: {} for i in range(n)}
        visited = {0}
        answer = [0] * n
        def dfs(node):
            nnodes, sumpath = 1, 0
            for i in adjmat[node]:
                if i not in visited:
                    visited.add(i)
                    cnode, csumpath = dfs(i)
                    pathmap[node][i] = (cnode, csumpath)
                    nnodes += cnode
                    sumpath += (csumpath + cnode)
            return (nnodes, sumpath)
        rnode, rsumpath = dfs(0)
        answer[0] = rsumpath
        stack = [0]
        while stack:
            parent = stack.pop()
            tchildren = sum(pathmap[parent][node][0] for node in pathmap[parent])
            for children in pathmap[parent]:
                answer[children] = answer[parent] + tchildren - (2 * pathmap[parent][children][0]) + (n - tchildren)
                stack.append(children)
        return answer
            
