from heapq import heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.lmin = 0
        self.lmax = 0
        

    def addNum(self, num: int) -> None:
        if self.lmax - self.lmin == 1:
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
            self.lmin += 1
        else:
            heappush(self.maxheap, -heappushpop(self.minheap, num))
            self.lmax += 1
        

    def findMedian(self) -> float:
        if self.lmax == self.lmin:
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
