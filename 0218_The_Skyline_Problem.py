class Heap:
    def __init__(self):
        self.h = []
        self.d = defaultdict(int)
        
    def bup(self) -> None:
        l = len(self.h)
        i, p_i = l-1, (l - 1) // 2
        while p_i > -1 and self.h[p_i] < self.h[i]:
            self.h[i], self.h[p_i] = self.h[p_i], self.h[i]
            i = p_i
            p_i = (i - 1) // 2
        return
        
    def bdown(self, i: int, l: int) -> None:
        c_1, c_2 = 2 * i + 1, 2 * i + 2
        while c_2 < l:
            if self.h[i] > self.h[c_1] and self.h[i] > self.h[c_2]:
                return
            else:
                c = c_1 if self.h[c_1] > self.h[c_2] else c_2
                self.h[i], self.h[c] = self.h[c], self.h[i]
                i = c
                c_1, c_2 = 2 * i + 1, 2 * i + 2
        if c_1 < l and self.h[i] < self.h[c_1]:
            self.h[i], self.h[c_1] = self.h[c_1], self.h[i]
        return
        
    def h_add(self, v: int) -> None:
        if not self.d[v]:
            self.h.append(v)
            self.bup()
        self.d[v] += 1
        
    def h_rem(self, v: int) -> None:
        if self.d[v] == 1:
            l = len(self.h)
            for i in range(l):
                if self.h[i] == v:
                    break
            self.h[i], self.h[-1] = self.h[-1], self.h[i]
            self.h.pop()
            self.bdown(i, l - 1)
        self.d[v] -= 1
        
from heapq import heapify, heappush

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #heap = Heap()
        #heap.h_add(0)
        heap = [0]
        points, o = [], []
        for x1, x2, h in buildings:
            points.append([x1, False, h])
            points.append([x2, True, h])
        def comp(o1: List, o2: List) -> None:
            if o1[0] == o2[0]:
                if o1[1] != o2[1]:
                    return o1[1] - o2[1]
                elif o1[1] == False:
                    return o2[2] - o1[2]
                else:
                    return o1[2] - o2[2]
            return o1[0] - o2[0]
        points.sort(key = functools.cmp_to_key(comp))
        for x, f, h in points:
            if f == False:
                if h > -heap[0]:
                    o.append([x, h])
                heappush(heap, -h)
            else:
                heap.remove(-h)
                heapify(heap)
                if h > -heap[0]:
                    o.append([x, -heap[0]])
        return o
                
