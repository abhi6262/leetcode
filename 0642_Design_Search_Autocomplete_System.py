from heapq import heappush, heappushpop
class Node:
    def __init__(self):
        self.children = {}
        self.isend = 0
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.curr = self.root
        self.prefix = list()
        for i, s in enumerate(sentences):
            r = self.root
            for c in s:
                if c not in r.children:
                    n = Node()
                    r.children[c] = n
                r = r.children[c]
            r.isend = times[i]

    def input(self, c: str) -> List[str]:
        if c not in self.curr.children:
            if c == "#":
                self.curr.isend += 1
                self.curr = self.root
                self.prefix = []
            else:
                n = Node()
                self.curr.children[c] = n
                self.curr = n
            return []
        r = self.curr.children[c]
        self.prefix.append(c)
        o, self.curr = [], r
        w = self.prefix[:]
        def rec(n, w):
            if n.isend > 0:
                    heappush(o, (-n.isend, ("".join(w))))
            for c in n.children:
                w.append(c)
                rec(n.children[c], w)
            w.pop()
            return
        rec(r, w)
        result = []
        for i in range(min(len(o),3)):
            result.append((heappop(o)[1]))
        return result
        
        
        
        
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
